from Trees import AVLTree, BST
import pytest
import random
import sys
import copy

sys.setrecursionlimit(10000)

NUMBERS = random.sample(range(1, 30001), 10000)
SIZES = [1000, 2000, 4000, 6000, 8000, 10000]
NUMBERS_TO_DELETE = random.sample(range(1, 30001), 10000)

FILLED_TREES = []
AVL_FILLED = AVLTree(NUMBERS)
BST_FILLED = BST()
BST_FILLED.insert_list(NUMBERS)
FILLED_TREES = [BST_FILLED, AVL_FILLED]


def test_init_AVL_with_numbers():
    avltree = AVLTree([10, 20, 30])
    assert avltree.root.val == 20


def test_init_AVL_empty():
    avltree = AVLTree()
    assert avltree.root is None


def test_init_bst_empy():
    bsttree = BST()
    assert bsttree.root is None


def test_insert_AVL():
    avltree = AVLTree()
    avltree.insert(5)
    assert avltree.root.val == 5


def test_insert_list_AVL():
    avltree = AVLTree()
    avltree.insert_list([10, 20, 30])
    """
            -> 30
    -> 20
            -> 10
    """
    assert avltree.root.val == 20
    assert avltree.root.left.val == 10
    assert avltree.root.right.val == 30


def test_insert_BST():
    bsttree = BST()
    bsttree.insert(5)
    assert bsttree.root.val == 5


def test_insert_list_BST():
    bsttree = BST()
    bsttree.insert_list([10, 20, 30])
    """
                    -> 30
            -> 20
    -> 10
            ->
    """
    assert bsttree.root.val == 10
    assert bsttree.root.right.val == 20
    assert bsttree.root.right.right.val == 30


def test_search_AVL():
    avltree = AVLTree()
    avltree.insert_list([10, 20, 30])
    """
            -> 30
    -> 20
            -> 10
    """
    assert avltree.search(20).val == 20
    assert avltree.search(20).left.val == 10
    assert avltree.search(20).right.val == 30


def test_search_BST():
    bsttree = BST()
    bsttree.insert_list([10, 20, 30])
    """
                    -> 30
            -> 20
    -> 10
            ->
    """
    assert bsttree.search(10).val == 10
    assert bsttree.search(10).right.val == 20
    assert bsttree.search(10).right.right.val == 30


@pytest.mark.parametrize("tree", [AVLTree, BST])
def test_search_list(tree):
    obj = tree()
    _list = [10, 20, 30]
    obj.insert_list(_list)
    for element, expected in zip(obj.search_list([10, 20, 30]), _list):
        assert element.val == expected


def test_delete_AVL():
    avltree = AVLTree()
    avltree.insert_list([10, 20, 30, 50])
    """
                    -> 50
            -> 30
    -> 20
            -> 10
    """
    avltree.delete(20)
    """
            -> 50
    -> 30
            -> 10
    """
    assert avltree.root.val == 30
    assert avltree.root.right.val == 50
    assert avltree.root.left.val == 10


def test_delete_list_AVL():
    avltree = AVLTree()
    avltree.insert_list([10, 20, 30, 50, 17, 9])
    """
                    -> 50
            -> 30
    -> 20
                    -> 17
            -> 10
                    -> 9
    """
    avltree.delete_list([20, 10])
    """
            -> 50
    -> 30
            -> 17
                    -> 9
    """
    assert avltree.root.val == 30
    assert avltree.root.right.val == 50
    assert avltree.root.left.val == 17
    assert avltree.root.left.left.val == 9


def test_delete_BST():
    bsttree = BST()
    bsttree.insert_list([20, 10, 30, 50])
    """
                    -> 50
            -> 30
    -> 20
            -> 10
    """
    bsttree.delete(20)
    """
            -> 50
    -> 30
            -> 10
    """
    assert bsttree.root.val == 30
    assert bsttree.root.right.val == 50
    assert bsttree.root.left.val == 10


def test_delete_list_BST():
    bsttree = BST()
    bsttree.insert_list([10, 20, 30, 50, 17, 9])
    """
                            -> 50
                    -> 30
            -> 20
                    -> 17
    -> 10
            -> 9
    """
    bsttree.delete_list([10, 30])
    """
                    -> 50
            -> 20
    -> 17
            -> 9
    """
    assert bsttree.root.val == 17
    assert bsttree.root.left.val == 9
    assert bsttree.root.right.val == 20
    assert bsttree.root.right.right.val == 50


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


@pytest.mark.parametrize('size', SIZES)
def test_insertTimeAVL(size, benchmark):
    benchmark.extra_info["function"] = "insertTime"
    benchmark.extra_info["tree"] = "AVL"
    benchmark.extra_info["size"] = size
    benchmark(AVLTree, NUMBERS[:size])


@pytest.mark.parametrize('size', SIZES)
def test_insertTimeBST(size, benchmark):
    benchmark.extra_info["function"] = "insertTime"
    benchmark.extra_info["tree"] = "BST"
    benchmark.extra_info["size"] = size
    bst = BST()
    benchmark(bst.insert_list, NUMBERS[:size])


@pytest.mark.parametrize("tree", FILLED_TREES)
@pytest.mark.parametrize("size", SIZES)
def test_searchTime(tree, size, benchmark):
    benchmark.extra_info["function"] = "searchTime"
    if str(tree.__class__) == "<class 'Trees.BST'>":
        benchmark.extra_info["tree"] = 'BST'
    else:
        benchmark.extra_info["tree"] = 'AVL'
    benchmark.extra_info["size"] = size
    benchmark(tree.search_list, NUMBERS[:size])


@pytest.mark.parametrize("tree", FILLED_TREES)
@pytest.mark.parametrize("size", SIZES)
def test_deleteTime(tree, size, benchmark):
    benchmark.extra_info["function"] = "deleteTime"
    if str(tree.__class__) == "<class 'Trees.BST'>":
        benchmark.extra_info["tree"] = 'BST'
    else:
        benchmark.extra_info["tree"] = 'AVL'
    benchmark.extra_info["size"] = size
    new_tree = copy.deepcopy(tree)
    benchmark(new_tree.delete_list, NUMBERS_TO_DELETE[:size])
