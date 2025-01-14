# AUTO GENERATED ON 2023-08-11 AT 16:40:52
# DO NOT EDIT BY HAND!
#
# To regenerate file, run
#
#     python dev/generate-tests.py
#

# fmt: off

import cupy
import pytest

import awkward as ak
import awkward._connect.cuda as ak_cu

cupy_backend = ak._backends.CupyBackend.instance()

def test_cuda_awkward_ListArray32_validity_1():
    starts = cupy.array([2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], dtype=cupy.int32)
    stops = cupy.array([3, 2, 4, 5, 3, 4, 2, 5, 3, 4, 6, 11], dtype=cupy.int32)
    length = 3
    lencontent = 3
    funcC = cupy_backend['awkward_ListArray_validity', cupy.int32, cupy.int32]

def test_cuda_awkward_ListArray32_validity_2():
    starts = cupy.array([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], dtype=cupy.int32)
    stops = cupy.array([8, 4, 5, 6, 5, 5, 7], dtype=cupy.int32)
    length = 3
    lencontent = 3
    funcC = cupy_backend['awkward_ListArray_validity', cupy.int32, cupy.int32]

def test_cuda_awkward_ListArray32_validity_3():
    starts = cupy.array([1, 4, 5, 6, 5, 5, 7, 1, 2, 1, 3, 1, 5, 3, 2], dtype=cupy.int32)
    stops = cupy.array([1, 4, 5, 6, 5, 5, 7, 1, 2, 1, 3, 1, 5, 3, 2], dtype=cupy.int32)
    length = 3
    lencontent = 3
    funcC = cupy_backend['awkward_ListArray_validity', cupy.int32, cupy.int32]
    funcC(starts, stops, length, lencontent)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")

def test_cuda_awkward_ListArray32_validity_4():
    starts = cupy.array([1, 7, 6, 1, 3, 4, 2, 5, 2, 3, 1, 2, 3, 4, 5, 6, 7, 1, 2], dtype=cupy.int32)
    stops = cupy.array([1, 9, 6, 2, 4, 5, 3, 6, 3, 4, 2, 4, 5, 5, 7, 8, 2, 3], dtype=cupy.int32)
    length = 3
    lencontent = 3
    funcC = cupy_backend['awkward_ListArray_validity', cupy.int32, cupy.int32]

def test_cuda_awkward_ListArray32_validity_5():
    starts = cupy.array([0, 0, 0, 0, 0, 0, 0, 0], dtype=cupy.int32)
    stops = cupy.array([1, 1, 1, 1, 1, 1, 1, 1], dtype=cupy.int32)
    length = 3
    lencontent = 3
    funcC = cupy_backend['awkward_ListArray_validity', cupy.int32, cupy.int32]
    funcC(starts, stops, length, lencontent)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")

