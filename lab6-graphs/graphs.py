import argparse
from typing import List, Tuple


def read_from_txt(path) -> List[int]:
    """
    Parameters:
        path: path to file to be readed.
    Returns:
        Two dimensional list of numbers from file.
    """
    result = []
    with open(path) as f:
        for line in f:
            line = line.rstrip()
            result.append([int(number) for number in line])
    return result


class Graph():
    def __init__(self, array: List[List[int]]) -> None:
        if not all(len(array[0]) == len(row) for row in array):
            raise ValueError("The rows must be the same length")
        self.array = array
        self.source, self.destination = self.find_zero_positions()

    def find_zero_positions(self) -> List[Tuple[int]]:
        """
        Parameters:
            None
        Returns:
            List of 2 tuples with coordinates of zeros in given list.
        Raises:
            ValueError: if there is more or less than 2 zeros in list.
        """
        positions = []
        for row_index, row in enumerate(self.array):
            if 0 in row:
                positions.append((row_index, row.index(0)))
        if len(positions) != 2:
            raise ValueError("The list should contain exactly two zeros")
        return positions

    def dijkstra(self):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    array = read_from_txt(args.file)
    graph = Graph(array)

