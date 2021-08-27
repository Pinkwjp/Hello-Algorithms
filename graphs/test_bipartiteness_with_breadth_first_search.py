"""
test to see if a graph is bipartite using breadth first search

a bipartite graph is one where the node set V can be partitioned 
into sets X and Y in such a way that every edge has one end
in X and the other end in Y.

by coloring the nodes with two colors, using breadth first search,
if any node ends with two colors, then the graph is not bipartite.

the graph can be either connected or non-connected.
"""

from queue import Queue 
from typing import Set, Dict

Graph = Dict[int, Set]
Node = int

def test_bipartiteness(G: Graph) -> bool:
    Red: Set[Node] = set()
    Blue: Set[Node] = set()
    seen: Set[Node] = set()
    # try breadth-first-search from every node
    for s in G:
        if s in seen: continue
        seen.add(s)
        Q: Queue = Queue() # FIFO
        # initialize
        Q.put(s)
        Red.add(s)
        while not Q.empty():
            u = Q.get()
            for v in G[u]:
                # breadth first search
                if v not in seen:
                    seen.add(v)
                    Q.put(v)
                # coloring
                if u in Red:
                    Blue.add(v)
                else:
                    Red.add(v)    
    # scan nodes color
    for u in G:
        if u in Red and u in Blue:
            return False
    return True


def test():
    G = {  # component 1 - odd edges cycle - non-bipartite
        0: {1, 2},
        1: {0, 2},
        2: {0, 1},
        # compnent 2
        3: {4},
        4: {3}}
    assert test_bipartiteness(G) == False

    G1 = {  # component 1
        0: {1},
        1: {0},
        # compnent 2
        3: {4},
        4: {3}}
    assert test_bipartiteness(G1) == True

# mypy test_bipartiteness_with_breadth_first_search.py
if __name__ == '__main__':
    test()
