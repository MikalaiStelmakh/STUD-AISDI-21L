from Trees import AVLTree


def test_init_1():
    avltree = AVLTree([10, 20, 30])
    assert avltree.root.val == 20


def test_init_2():
    avltree = AVLTree()
    assert avltree.root is None


def test_init_3():
    avltree = AVLTree([1, 2, 3, 4, 5, 6, 7])
    assert avltree.root.val == 4


def test_insert_find_1():
    avltree = AVLTree([1, 2, 3, 4])
    avltree.insert(5)
    assert avltree.findNode(5).val == 5


def test_insert_find_2():
    avltree = AVLTree([1, 2, 3, 4])
    avltree.insert(2.5)
    assert avltree.findNode(2.5).val == 2.5


def test_delete_1():
    avltree = AVLTree([1, 2, 3, 4])
    avltree.delete(2)
    assert avltree.findNode(2) is None


def test_delete_2():
    avltree = AVLTree([1, 2, 3, 4])
    avltree.delete(2)
    assert avltree.root.val == 3


def test_leftRotate():
    avltree = AVLTree([1, 2, 3, 4, 5, 6, 7, 8])
    right = avltree.root.right
    avltree.root = avltree.leftRotate(avltree.root)
    assert avltree.root == right


def test_rightRotate():
    avltree = AVLTree([1, 2, 3, 4, 5, 6, 7, 8])
    left = avltree.root.left
    avltree.root = avltree.rightRotate(avltree.root)
    assert avltree.root == left


def test_height():
    n = 16
    avltree = AVLTree([i for i in range(2 ** n)])
    assert avltree.getHeight(avltree.root) <= n + 1
