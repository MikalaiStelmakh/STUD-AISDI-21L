from abstract_heap import AbstractHeap


class Node:
    def __init__(self, value=None):
        self.val = value
        self.parent = None
        self.firstChild = None
        self.secondChild = None
        self.thirdChild = None
        self.fourthChild = None


class Heap(AbstractHeap):
    def __init__(self, dimension, value=None):
        self.dimension = dimension
        self.root = None if not value else Node(value)
        self.data = [] if not value else [self.root]

    def peek(self):
        return self.root

    def findParentIndex(self, index):
        return (index - 1) // self.dimension

    def findFirstChildIndex(self, index):
        return self.dimension * index + 1

    def findSecondChildIndex(self, index):
        return self.dimension * index + 2

    def findThirdChildIndex(self, index):
        return self.dimension * index + 3

    def findFourthChildIndex(self, index):
        return self.dimension * index + 4

    def heapify(self, start_index):
        for index, node in enumerate(self.data[start_index:]):
            index += start_index
            if index == 0:
                self.root = node
                continue
            parentIndex = self.findParentIndex(index)
            node.parent = self.data[parentIndex]
            parentFirstChildIndex = self.findFirstChildIndex(parentIndex)
            parentSecondChildIndex = self.findSecondChildIndex(parentIndex)
            if parentFirstChildIndex == index:
                node.parent.firstChild = node
            elif parentSecondChildIndex == index:
                node.parent.secondChild = node
            elif self.dimension > 3:
                parentThirdChildIndex = self.findThirdChildIndex(parentIndex)
                if parentThirdChildIndex == index:
                    node.parent.thirdChild = node
                parentFourthChildIndex = self.findFourthChildIndex(parentIndex)
                if parentFourthChildIndex == index:
                    node.parent.fourthChild = node
            elif self.dimension > 2:
                parentThirdChildIndex = self.findThirdChildIndex(parentIndex)
                if parentThirdChildIndex == index:
                    node.parent.thirdChild = node

    def push(self, values):
        current_index = len(self.data)
        for value in values:
            self.data.append(Node(value))
        self.heapify(current_index)

    def pop(self):
        deleted_node = self.data[0]
        del self.data[0]
        self.heapify(0)
        return deleted_node

    def pop_n_times(self, number_of_repetitions):
        """Same as using pop function n times.
        Much more efficient when removing a large number of elements."""
        del self.data[:number_of_repetitions]
        self.heapify(0)

    def get_raw_data(self):
        return self.data

    def printTree(self):
        if self.dimension == 2:
            return self.printTwoDimension(self.data[0])

    def printTwoDimension(self, node, level=0):
        if node is not None:
            self.printTwoDimension(node.secondChild, level + 1)
            print('\t' * level + '->' + str(node.val))
            self.printTwoDimension(node.firstChild, level + 1)


if __name__ == '__main__':
    heap = Heap(dimension=2, value=30)
    heap.push([20, 40, 50, 4, 9, 10, 19])
    heap.printTree()
    print('------------------------')
    print(heap.pop())
    heap.printTree()
    print('------------------------')
    print(heap.peek().val)
    print(len(heap))
    heap.printTree()