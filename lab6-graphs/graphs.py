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

    def minDistance(self, dist, queue):
        minimum = float("Inf")
        min_index = -1
        for i in dist.keys():
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def posible(self, pos, x=0, y=0):
        posNext = (pos[0] + x, pos[1] + y)
        if 0 <= posNext[0] < len(self.array) and 0 <= posNext[1] < len(self.array[0]):
            return posNext
        return None

    def dijkstra(self):
        dist = dict()
        parent = dict()
        queue = []
        for row in range(len(self.array)):
            for column in range(len(self.array[row])):
                dist[(row, column)] = float("Inf")
                parent[(row, column)] = tuple()
                queue.append((row, column))

        start, finish = self.find_zero_positions()

        dist[start] = 0

        while finish in queue:
            vertexFrom = self.minDistance(dist, queue)
            queue.remove(vertexFrom)
            xOffset, yOffset = [1, -1, 0, 0], [0, 0, 1, -1]
            for dir in range(4):
                vertexTo = self.posible(vertexFrom,
                                        x=xOffset[dir], y=yOffset[dir])
                if vertexTo:
                    i, j = vertexTo
                    if dist[vertexFrom] + self.array[i][j] < dist[vertexTo]:
                        dist[vertexTo] = dist[vertexFrom] + self.array[i][j]
                        parent[vertexTo] = vertexFrom
        step = finish
        path = []
        while step != start:
            path.append(step)
            step = parent[step]
        path.append(step)
        path.reverse()
        return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    array = read_from_txt(args.file)
    graph = Graph(array)

