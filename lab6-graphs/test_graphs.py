import pytest
from graphs import InvalidGraph, Graph


def test_make_from_txt():
    graph = Graph.make_from_txt("lab6-graphs/boards/example.txt")
    assert graph.graph == [[1, 1, 1, 1, 2, 2],
                           [1, 0, 4, 1, 2, 2],
                           [9, 4, 2, 1, 1, 1],
                           [9, 9, 6, 4, 1, 1],
                           [9, 9, 0, 4, 1, 1],
                           [9, 9, 1, 1, 1, 1]]


def test_invalid_size():
    array = [[1, 0, 3, 4, 5],
             [4, 2, 4, 5, 6],
             [6, 3, 0, 1]]
    with pytest.raises(InvalidGraph):
        Graph(array)


def test_three_source_destination_values():
    array = [[1, 0, 4, 4, 6],
             [0, 5, 4, 2, 7],
             [1, 5, 7, 0, 3]]
    graph = Graph(array)
    with pytest.raises(InvalidGraph):
        graph.find_shortest_path(value=0)


def test_find_shortest_path_example():
    """
    111122
    104122
    942111
    996411
    990411
    991111
    """
    graph = Graph.make_from_txt("lab6-graphs/boards/example.txt")
    assert graph.find_shortest_path(0) == (" ------ \n"
                                           "| 111  |\n"
                                           "| 0 1  |\n"
                                           "|   11 |\n"
                                           "|    1 |\n"
                                           "|  0 1 |\n"
                                           "|  111 |\n"
                                           " ------ ")


def test_find_shortest_path_board1():
    """
    087142345
    191111111
    171233441
    151353211
    111243221
    111589177
    436431430
    """
    graph = Graph.make_from_txt("lab6-graphs/boards/board1.txt")
    assert graph.find_shortest_path(0) == (" --------- \n"
                                           "|0        |\n"
                                           "|1 1111111|\n"
                                           "|1 1     1|\n"
                                           "|1 1     1|\n"
                                           "|111     1|\n"
                                           "|        7|\n"
                                           "|        0|\n"
                                           " --------- ")


def test_find_shortest_path_board2():
    """
    0111111114
    9997982423
    9999999919
    9011111114
    """
    graph = Graph.make_from_txt("lab6-graphs/boards/board2.txt")
    assert graph.find_shortest_path(0) == (" ---------- \n"
                                           "|011111111 |\n"
                                           "|        2 |\n"
                                           "|        1 |\n"
                                           "| 01111111 |\n"
                                           " ---------- ")


def test_find_shortest_path_board3():
    """
    42034
    24913
    73057
    """
    graph = Graph.make_from_txt("lab6-graphs/boards/board3.txt")
    assert graph.find_shortest_path(0) == (" ----- \n"
                                           "|  0  |\n"
                                           "|  9  |\n"
                                           "|  0  |\n"
                                           " ----- ")