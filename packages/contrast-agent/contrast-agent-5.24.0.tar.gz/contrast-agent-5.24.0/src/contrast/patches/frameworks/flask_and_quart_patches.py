# -*- coding: utf-8 -*-
# Copyright © 2023 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
import sys
import functools
from contrast_vendor.wrapt import register_post_import_hook

import contrast
from contrast.agent import scope
from contrast.agent.middlewares.route_coverage.common import build_route
from contrast.agent.middlewares.route_coverage.flask_routes import create_routes
from contrast.agent.policy import patch_manager
from contrast.utils.patch_utils import build_and_apply_patch, wrap_and_watermark
from contrast.utils.decorators import fail_quietly
from contrast.utils.safe_import import safe_import_list

from contrast.agent.assess.rules.config import (
    FlaskSessionAgeRule,
    FlaskSecureFlagRule,
    FlaskHttpOnlyRule,
)

from contrast_vendor import structlog as logging

FLASK_MODULE_NAME = "flask"
QUART_MODULE_NAME = "quart"

logger = logging.getLogger("contrast")


@functools.lru_cache(maxsize=1)
def _get_flask_app_type():
    return tuple(safe_import_list("flask.Flask"))


@functools.lru_cache(maxsize=1)
def _get_quart_app_type():
    return tuple(safe_import_list("quart.Quart"))


def build_flask_full_dispatch_request_patch(orig_func, patch_policy):
    del patch_policy

    def full_dispatch_request_patch(wrapped, instance, args, kwargs):
        try:
            result = wrapped(*args, **kwargs)
        finally:
            do_first_request_analysis(instance)
            do_flask_route_observation(instance)
        return result

    return wrap_and_watermark(orig_func, full_dispatch_request_patch)


def build_quart_full_dispatch_request_patch(orig_func, patch_policy):
    del patch_policy

    async def full_dispatch_request_patch(wrapped, instance, args, kwargs):
        try:
            result = await wrapped(*args, **kwargs)
        finally:
            do_first_request_analysis(instance)
            do_quart_route_observation(instance, *args, **kwargs)
        return result

    return wrap_and_watermark(orig_func, full_dispatch_request_patch)


@fail_quietly("Failed to run first-request analysis")
@scope.with_contrast_scope
def do_first_request_analysis(app_instance):
    from contrast.agent import agent_state

    if not agent_state.is_first_request():
        return

    do_config_scanning(app_instance)
    do_route_discovery(app_instance)


@fail_quietly("unable to perform Flask route observation")
@scope.with_contrast_scope
def do_flask_route_observation(flask_instance):
    logger.debug("Performing Flask route observation")

    flask_ctx = None
    try:
        from flask.globals import request_ctx

        flask_ctx = request_ctx
    except ImportError:
        from flask.globals import _request_ctx_stack

        flask_ctx = _request_ctx_stack.top

    do_route_observation(flask_ctx, flask_instance)


@fail_quietly("unable to perform Quart route observation")
@scope.with_contrast_scope
def do_quart_route_observation(quart_instance, *args, **kwargs):
    logger.debug("Performing Quart route observation")

    quart_ctx = args[0] if len(args) > 0 else kwargs.get("request_context")
    do_route_observation(quart_ctx, quart_instance)


@fail_quietly("unable to perform Flask/Quart route observation")
@scope.with_contrast_scope
def do_route_observation(framework_ctx, app_instance):
    if not framework_ctx:
        logger.debug("unable to get framework ctx for route observation")
        return

    context = contrast.CS__CONTEXT_TRACKER.current()
    if context is None:
        logger.debug("not in request context - skipping route observation")
        return

    endpoint = getattr(framework_ctx.request.url_rule, "endpoint", None)
    view_func = app_instance.view_functions.get(endpoint)
    if view_func is None:
        logger.debug("did not find endpoint for route observation")
        return

    context.view_func = view_func
    context.view_func_str = build_route(view_func.__name__, view_func)
    logger.debug("Observed route: %s", context.view_func_str)


@fail_quietly("Failed to run config scanning rules")
def do_config_scanning(app_instance):
    logger.debug("Running config scanning rules")
    for rule in [FlaskSessionAgeRule, FlaskSecureFlagRule, FlaskHttpOnlyRule]:
        rule().apply(app_instance)


@fail_quietly("unable to perform route discovery")
def do_route_discovery(app_instance):
    from contrast.agent import agent_state

    discovered_routes = create_routes(app_instance)
    agent_state.update_routes(discovered_routes)
    logger.debug(
        "Discovered the following routes: %s",
        [f"{route.verb} {route.url}" for route in discovered_routes.values()],
    )


def patch_flask(flask_module):
    build_and_apply_patch(
        flask_module.Flask,
        "full_dispatch_request",
        build_flask_full_dispatch_request_patch,
    )


def patch_quart(quart_module):
    build_and_apply_patch(
        quart_module.Quart,
        "full_dispatch_request",
        build_quart_full_dispatch_request_patch,
    )


def register_patches():
    register_post_import_hook(patch_flask, FLASK_MODULE_NAME)
    register_post_import_hook(patch_quart, QUART_MODULE_NAME)


def reverse_patches():
    flask_module = sys.modules.get(FLASK_MODULE_NAME)
    if flask_module:
        patch_manager.reverse_patches_by_owner(flask_module.Flask)

    quart_module = sys.modules.get(QUART_MODULE_NAME)
    if quart_module:
        patch_manager.reverse_patches_by_owner(quart_module.Quart)
