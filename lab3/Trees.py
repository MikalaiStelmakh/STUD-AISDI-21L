class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def insert_list(self, numbers):
        for number in numbers:
            self.insert(number)

    def search_list(self, numbers):
        return [self.search(number) for number in numbers]

    def search(self, val):
        if self.root is None:
            return None
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if val == currentNode.val:
            return currentNode
        elif val < currentNode.val and currentNode.left is not None:
            return self.findNode(currentNode.left, val)
        elif val > currentNode.val and currentNode.right is not None:
            return self.findNode(currentNode.right, val)
        else:
            return None

    def delete_list(self, numbers):
        return [self.delete(number) for number in numbers]

    def printTree(self):
        self._print(self.root)

    def _print(self, node, level=0):
        if node is not None:
            self._print(node.right, level + 1)
            print('\t' * level + '->', node.val)
            self._print(node.left, level + 1)


class BST(TreeNode):
    def __init__(self, val=None):
        super().__init__(val)
        self.root = None

    def insert_list(self, numbers):
        return super().insert_list(numbers)

    def insert(self, val):
        if not self.val:
            self.val = val
            self.root = self
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BST(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BST(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def delete_list(self, numbers):
        return super().delete_list(numbers)

    def delete(self, val):
        if self is None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def search_list(self, numbers):
        return super().search_list(numbers)

    def printTree(self):
        return super().printTree()


class AVLTree(TreeNode):
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            for value in values:
                self.root = self._insert(self.root, value)

    def insert_list(self, numbers):
        return super().insert_list(numbers)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        elif key < root.val:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete_list(self, numbers):
        return super().delete_list(numbers)

    def delete(self, key):
        return self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        elif key < root.val:
            root.left = self._delete(root.left, key)

        elif key > root.val:
            root.right = self._delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def search_list(self, numbers):
        return super().search_list(numbers)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def printTree(self):
        return super().printTree()


if __name__ == '__main__':
    tree = AVLTree([])
    tree.insert_list([10, 20, 30, 5, 40, 50])
    tree.insert_list([15, 25])
    tree.delete_list([20, 30])
    print(tree.search_list([10, 15]))
    tree.printTree()
    print('-------------------------------------')
    bst = BST()
    bst.insert_list([10, 20, 30, 5, 40, 50])
    bst.insert_list([15, 25])
    bst.delete_list([20, 30])
    print(bst.search_list([10, 15]))
    bst._print(bst)