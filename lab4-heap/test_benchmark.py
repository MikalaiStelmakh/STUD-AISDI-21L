from heap import Heap
import pytest
import random
import copy


BENCHMARK_ROUNDS = 10
NUMBERS = random.sample(range(1, 30001), 10000)
SIZES = [1000, 2000, 4000, 6000, 8000, 10000]
DIMENSIONS = [2, 3, 4]
FILLED_HEAPS = [Heap(dimension=2), Heap(dimension=3), Heap(dimension=4)]
for heap in FILLED_HEAPS:
    heap.push(NUMBERS)
ids = [2, 3, 4]


@pytest.mark.parametrize("dimension", DIMENSIONS)
@pytest.mark.parametrize("size", SIZES)
def test_push_n_elements_time(dimension, size, benchmark):
    """Benchmark pushing {size} number of elements
    to {dimension}-ary heap."""
    def func():
        heap = Heap(dimension=dimension)
        heap.push(NUMBERS[:size])
    benchmark.extra_info["function"] = "push"
    benchmark.extra_info["dimension"] = dimension
    benchmark.extra_info["size"] = size
    benchmark.pedantic(func, rounds=BENCHMARK_ROUNDS)


@pytest.mark.parametrize("heap, dimension", zip(FILLED_HEAPS, DIMENSIONS), ids=ids)
@pytest.mark.parametrize("size", SIZES)
def test_pop_n_times_time(heap, dimension, size, benchmark):
    """Benchmark pop the topmost element {size} times
    from {dimension}-ary heap."""
    def func():
        heapCopy = copy.deepcopy(heap)
        for _ in range(size):
            heapCopy.pop()
    benchmark.extra_info["function"] = "pop_n_times"
    benchmark.extra_info["dimension"] = dimension
    benchmark.extra_info["size"] = size
    benchmark.pedantic(func, rounds=BENCHMARK_ROUNDS)


@pytest.mark.parametrize("heap, dimension", zip(FILLED_HEAPS, DIMENSIONS), ids=ids)
@pytest.mark.parametrize("size", SIZES)
def test_pop_n_times_method_time(heap, dimension, size, benchmark):
    """Benchmark Heap class method 'pop_n_times' that pops the topmost element {size} times from {dimension}-ary heap.
    Much more efficient when removing a large number of elements.
    Time is inversely propotional to the time of using pop function {size} times"""
    def func():
        heapCopy = copy.deepcopy(heap)
        heapCopy.pop_n_times(size)
    benchmark.extra_info["function"] = "pop_n_times_method"
    benchmark.extra_info["dimension"] = dimension
    benchmark.extra_info["size"] = size
    benchmark.pedantic(func, rounds=BENCHMARK_ROUNDS)
