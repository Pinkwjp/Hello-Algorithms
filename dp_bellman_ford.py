from typing import Dict, Tuple, TypeVar, List
from copy import deepcopy

Node = int  # node represent by 0, 1, ...
Dvalue = TypeVar('Dvalue', int, float)  # distance value can be int or float
Graph = Dict[Node, Dict[Node, Dvalue]]
Distance = Dict[Node, Dvalue]  # distance from source to node
INFINITY = float('inf')

def init_distance(G: Graph, s: Node) -> Distance:
    """initial distances from source s to all other is infinity"""
    D: Distance = {}
    for u in G:
        # initial distance from source to u is infinity
        D[u] = INFINITY
    D[s] = 0  # except source
    return D

def explicit_two_way_graph(G: Graph) -> Graph:
    """return a explicit two way graph
    (if u -> v and not v -> u, then G[v][u] = inf)
    G - a directed weighted graph
    """
    H = deepcopy(G)
    for u in G:
        for neighbour in G[u]:
            if u is neighbour:  # same node, ignore
                continue
            if u not in G[neighbour]:
                H[neighbour][u] = INFINITY
    return H

def dynamic_programming_bellman_ford(G: Graph, s: Node) -> Distance:
    """ return the shortest distance from s to all nodes
    assuming no negative cycle
    G - directed weighted graph
    """
    # if u -> v and not v -> u, then H[v][u] = inf
    H = explicit_two_way_graph(G)
    # distance from s to all nodes, D[s] = 0, D[u] = inf
    D = init_distance(H, s)
    # number of nodes
    n = len(H)
    # for each path from s to u, there is at most n-1 edges without negative cycle
    for i in range(n-1):
        for u in H:
            D[u] = min(D[u], min(D[v]+H[v][u] for v in H[u]))
    return D

def dp_bellman_ford_with_negative_cycle_detection(G: Graph, s: Node) -> Distance:
    """ return the shortest distance from s to all nodes
    assuming no negative cycle
    G - directed weighted graph
    """
    # if u -> v and not v -> u, then H[v][u] = inf
    H = explicit_two_way_graph(G)
    # distance from s to all nodes, D[s] = 0, D[u] = inf
    D = init_distance(H, s)
    # number of nodes
    n = len(H)
    # for each path from s to u, there is at most n-1 edges without negative cycle
    for i in range(n):
        improve = False
        # for every nodes in the graph
        for u in H:
            # estimate the shortest path to u through its neighbours
            new_estimate = min(D[v]+H[v][u] for v in H[u])
            # a shorter path?
            if new_estimate < D[u]:
                # update
                D[u] = new_estimate
                improve = True
        # if no nodes has a improved distance
        if not improve:
            break
    else:
        raise(ValueError('nagetive cycle detected!'))
    return D

def build_all_path(G: Graph, s: Node, D: Distance) -> List[list]:
    """ build all paths from s to all other nodes
    a path from s to u - a list as [s, ..., u]
    D - a dict of shortest distance from s to all nodes
    return a list of all paths
    """
    H = explicit_two_way_graph(G)
    all_paths = []
    for u in H: # for every nodes in the graph
        if D[u] is INFINITY: # no path from s to u
            continue  # skip
        path = [u]  # backward, u to s, [u, ..., s] 
        while u is not s:  # trace backward until reach s
            for v in H[u]:  # check all u's neighbours
                if v is u:  # u is in u's neighbours as well
                    continue # skip u itself
                if D[v] + H[v][u] == D[u]:  # v is on the shortest path from s to u
                    path.append(v)
                    u = v # one step closer
                    break # now to search from v
        path.reverse() # forward, s to u, [s, ..., u] 
        print(path)
        all_paths.append(path) # collect 
    return all_paths
    

# here every node u can reach itself
G = {0: {0: 0, 1: 10, 2: 20}, 1: {1: 0}, 2: {2: 0}}
C = {0: {0: 0, 1: 10, 2: 20}, 1: {1: 0, 0: INFINITY}, 2: {2: 0, 0: INFINITY}}
assert explicit_two_way_graph(G) == C

G2 = {0: {0: 0, 1: 20, 2: 10}, 1: {0: -50, 1: 0},
      2: {2: 0, 1: -20}}  # with negative cycle
assert dynamic_programming_bellman_ford(G2, 0) == {0: -30, 1: -10, 2: -20} # fail to detect the negative cycle
# dp_bellman_ford_with_negative_cycle_detection(G2, 0)             ValueError: nagetive cycle detected!

G3 = {0: {0: 0, 1: 20, 2: 10}, 1: {1: 0}, 2: {2: 0, 1: -20}}
assert dynamic_programming_bellman_ford(G3, 0) == {0: 0, 1: -10, 2: 10}

assert dp_bellman_ford_with_negative_cycle_detection(G3, 0) == {
    0: 0, 1: -10, 2: 10}

D3 = dp_bellman_ford_with_negative_cycle_detection(G3, 0)
assert build_all_path(G3, 0, D3) == [[0], [0, 2, 1], [0, 2]]

# mypy dp_bellman_ford.py
