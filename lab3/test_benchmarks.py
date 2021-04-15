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
