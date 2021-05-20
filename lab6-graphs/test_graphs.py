import pytest
from graphs import read_from_txt, Graph


def test_read_from_txt():
    assert read_from_txt("lab6-graphs/example.txt") == [[1, 1, 1, 1, 2, 2],
                                                        [1, 0, 4, 1, 2, 2],
                                                        [9, 4, 2, 1, 1, 1],
                                                        [9, 9, 6, 4, 1, 1],
                                                        [9, 9, 0, 4, 1, 1],
                                                        [9, 9, 1, 1, 1, 1]]


def test_invalid_size():
    array = [[1, 0, 3, 4, 5],
             [4, 2, 4, 5, 6],
             [6, 3, 0, 1]]
    with pytest.raises(ValueError):
        Graph(array)


def test_three_zeros():
    array = [[1, 0, 4, 4, 6],
             [0, 5, 4, 2, 7],
             [1, 5, 7, 0, 3]]
    with pytest.raises(ValueError):
        Graph(array)


def test_find_shortest_path():
    array = [[1, 1, 1, 1, 2, 2],
             [1, 0, 4, 1, 2, 2],
             [9, 4, 2, 1, 1, 1],
             [9, 9, 6, 4, 1, 1],
             [9, 9, 0, 4, 1, 1],
             [9, 9, 1, 1, 1, 1]]
    graph = Graph(array)
    assert graph.find_shortest_path() == """ 111
                                             0 1
                                               11
                                                1
                                              0 1
                                              111"""