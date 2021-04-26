from heap import Node, Heap
import pytest


DIMENSIONS = [2, 3, 4]


@pytest.mark.parametrize("dimension", DIMENSIONS)
def test_initialize_empty_heap(dimension):
    heap = Heap(dimension=dimension)
    assert heap.root is None


@pytest.mark.parametrize("dimension", DIMENSIONS)
def test_initialize_heap(dimension):
    heap = Heap(dimension=dimension, value=10)
    assert heap.root.val == 10


@pytest.mark.parametrize("dimension", DIMENSIONS)
def test_push_to_empty_heap(dimension):
    heap = Heap(dimension=dimension)
    heap.push([10, 20, 30])
    assert heap.root.val == 10
    assert heap.root.firstChild.val == 20
    assert heap.root.secondChild.val == 30


def test_push_to_two_dimension_heap():
    heap = Heap(dimension=2, value=30)
    heap.push([20, 40, 50, 4])
    assert heap.root.val == 30
    assert heap.root.firstChild.val == 20
    assert heap.root.secondChild.val == 40
    assert heap.root.firstChild.firstChild.val == 50
    assert heap.root.firstChild.secondChild.val == 4


def test_push_to_three_dimension_heap():
    heap = Heap(dimension=3, value=30)
    heap.push([20, 40, 50, 4])
    assert heap.root.val == 30
    assert heap.root.firstChild.val == 20
    assert heap.root.secondChild.val == 40
    assert heap.root.thirdChild.val == 50
    assert heap.root.firstChild.firstChild.val == 4


def test_push_to_four_dimension_heap():
    heap = Heap(dimension=4, value=30)
    heap.push([20, 40, 50, 4])
    assert heap.root.val == 30
    assert heap.root.firstChild.val == 20
    assert heap.root.secondChild.val == 40
    assert heap.root.thirdChild.val == 50
    assert heap.root.fourthChild.val == 4