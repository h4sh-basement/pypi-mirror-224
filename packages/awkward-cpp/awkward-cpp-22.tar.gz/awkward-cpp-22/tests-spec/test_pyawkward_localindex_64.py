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

def test_pyawkward_localindex_64_1():
    toindex = [123, 123, 123]
    length = 3
    funcPy = getattr(kernels, 'awkward_localindex_64')
    funcPy(toindex=toindex, length=length)
    pytest_toindex = [0, 1, 2]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)

