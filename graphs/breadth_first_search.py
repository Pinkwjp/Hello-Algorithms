"""
explore and return the connected component of G containing s
using breadth first search
"""

from queue import Queue
from typing import Dict, Set

Graph = Dict[int, Set]
Node = int


def breadth_first_search(G: Graph, s: Node) -> Set[Node]:
    component: Set[Node] = set()
    Q: Queue = Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        if u in component:
            continue
        component.add(u)
        for v in G[u]:
            Q.put(v)
    return component


def test():
    G = {  # component 1
        0: {1, 2},
        1: {0, 2},
        2: {0, 1},
        # compnent 2
        3: {4},
        4: {3}}
    c1 = breadth_first_search(G, 1)
    c2 = breadth_first_search(G, 0)
    assert c1 == c2 == {0, 1, 2}


# mypy breadth_first_search.py
if __name__ == '__main__':
    test()
