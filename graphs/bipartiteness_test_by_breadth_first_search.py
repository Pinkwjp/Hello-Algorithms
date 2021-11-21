"""
test if a graph is bipartited using breadth first search

a bipartite graph is one where the node set V can be partitioned 
into sets X and Y in such a way that:

every edge has one end in X and the other end in Y
"""

from queue import Queue 
from typing import Set, Dict, Tuple

Graph = Dict[int, Set]
Node = int


def bipartite_edge(X: Set[Node], Y: Set[Node], edge: Tuple[Node, Node]) -> None:
    """put the end nodes of an edge in two groups"""
    (u, v) = edge
    if u in X:
        Y.add(v)
    else:
        X.add(v)


def bipartite_all_edges(G: Graph) -> Tuple[Set[Node], Set[Node]]:
    """put the end nodes of all edges in a graph in two groups"""
    group_x: Set[Node] = set()
    group_y: Set[Node] = set()
    seen_nodes: Set[Node] = set()
    for s in G:
        if s in seen_nodes: continue
        seen_nodes.add(s)
        Q: Queue = Queue() 
        Q.put(s)
        group_x.add(s)
        while not Q.empty():
            u = Q.get()
            for v in G[u]:
                if v not in seen_nodes:
                    seen_nodes.add(v)
                    Q.put(v)
                bipartite_edge(group_x, group_y, (u, v))
    return group_x, group_y


def is_bipartited(G: Graph) -> bool:
    X, Y = bipartite_all_edges(G)
    for u in G:
        if u in X and u in Y:
            return False
    return True


def test():
    G1 = {# component 1 - odd edges cycle - non-bipartite
          0: {1, 2},
          1: {0, 2},
          2: {0, 1},
          # compnent 2
          3: {4},
          4: {3}}
    assert is_bipartited(G1) == False

    G2 = {# component 1
          0: {1},
          1: {0},
          # compnent 2
          3: {4},
          4: {3}}
    assert is_bipartited(G2) == True

# mypy bipartiteness_test_by_breadth_first_search.py
if __name__ == '__main__':
    test()
