from pattern_search import find_n, find_kmp, find_kr
import pytest


def read_from_file(file_path) -> str:
    with open(file_path) as file:
        data = file.read().rstrip()
    return data


BENCHMARK_ROUNDS = 5
TEXT = read_from_file("lab5-pattern_search/pan-tadeusz.txt")
TEXT_LIST = TEXT.split()

SIZES = [100, 300, 500, 700, 1000]
FUNCTIONS = [find_n, find_kmp, find_kr]
ids = ["Naive", "Knuth Morris Pratt", "Karp Rabin"]


@pytest.mark.parametrize("size", SIZES)
@pytest.mark.parametrize("function, function_name", zip(FUNCTIONS, ids), ids=ids)
def test_pattern_search(size, function, function_name, benchmark):
    def func():
        for pattern in TEXT_LIST[:size]:
            function(substring=pattern, text=TEXT)
    benchmark.extra_info["function"] = function_name
    benchmark.extra_info["size"] = size
    benchmark.pedantic(func, rounds=BENCHMARK_ROUNDS)
