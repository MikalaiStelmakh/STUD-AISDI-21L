from Trees import AVLTree, BST
import pytest
import random
import sys
import copy

sys.setrecursionlimit(10000)

NUMBERS = random.sample(range(1, 30001), 10000)
SIZES = [1000, 2000, 4000, 6000, 8000, 10000]

FILLED_TREES = []
AVL_FILLED = AVLTree(NUMBERS)
BST_FILLED = BST()
BST_FILLED.insert_list(NUMBERS)
FILLED_TREES = [BST_FILLED, AVL_FILLED]


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
    assert avltree.search(5).val == 5


def test_insert_find_2():
    avltree = AVLTree([1, 2, 3, 4])
    avltree.insert(2.5)
    assert avltree.search(2.5).val == 2.5


def test_delete_1():
    avltree = AVLTree([1, 2, 3, 4])
    avltree.delete(2)
    assert avltree.search(2) is None


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
    benchmark(new_tree.delete_list, NUMBERS[:size])