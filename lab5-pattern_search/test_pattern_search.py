from pattern_search import find_n, find_kmp, find_kr
import random
import pytest

FUNCTIONS = [find_n, find_kmp, find_kr]
TEXT = """  Nam porttitor, elit quis rhoncus molestie, lorem massa
            sollicitudin leo, ac auctor orci magna at est. Donec in
            ipsum congue, lobortis purus non, euismod lectus.
            Vestibulum rhoncus gravida auctor."""


@pytest.mark.parametrize("function", FUNCTIONS)
def test_empty_text(function):
    assert function(substring="aBc", text="") == []


@pytest.mark.parametrize("function", FUNCTIONS)
def test_empty_substring(function):
    assert function(substring="", text="abcd") == [0, 1, 2, 3]


@pytest.mark.parametrize("function", FUNCTIONS)
def test_substring_equals_text(function):
    assert function(substring=TEXT, text=TEXT) == [0]


@pytest.mark.parametrize("function", FUNCTIONS)
def test_substring_longer_than_text(function):
    substring = TEXT + "a"
    assert function(substring=substring, text=TEXT) == []


@pytest.mark.parametrize("function", FUNCTIONS)
def test_text_dont_contains_substring(function):
    assert function(substring="hello", text="world") == []


@pytest.mark.parametrize("function", FUNCTIONS)
def test_pattern_searching(function):
    assert function(substring="AABA", text="AABAACAADAABAABA") == [0, 9, 12]


def test_random_letters():
    text = "".join(random.choices(["a", "b"], k=100))
    substring = "".join(random.choices(["a", "b"], k=10))
    assert find_n(substring, text) == find_kmp(substring, text)
    assert find_n(substring, text) == find_kr(substring, text)