"""
using dfs to find out the distance (number of edges) from source s 
to all reachable nodes (nodes in the same component)
"""

from queue import Queue
from typing import Dict, Set

Graph = Dict[int, Set]
Node = int


def breadth_first_search_distance(G: Graph, s: Node) -> Dict[Node, int]:
    distance: Dict[Node, int] = {s: 0}
    discovered: Set[Node] = {s}
    Q: Queue = Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if v in discovered: continue
            discovered.add(v)
            Q.put(v)
            distance[v] = distance[u] + 1 
    return distance


def test():
    G = {  # component 1
        0: {1, 2},
        1: {0, 2},
        2: {0, 1, 3},
        3: {2},
        # compnent 2
        4: {5},
        5: {4}}
    D = breadth_first_search_distance(G, 0)
    print(D)


# mypy breadth_first_search_distance.py
if __name__ == '__main__': 
    test()
