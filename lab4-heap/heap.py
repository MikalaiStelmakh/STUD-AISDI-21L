from abstract_heap import AbstractHeap
import random


class Heap(AbstractHeap):
    def __init__(self, dimension: int):
        if dimension < 2:
            raise ValueError("Invalid dimension value")
        self.dimension = dimension
        self._data = []

    def shift_down(self, startpos, pos):
        newitem = self._data[pos]
        # Follow the path to the root, moving parents down until finding
        # a place newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) // 2
            parent = self._data[parentpos]
            if newitem < parent:
                self._data[pos] = parent
                pos = parentpos
                continue
            break
        self._data[pos] = newitem

    def shift_up(self, pos):
        endpos = len(self._data)
        startpos = pos
        newitem = self._data[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self._data[childpos] < self._data[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            self._data[pos] = self._data[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self._data[pos] = newitem
        self.shift_down(startpos, pos)

    def peek(self):
        """Get the topmost element without changing the heap."""
        return self._data[0]

    def push(self, item):
        """Add an element to the heap."""
        self._data.append(item)
        self.shift_down(0, len(self._data)-1)

    def pop(self):
        """Remove the topmost element from the heap and return it."""
        deleted = self._data[0]
        del self._data[0]
        if self._data:
            self.shift_up(0)
        return deleted

    def get_raw_data(self):
        """Get the underlying data storage."""
        return self._data

    def pprint(self, root: int = 0, depth: int = 0) -> str:
        str_: str = ""

        leftmost_child = root*self.dimension + 1
        children = list(range(
            leftmost_child,
            min(len(self), leftmost_child + self.dimension)
        ))

        left_children = children[:self.dimension//2]
        right_children = children[self.dimension//2:]

        for child in reversed(right_children):
            str_ += self.pprint(child, depth + 4)
        str_ += " "*depth + repr(self._data[root]) + "\n"
        for child in reversed(left_children):
            str_ += self.pprint(child, depth + 4)

        return str_

    # def _print(self, index=0, level=0):
    #     children = [self._data[index*self.dimension + indx] for indx in range(1, self.dimension+1)
    #                 if index*self.dimension + indx < len(self._data)]
    #     for child in reversed(children):
    #         new_index = children.index(child) + 1
    #         self._print(index+new_index, level+1)
    #         print("\t"*(level+1) + "->", child)


if __name__ == '__main__':
    heap = Heap(2)

    NUMBERS = random.sample(range(1, 30001), 10000)
    for number in NUMBERS:
        heap.push(number)
    for _ in range(10000):
        heap.pop()



