# AUTO GENERATED ON 2023-08-11 AT 16:40:52
# DO NOT EDIT BY HAND!
#
# To regenerate file, run
#
#     python dev/generate-tests.py
#

# fmt: off

import ctypes
import pytest

from awkward_cpp.cpu_kernels import lib

def test_cpuawkward_UnionArray8_regular_index_getsize_1():
    size = [123]
    size = (ctypes.c_int64*len(size))(*size)
    fromtags = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromtags = (ctypes.c_int8*len(fromtags))(*fromtags)
    length = 3
    funcC = getattr(lib, 'awkward_UnionArray8_regular_index_getsize')
    ret_pass = funcC(size, fromtags, length)
    pytest_size = [1]
    assert size[:len(pytest_size)] == pytest.approx(pytest_size)
    assert not ret_pass.str

def test_cpuawkward_UnionArray8_regular_index_getsize_2():
    size = [123]
    size = (ctypes.c_int64*len(size))(*size)
    fromtags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    fromtags = (ctypes.c_int8*len(fromtags))(*fromtags)
    length = 3
    funcC = getattr(lib, 'awkward_UnionArray8_regular_index_getsize')
    ret_pass = funcC(size, fromtags, length)
    pytest_size = [2]
    assert size[:len(pytest_size)] == pytest.approx(pytest_size)
    assert not ret_pass.str

def test_cpuawkward_UnionArray8_regular_index_getsize_3():
    size = [123]
    size = (ctypes.c_int64*len(size))(*size)
    fromtags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    fromtags = (ctypes.c_int8*len(fromtags))(*fromtags)
    length = 3
    funcC = getattr(lib, 'awkward_UnionArray8_regular_index_getsize')
    ret_pass = funcC(size, fromtags, length)
    pytest_size = [2]
    assert size[:len(pytest_size)] == pytest.approx(pytest_size)
    assert not ret_pass.str

def test_cpuawkward_UnionArray8_regular_index_getsize_4():
    size = [123]
    size = (ctypes.c_int64*len(size))(*size)
    fromtags = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromtags = (ctypes.c_int8*len(fromtags))(*fromtags)
    length = 3
    funcC = getattr(lib, 'awkward_UnionArray8_regular_index_getsize')
    ret_pass = funcC(size, fromtags, length)
    pytest_size = [1]
    assert size[:len(pytest_size)] == pytest.approx(pytest_size)
    assert not ret_pass.str

def test_cpuawkward_UnionArray8_regular_index_getsize_5():
    size = [123]
    size = (ctypes.c_int64*len(size))(*size)
    fromtags = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromtags = (ctypes.c_int8*len(fromtags))(*fromtags)
    length = 3
    funcC = getattr(lib, 'awkward_UnionArray8_regular_index_getsize')
    ret_pass = funcC(size, fromtags, length)
    pytest_size = [1]
    assert size[:len(pytest_size)] == pytest.approx(pytest_size)
    assert not ret_pass.str

