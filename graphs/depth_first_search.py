"""
depth first search
"""

from typing import Dict, Set, List

Graph = Dict[int, Set]
Node = int


def depth_first_search_recursive(G: Graph, s: Node) -> Set[Node]:
    connected_compoent: Set[Node] = set()
    depth_first_explore(G, s, connected_compoent)
    return connected_compoent


def depth_first_explore(G: Graph, u: Node, explored_nodes: Set[Node]) -> None:
    explored_nodes.add(u)
    for v in G[u]:
        if v not in explored_nodes:
            depth_first_explore(G, v, explored_nodes)
    

def depth_first_search_iterative(G: Graph, s: Node) -> Set[Node]:
    connected_component: Set[Node] = set()
    stack: List[Node] = [s]
    while stack:
        u = stack.pop()
        if u in connected_component:
            continue
        connected_component.add(u)
        for v in G[u]:
            stack.append(v)
    return connected_component


def test():
    G = {# connected_component 1
         0: {1, 2},
         1: {0, 2},
         2: {0, 1},
         # connected_component 2
         3: {4},
         4: {3}
         }
    c1 = depth_first_search_recursive(G, 1)
    c2 = depth_first_search_recursive(G, 0)
    assert c1 == c2 == {0, 1, 2}


# mypy depth_first_search.py
if __name__ == '__main__':
    test()
