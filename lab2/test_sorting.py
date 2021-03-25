from Sorting import (
    bubbleSort, selectionSort,
    mergeSort, merge
)


def test_merge():
    list1 = [3, 4, 7, 9]
    list2 = [4, 5, 6, 8]
    assert merge(list1, list2) == [3, 4, 4, 5, 6, 7, 8, 9]


def test_bubbleSort(benchmark):
    assert benchmark(bubbleSort, [6, 5, 4, 8, 3, 4, 9, 7]) == [3, 4, 4, 5, 6, 7, 8, 9]


def test_selectionSort(benchmark):
    assert benchmark(selectionSort, [6, 5, 4, 8, 3, 4, 9, 7]) == [3, 4, 4, 5, 6, 7, 8, 9]


def test_mergeSort(benchmark):
    assert benchmark(mergeSort, [6, 5, 4, 8, 3, 4, 9, 7]) == [3, 4, 4, 5, 6, 7, 8, 9]
