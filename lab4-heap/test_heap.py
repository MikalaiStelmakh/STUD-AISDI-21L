from heap import Heap
import pytest

DIMENSIONS = [2, 3, 4]


@pytest.mark.parametrize("dimension", DIMENSIONS)
def test_initialize_heap(dimension):
    heap = Heap(dimension=dimension)
    assert heap.get_raw_data() == []


@pytest.mark.parametrize("dimension", DIMENSIONS)
def test_push_single_value_to_empty_heap(dimension):
    heap = Heap(dimension=dimension)
    heap.push(10)
    assert heap.get_raw_data() == [10]


@pytest.mark.parametrize("dimension", DIMENSIONS)
def test_push_to_heap(dimension):
    heap = Heap(dimension=dimension)
    heap.push(20)
    heap.push(10)
    heap.push(30)
    heap.push(19)
    heap.push(22)
    assert heap.get_raw_data() == [10, 19, 20, 22, 30]


@pytest.mark.parametrize("dimension", DIMENSIONS)
def test_pop_from_heap(dimension):
    heap = Heap(dimension=dimension)
    heap.push(20)
    heap.push(10)
    heap.push(30)
    heap.push(19)
    heap.push(22)
    assert heap.pop() == 10
    assert heap.get_raw_data() == [19, 20, 30, 22]


@pytest.mark.parametrize("dimension", DIMENSIONS)
def test_get_heap_length(dimension):
    heap = Heap(dimension=dimension)
    heap.push(20)
    heap.push(10)
    heap.push(30)
    heap.push(19)
    heap.push(22)
    assert len(heap) == 5
