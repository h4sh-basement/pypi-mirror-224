# AUTO GENERATED ON 2023-08-11 AT 16:40:52
# DO NOT EDIT BY HAND!
#
# To regenerate file, run
#
#     python dev/generate-tests.py
#

# fmt: off

import pytest
import kernels

def test_pyawkward_UnionArray8_U32_regular_index_1():
    toindex = [123, 123, 123]
    current = [123, 123, 123]
    size = 3
    fromtags = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    length = 3
    funcPy = getattr(kernels, 'awkward_UnionArray8_U32_regular_index')
    funcPy(toindex=toindex, current=current, size=size, fromtags=fromtags, length=length)
    pytest_toindex = [0, 1, 2]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)
    pytest_current = [3, 0, 0]
    assert current[:len(pytest_current)] == pytest.approx(pytest_current)

def test_pyawkward_UnionArray8_U32_regular_index_2():
    toindex = [123, 123, 123]
    current = [123, 123, 123]
    size = 3
    fromtags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    length = 3
    funcPy = getattr(kernels, 'awkward_UnionArray8_U32_regular_index')
    funcPy(toindex=toindex, current=current, size=size, fromtags=fromtags, length=length)
    pytest_toindex = [0, 1, 2]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)
    pytest_current = [0, 3, 0]
    assert current[:len(pytest_current)] == pytest.approx(pytest_current)

def test_pyawkward_UnionArray8_U32_regular_index_3():
    toindex = [123, 123, 123]
    current = [123, 123, 123]
    size = 3
    fromtags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    length = 3
    funcPy = getattr(kernels, 'awkward_UnionArray8_U32_regular_index')
    funcPy(toindex=toindex, current=current, size=size, fromtags=fromtags, length=length)
    pytest_toindex = [0, 1, 2]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)
    pytest_current = [0, 3, 0]
    assert current[:len(pytest_current)] == pytest.approx(pytest_current)

def test_pyawkward_UnionArray8_U32_regular_index_4():
    toindex = [123, 123, 123]
    current = [123, 123, 123]
    size = 3
    fromtags = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    length = 3
    funcPy = getattr(kernels, 'awkward_UnionArray8_U32_regular_index')
    funcPy(toindex=toindex, current=current, size=size, fromtags=fromtags, length=length)
    pytest_toindex = [0, 1, 2]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)
    pytest_current = [3, 0, 0]
    assert current[:len(pytest_current)] == pytest.approx(pytest_current)

def test_pyawkward_UnionArray8_U32_regular_index_5():
    toindex = [123, 123, 123]
    current = [123, 123, 123]
    size = 3
    fromtags = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    length = 3
    funcPy = getattr(kernels, 'awkward_UnionArray8_U32_regular_index')
    funcPy(toindex=toindex, current=current, size=size, fromtags=fromtags, length=length)
    pytest_toindex = [0, 1, 2]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)
    pytest_current = [3, 0, 0]
    assert current[:len(pytest_current)] == pytest.approx(pytest_current)

