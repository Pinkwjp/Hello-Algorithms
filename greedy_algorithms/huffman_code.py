from heapq import heappush, heappop
from typing import Dict, List, Any


def huffman_binary_tree(alphabets: List[str], frequencies: List[float]) -> List[Any]:
    """return a huffman binary tree (list based)"""
    trees: List[Any] = []
    for i, (frequency, alphabet) in enumerate(zip(frequencies, alphabets)):
        heappush(trees, (frequency, i, [alphabet]))
    while len(trees) > 1:
        u_freqency, _, u_subtree = heappop(trees)
        v_freqency, _, v_subtree = heappop(trees)
        heappush(trees, (u_freqency+v_freqency, i:=i+1, [u_subtree, v_subtree]))
    _, _, tree = trees.pop()
    return tree


def huffman_code(tree: List[Any]) -> Dict[Any, str]:
    """
    return huffman code 
    
    tree: a huffman binary tree
    """
    codes: Dict[Any, str] = {}
    _walk_huffman_tree(tree, codes)
    return codes


def _walk_huffman_tree(tree: List[Any], codes: Dict[Any, str], code: str = '') -> None:
    """walk huffman tree and register huffman code"""
    if len(tree) == 1:
        alphabet = tree[0]
        codes[alphabet] = code
    else:
        _walk_huffman_tree(tree[0], codes, code+'0')
        _walk_huffman_tree(tree[1], codes, code+'1')
