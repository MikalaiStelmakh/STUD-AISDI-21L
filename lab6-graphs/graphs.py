import argparse
from typing import List, Tuple, Dict

Point = Tuple[int, int]


class InvalidGraph(ValueError):
    pass


class Graph():
    def __init__(self, graph: List[List[int]]) -> None:
        """
        Parameters:
            graph: Two dimensional list (graph) to be initialized.
        Returns:
            None
        Raises:
            InvalidGraph: if rows on board are not of the same length.
        """
        if not all(len(graph[0]) == len(row) for row in graph):
            raise InvalidGraph("The rows must be the same length.\n")
        self.graph = graph

    def find_source_dest_positions(self, value) -> List[Point]:
        """
        Parameters:
            value: source and destination point values.
        Returns:
            List of 2 tuples with coordinates of "value" in given graph.
        Raises:
            InvalidGraph: if there is more or less than 2 "values" in graph.
        """
        positions = []
        for row_index, row in enumerate(self.graph):
            if value in row:
                for col_index, element in enumerate(row):
                    if element == value:
                        positions.append((row_index, col_index))
        if len(positions) != 2:
            raise InvalidGraph("There must be exactly one source and one destination value.\n")
        return positions

    def minDistance(self, dist: Dict[int, Point], queue: List[Point]):
        """
        Parameters:
            dist: dictionary with point as a value
                  and distance to it from the source as a key.
            queue: list of unvisited points.
        Returns:
            Not visited Point with the minimum distance from the source.
        """
        minimum = float("Inf")
        min_index = -1
        for i in dist.keys():
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def possible(self, pos, x=0, y=0):
        """
        Parameters:
            pos: current position.
            x, y: offset from the current position.
        Returns:
            Point of current position plus offset if the point exists.
        """
        posNext = (pos[0] + x, pos[1] + y)
        if 0 <= posNext[0] < len(self.graph) and 0 <= posNext[1] < len(self.graph[0]):
            return posNext
        return None

    def dijkstra(self, value: int) -> List[Point]:
        """
        Parameters:
            value: source and destination point values
                   between which finding the shortest path.
        Returns:
            List with shortest path ordered list of Points.
        """
        dist = dict()
        parent = dict()
        queue = []
        for row in range(len(self.graph)):
            for column in range(len(self.graph[row])):
                dist[(row, column)] = float("Inf")
                parent[(row, column)] = tuple()
                queue.append((row, column))
        start, finish = self.find_source_dest_positions(value)
        dist[start] = 0
        while finish in queue:
            vertexFrom = self.minDistance(dist, queue)
            queue.remove(vertexFrom)
            xOffset, yOffset = [1, -1, 0, 0], [0, 0, 1, -1]
            for dir in range(4):
                vertexTo = self.possible(vertexFrom,
                                        x=xOffset[dir], y=yOffset[dir])
                if vertexTo:
                    i, j = vertexTo
                    if dist[vertexFrom] + self.graph[i][j] < dist[vertexTo]:
                        dist[vertexTo] = dist[vertexFrom] + self.graph[i][j]
                        parent[vertexTo] = vertexFrom
        step = finish
        path = []
        while step != start:
            path.append(step)
            step = parent[step]
        path.append(step)
        path.reverse()
        return path

    def find_shortest_path(self, value: int) -> str:
        """
        Parameters:
            value: source and destination point values
                   between which finding the shortest path.
        Returns:
            String with printed path.
        """
        path = self.dijkstra(value)
        result = " " + "-"*len(self.graph[0]) + " " + "\n"
        sorted_path = [sorted([x[1] for x in path if x[0] == row_num])
                       for row_num in range(len(self.graph))]
        for row_num, row in enumerate(sorted_path):
            result += "|"
            for column_num in range(len(self.graph[0])):
                result += str(self.graph[row_num][column_num]) if column_num in row else " "
            result += "|\n"
        result += " " + "-"*len(self.graph[0]) + " "
        return result

    @classmethod
    def make_from_txt(_class, path):
        """
        Parameters:
            _class: the class whose object will be created.
            path: path to .txt file with board.
        Returns:
            Object of _class with graph as an argument.
        Raises:
            InvalidGraph: if board in .txt file includes invalid characters.
        """
        result = []
        with open(path) as f:
            for line in f:
                line = line.rstrip()
                result.append([number for number in line])
        for row_index, row in enumerate(result):
            for col_index, col in enumerate(row):
                try:
                    result[row_index][col_index] = int(col)
                except ValueError:
                    raise InvalidGraph("Invalid character in: "
                                       f"Line {row_index+1}, column {col_index+1}.\n")
        return _class(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    graph = Graph.make_from_txt(args.file)
    path = graph.find_shortest_path(0)
    print(path)
