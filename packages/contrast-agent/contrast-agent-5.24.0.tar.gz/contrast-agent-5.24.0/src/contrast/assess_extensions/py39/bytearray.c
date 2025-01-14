/*
 * Copyright © 2023 Contrast Security, Inc.
 * See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
 */
/* THIS FILE WAS AUTOMATICALLY GENERATED BY HOOKSPY */
/* Python requires its own header to always be included first */
#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <contrast/assess/patches.h>
#include <contrast/assess/propagate.h>
#include <contrast/assess/scope.h>
#include <contrast/assess/utils.h>

typedef PyObject *(*fastcall_func)(PyObject *, PyObject *const *, Py_ssize_t);
typedef PyObject *(*fastcall_kwargs_func)(
    PyObject *, PyObject *const *, Py_ssize_t, PyObject *);

#define BYTEARRAY_DECODE_OFFSET 10
#define BYTEARRAY_REPLACE_OFFSET 35
#define BYTEARRAY_SPLIT_OFFSET 45
#define BYTEARRAY_RSPLIT_OFFSET 43
#define BYTEARRAY_JOIN_OFFSET 27
#define BYTEARRAY_CAPITALIZE_OFFSET 5
#define BYTEARRAY_TITLE_OFFSET 50
#define BYTEARRAY_CENTER_OFFSET 6
#define BYTEARRAY_EXPANDTABS_OFFSET 12
#define BYTEARRAY_PARTITION_OFFSET 32
#define BYTEARRAY_LJUST_OFFSET 28
#define BYTEARRAY_LOWER_OFFSET 29
#define BYTEARRAY_LSTRIP_OFFSET 30
#define BYTEARRAY_RJUST_OFFSET 41
#define BYTEARRAY_RSTRIP_OFFSET 44
#define BYTEARRAY_RPARTITION_OFFSET 42
#define BYTEARRAY_SPLITLINES_OFFSET 46
#define BYTEARRAY_STRIP_OFFSET 48
#define BYTEARRAY_SWAPCASE_OFFSET 49
#define BYTEARRAY_TRANSLATE_OFFSET 51
#define BYTEARRAY_UPPER_OFFSET 52
#define BYTEARRAY_ZFILL_OFFSET 53
#define BYTEARRAY_REMOVEPREFIX_OFFSET 36
#define BYTEARRAY_REMOVESUFFIX_OFFSET 37

fastcall_kwargs_func bytearray_decode_orig;
fastcall_func bytearray_replace_orig;
fastcall_kwargs_func bytearray_split_orig;
fastcall_kwargs_func bytearray_rsplit_orig;
binaryfunc bytearray_join_orig;
unaryfunc bytearray_capitalize_orig;
unaryfunc bytearray_title_orig;
fastcall_func bytearray_center_orig;
fastcall_kwargs_func bytearray_expandtabs_orig;
binaryfunc bytearray_partition_orig;
fastcall_func bytearray_ljust_orig;
unaryfunc bytearray_lower_orig;
fastcall_func bytearray_lstrip_orig;
fastcall_func bytearray_rjust_orig;
fastcall_func bytearray_rstrip_orig;
binaryfunc bytearray_rpartition_orig;
fastcall_kwargs_func bytearray_splitlines_orig;
fastcall_func bytearray_strip_orig;
unaryfunc bytearray_swapcase_orig;
fastcall_kwargs_func bytearray_translate_orig;
unaryfunc bytearray_upper_orig;
binaryfunc bytearray_zfill_orig;
binaryfunc bytearray_removeprefix_orig;
binaryfunc bytearray_removesuffix_orig;

HOOK_TERNARY_FASTCALL(bytearray_decode);
PyObject *bytearray_replace_new(
    PyObject *self, PyObject *const *args, Py_ssize_t nargs) {
    /* In Py37 the replace method type moved to METH_FASTARGS. This means that
     * instead of args being passed as a tuple, they are passed as a C array
     * that contains PyObjects. We need to check whether there is the number of
     * args that we expect, and whether the arg we care about is not NULL.
     * Specifically, we want args[1] since it represents the "new" string in
     * the replacement.
     */
    PyObject *hook_args = pack_args_tuple(args, nargs);
    PyObject *result = bytearray_replace_orig(self, args, nargs);

    if (result == NULL || nargs < 2 || args[1] == NULL)
        goto cleanup_and_exit;

    if (result == self)
        goto cleanup_and_exit;

    call_string_propagator(
        "propagate_bytearray_replace", self, result, hook_args, NULL);

cleanup_and_exit:
    Py_XDECREF(hook_args);
    return result;
}

PyObject *bytearray_split_new(
    PyObject *self, PyObject *const *args, Py_ssize_t nargs, PyObject *kwnames) {
    PyObject *result = bytearray_split_orig(self, args, nargs, kwnames);
    PyObject *args_tuple = pack_args_tuple(args, nargs);
    PyObject *kwargs = pack_kwargs_dict(args, nargs, kwnames);

    if (result == NULL || PySequence_Length(result) == 1)
        goto cleanup_and_exit;

    call_string_propagator(
        "propagate_bytearray_split", (PyObject *)self, result, args_tuple, kwargs);

cleanup_and_exit:
    Py_XDECREF(args_tuple);
    Py_XDECREF(kwargs);
    return result;
}

PyObject *bytearray_rsplit_new(
    PyObject *self, PyObject *const *args, Py_ssize_t nargs, PyObject *kwnames) {
    PyObject *result = bytearray_rsplit_orig(self, args, nargs, kwnames);
    PyObject *args_tuple = pack_args_tuple(args, nargs);
    PyObject *kwargs = pack_kwargs_dict(args, nargs, kwnames);

    if (result == NULL || PySequence_Length(result) == 1)
        goto cleanup_and_exit;

    call_string_propagator(
        "propagate_bytearray_rsplit", (PyObject *)self, result, args_tuple, kwargs);

cleanup_and_exit:
    Py_XDECREF(args_tuple);
    Py_XDECREF(kwargs);
    return result;
}

PyObject *bytearray_join_new(PyObject *self, PyObject *args) {
    PyObject *list = PySequence_List(args);

    /* Converting args to a list might legitimately raise an exception in some cases.
     * We need to be sure we don't suppress that exception to maintain original app
     * behavior. We've seen this before when args is a generator.
     */
    if (list == NULL) {
        return NULL;
    }

    /* In Py36+ we also hook an internal function that is called by this
     * function in order to propagate fstring formatting. We still want to have
     * a separate hook for join so that the events are reported differently.
     * This means that we need to go into scope when calling the original
     * function here so that we don't propagate twice.
     */
    enter_propagation_scope();
    PyObject *result = bytearray_join_orig((PyObject *)self, list);
    exit_propagation_scope();

    PyObject *prop_args = PyTuple_Pack(1, list);

    if (prop_args == NULL || result == NULL)
        goto cleanup_and_exit;

    call_string_propagator(
        "propagate_bytearray_join", (PyObject *)self, result, prop_args, NULL);

cleanup_and_exit:
    Py_XDECREF(list);
    Py_XDECREF(prop_args);
    return result;
}

HOOK_UNARYFUNC(bytearray_capitalize);
HOOK_UNARYFUNC(bytearray_title);
HOOK_FASTCALL(bytearray_center);
HOOK_TERNARY_FASTCALL(bytearray_expandtabs);
HOOK_BINARYFUNC(bytearray_partition);
HOOK_FASTCALL(bytearray_ljust);
HOOK_UNARYFUNC(bytearray_lower);
HOOK_FASTCALL(bytearray_lstrip);
HOOK_FASTCALL(bytearray_rjust);
HOOK_FASTCALL(bytearray_rstrip);
HOOK_BINARYFUNC(bytearray_rpartition);
HOOK_TERNARY_FASTCALL(bytearray_splitlines);
HOOK_FASTCALL(bytearray_strip);
HOOK_UNARYFUNC(bytearray_swapcase);
HOOK_TERNARY_FASTCALL(bytearray_translate);
HOOK_UNARYFUNC(bytearray_upper);
HOOK_BINARYFUNC(bytearray_zfill);
HOOK_BINARYFUNC(bytearray_removeprefix);
HOOK_BINARYFUNC(bytearray_removesuffix);

CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_decode, 10)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_replace, 35)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_split, 45)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_rsplit, 43)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_join, 27)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_capitalize, 5)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_title, 50)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_center, 6)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_expandtabs, 12)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_partition, 32)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_ljust, 28)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_lower, 29)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_lstrip, 30)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_rjust, 41)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_rstrip, 44)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_rpartition, 42)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_splitlines, 46)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_strip, 48)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_swapcase, 49)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_translate, 51)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_upper, 52)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_zfill, 53)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_removeprefix, 36)
CREATE_HOOK_METHOD(PyByteArray_Type, bytearray_removesuffix, 37)

static PyMethodDef methods[] = {
    {"apply_decode_hook",
     apply_bytearray_decode_hook,
     METH_O,
     "Enable bytearray.decode hook"},
    {"apply_replace_hook",
     apply_bytearray_replace_hook,
     METH_O,
     "Enable bytearray.replace hook"},
    {"apply_split_hook",
     apply_bytearray_split_hook,
     METH_O,
     "Enable bytearray.split hook"},
    {"apply_rsplit_hook",
     apply_bytearray_rsplit_hook,
     METH_O,
     "Enable bytearray.rsplit hook"},
    {"apply_join_hook",
     apply_bytearray_join_hook,
     METH_O,
     "Enable bytearray.join hook"},
    {"apply_capitalize_hook",
     apply_bytearray_capitalize_hook,
     METH_O,
     "Enable bytearray.capitalize hook"},
    {"apply_title_hook",
     apply_bytearray_title_hook,
     METH_O,
     "Enable bytearray.title hook"},
    {"apply_center_hook",
     apply_bytearray_center_hook,
     METH_O,
     "Enable bytearray.center hook"},
    {"apply_expandtabs_hook",
     apply_bytearray_expandtabs_hook,
     METH_O,
     "Enable bytearray.expandtabs hook"},
    {"apply_partition_hook",
     apply_bytearray_partition_hook,
     METH_O,
     "Enable bytearray.partition hook"},
    {"apply_ljust_hook",
     apply_bytearray_ljust_hook,
     METH_O,
     "Enable bytearray.ljust hook"},
    {"apply_lower_hook",
     apply_bytearray_lower_hook,
     METH_O,
     "Enable bytearray.lower hook"},
    {"apply_lstrip_hook",
     apply_bytearray_lstrip_hook,
     METH_O,
     "Enable bytearray.lstrip hook"},
    {"apply_rjust_hook",
     apply_bytearray_rjust_hook,
     METH_O,
     "Enable bytearray.rjust hook"},
    {"apply_rstrip_hook",
     apply_bytearray_rstrip_hook,
     METH_O,
     "Enable bytearray.rstrip hook"},
    {"apply_rpartition_hook",
     apply_bytearray_rpartition_hook,
     METH_O,
     "Enable bytearray.rpartition hook"},
    {"apply_splitlines_hook",
     apply_bytearray_splitlines_hook,
     METH_O,
     "Enable bytearray.splitlines hook"},
    {"apply_strip_hook",
     apply_bytearray_strip_hook,
     METH_O,
     "Enable bytearray.strip hook"},
    {"apply_swapcase_hook",
     apply_bytearray_swapcase_hook,
     METH_O,
     "Enable bytearray.swapcase hook"},
    {"apply_translate_hook",
     apply_bytearray_translate_hook,
     METH_O,
     "Enable bytearray.translate hook"},
    {"apply_upper_hook",
     apply_bytearray_upper_hook,
     METH_O,
     "Enable bytearray.upper hook"},
    {"apply_zfill_hook",
     apply_bytearray_zfill_hook,
     METH_O,
     "Enable bytearray.zfill hook"},
    {"apply_removeprefix_hook",
     apply_bytearray_removeprefix_hook,
     METH_O,
     "Enable bytearray.removeprefix hook"},
    {"apply_removesuffix_hook",
     apply_bytearray_removesuffix_hook,
     METH_O,
     "Enable bytearray.removesuffix hook"},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef bytearray_module_def = {
    PyModuleDef_HEAD_INIT,
    "bytearray_hooks",
    "methods for hooking bytearray methods",
    -1,
    methods,
    NULL,
    NULL,
    NULL,
    NULL};

PyObject *create_bytearray_hook_module(PyObject *self, PyObject *arg) {
    return PyModule_Create(&bytearray_module_def);
}
