import pytest
from graphs import Graph


def test_make_from_txt():
    graph = Graph.make_from_txt("lab6-graphs/example.txt")
    assert graph.array == [[1, 1, 1, 1, 2, 2],
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


def test_three_source_destination_values():
    array = [[1, 0, 4, 4, 6],
             [0, 5, 4, 2, 7],
             [1, 5, 7, 0, 3]]
    graph = Graph(array)
    with pytest.raises(ValueError):
        graph.find_shortest_path(value=0)


def test_find_shortest_path():
    array = [[1, 1, 1, 1, 2, 2],
             [1, 0, 4, 1, 2, 2],
             [9, 4, 2, 1, 1, 1],
             [9, 9, 6, 4, 1, 1],
             [9, 9, 0, 4, 1, 1],
             [9, 9, 1, 1, 1, 1]]
    graph = Graph(array)
    assert graph.find_shortest_path(0) == (" 111  \n"
                                           " 0 1  \n"
                                           "   11 \n"
                                           "    1 \n"
                                           "  0 1 \n"
                                           "  111 ")
