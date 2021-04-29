from abstract_heap import AbstractHeap


class Heap(AbstractHeap):
    def __init__(self, dimension: int):
        if dimension < 2:
            raise ValueError("Invalid dimension value")
        self.dimension = dimension
        self._data = []

    def shift_down(self, startpos: int, pos: int) -> None:
        """ If new element is less that its parent, swap them
            and do the same for all subsequent elements."""
        newitem = self._data[pos]
        # Follow the path to the root, moving parents down until finding
        # a place newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) // 2
            parent = self._data[parentpos]
            # If (inserted element < parent) - swap them
            # and check all elements after parent's index.
            if newitem < parent:
                self._data[pos] = parent
                pos = parentpos
                continue
            # Break if inserted element >= parent.
            break
        # Insert new element to list.
        self._data[pos] = newitem

    def shift_up(self, pos: int) -> None:
        """ If element at {pos} is greater that element at child pos, swap them
            and do the same for all subsequent elements."""
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

    def peek(self) -> C:
        """Get the topmost element without changing the heap."""
        return self._data[0]

    def push(self, item: C) -> None:
        """Add an element to the heap."""
        self._data.append(item)
        self.shift_down(0, len(self._data)-1)

    def pop(self) -> C:
        """Remove the topmost element from the heap and return it."""
        deleted = self._data[0]
        del self._data[0]
        if self._data:
            self.shift_up(0)
        return deleted

    def get_raw_data(self) -> List[C]:
        """Get the underlying data storage."""
        return self._data

    def _print(self, index=0, level=0):
        """Prints out a tree."""
        children = [self._data[index*self.dimension + indx] for indx
                    in range(1, self.dimension+1)
                    if index*self.dimension + indx < len(self._data)]
        if children:
            left_children = [children[i] for i in range(self.dimension // 2) if i < len(children)]
            right_children = children[self.dimension//2:]
            for child in reversed(right_children):
                new_index = (children.index(child)+1) + index*self.dimension
                self._print(new_index, level+1)
        print("\t"*level + "->", self._data[index])
        if children:
            for child in reversed(left_children):
                new_index = (children.index(child)+1) + index*self.dimension
                self._print(new_index, level+1)


if __name__ == '__main__':
    heap = Heap(4)
    heap.push(20)
    heap.push(10)
    heap.push(30)
    heap.push(19)
    heap.push(22)
    print(heap.get_raw_data())
    heap._print()
