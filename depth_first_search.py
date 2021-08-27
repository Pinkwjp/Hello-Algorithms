"""
explore and return the connected component of G containing s
using depth first search

note: 
the recursive and iterative version perform dfs in a 
different order from the child nodes
"""

from typing import Dict, Set, List

Graph = Dict[int, Set]
Node = int


def depth_first_search_recursive(G: Graph, s: Node) -> Set[Node]:
    component: Set[Node] = set()
    def recur(u: Node) -> None:
        component.add(u)
        for v in G[u]:
            if v not in component:
                recur(v)
    recur(s)
    return component


def depth_first_search_iterative(G: Graph, s: Node) -> Set[Node]:
    component: Set[Node] = set()
    stack: List[Node] = [s]
    while stack:
        # a node may be added to stack multiple times
        # only the latest added one will be used for searching
        u = stack.pop()
        if u in component:
            continue
        component.add(u)
        for v in G[u]:
            stack.append(v)
    return component


def test():
    G = {  # component 1
        0: {1, 2},
        1: {0, 2},
        2: {0, 1},
        # compnent 2
        3: {4},
        4: {3}}
    c1 = depth_first_search_recursive(G, 1)
    c2 = depth_first_search_recursive(G, 0)
    assert c1 == c2 == {0, 1, 2}


# mypy depth_first_search.py
if __name__ == '__main__':
    test()
