from queue import Queue
from typing import Dict, Set

Graph = Dict[int, Set]
Node = int


def distance_by_breadth_first_search(G: Graph, s: Node) -> Dict[Node, int]:
    distances: Dict[Node, int] = {s: 0}
    discovered_nodes: Set[Node] = {s}
    Q: Queue = Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if v in discovered_nodes: continue
            discovered_nodes.add(v)
            Q.put(v)
            distances[v] = distances[u] + 1 
    return distances


def test():
    G = {  # component 1
        0: {1, 2},
        1: {0, 2},
        2: {0, 1, 3},
        3: {2},
        # compnent 2
        4: {5},
        5: {4}}
    D = distance_by_breadth_first_search(G, 0)
    assert D == {0: 0, 1: 1, 2: 1, 3: 2}


# mypy breadth_first_search_distance.py
if __name__ == '__main__': 
    test()
