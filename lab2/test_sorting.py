from Sorting import (
    bubbleSort, selectionSort,
    mergeSort, merge, readText
)
import pytest
import sys


sys.setrecursionlimit(100000)
SIZES = [2000, 4000, 6000, 8000, 10000]
FUNCTIONS = [bubbleSort, selectionSort, mergeSort]
TEXT = readText("lab2/pan-tadeusz.txt", 10000)


def test_merge():
    list1 = [3, 4, 7, 9]
    list2 = [4, 5, 6, 8]
    assert merge(list1, list2) == [3, 4, 4, 5, 6, 7, 8, 9]


def test_readText():
    assert readText("lab2/pan-tadeusz.txt", 5) == [
        'Adam', 'Mickiewicz', 'Pan', 'Tadeusz', 'czyli'
    ]


@pytest.mark.parametrize("func", FUNCTIONS)
def test_panTadeusz(func):
    text = readText("lab2/pan-tadeusz.txt", 100)
    assert func(text) == sorted(text)


@pytest.mark.parametrize("func", FUNCTIONS)
@pytest.mark.parametrize("size", SIZES)
def test_benchmark(func, size, benchmark):
    benchmark.extra_info["func"] = func.__name__
    benchmark.extra_info["size"] = size
    benchmark(func, TEXT[:size])
