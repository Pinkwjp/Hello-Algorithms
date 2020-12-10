from typing import Dict, Tuple, TypeVar


Node = int  # node represent by 0, 1, ...
Dvalue = TypeVar('Dvalue', int, float)  # distance value can be int or float
Graph = Dict[Node, Dict[Node, Dvalue]]
Distance = Dict[Node, Dvalue]  # distance from source to node
Predecessor = Dict[Node, Node] # predecessor node of another node 

def init_distance(G: Graph, s: Node) -> Distance:
    """initial distances from source s to all other is infinity"""
    D: Distance = {}
    for u in G:
        # initial distance from source to u is infinity
        D[u] = float('inf')
    D[s] = 0  # except source
    return D

def init_predecessor(G: Graph, s: Node) -> Predecessor:
    """initial predecessors of all nodes is itself"""
    P: Predecessor = {}
    for u in G:
        # initial predecessor of u is u itself
        P[u] = u
    return P

def relax(from_u: Node, to_v: Node, G: Graph, D: Distance, P: Predecessor) -> bool:
    """ try to relax(reduce) distance from source to v through u """
    u, v = from_u, to_v
    # estimate distance from source through u to v
    estimate = D[u] + G[u][v] 
    if estimate < D[v]:
        # update distance
        D[v] = estimate 
        # update predecessor of v
        P[v] = u        
        return True
    return False

def bellman_ford_neg_detection_by_iteration_count(G: Graph, s: Node) -> Tuple[Distance, Predecessor]:
    """ 
    find out shortest distance from source s to all other nodes 
    with negative cycle detection by iteration number at most n-1
    """
    D = init_distance(G, s)  # initial distance
    P = init_predecessor(G, s)  # initial predecessor
    for _ in G:  # run n iterations of relaxation
        fringe = [s]  # nodes on the fringe to check, starting with s
        seen = set()  # nodes seen in current iteration of relaxation
        improve = False  # marker
        # start of current iteration
        while fringe:  # some node to check?
            u = fringe.pop()  # pick one, order doesn't matter
            # each node will be relaxed at most once per iteration
            if u in seen:  # node seen?
                continue  # ignore, back to fringe
            seen.add(u)  # not seen yet, mark as seen
            for v in G[u]:  # check all neighbours of u
                if relax(u, v, G, D, P):  # distance from s to v improved through u?
                    fringe.append(v)  # add to fringe
                    improve = True  # mark successful relaxation
        # end of current iteration
        if not improve:  # no relaxation, done
            break
    else:  # run n iterations and there are at most n-1 leagle iterations
        # so the graph has negative cycle
        raise ValueError('negative cycle detected.')
    return D, P

def bellman_ford_neg_detection_by_edge_count(G: Graph, s: Node) -> Tuple[Distance, Predecessor]:
    """
    find out shortest distance from source s to all other nodes
    with negative cycle detection by counting path edge count, 
    any path with n nodes has at most n-1 edge  
    """ 
    D = init_distance(G, s)  # distance
    P = init_predecessor(G, s)  # predecessor 
    edge_count = {u: 0 for u in G}  # edge count of the path from s to u
    fringe = [s]
    tatal_node_num = len(G)
    while fringe:
        u = fringe.pop()
        if edge_count[u] >= tatal_node_num:
            raise ValueError('negative cycle detected')
        for v in G[u]:  # check all neighbours of u
            if relax(u, v, G, D, P):  # distance from s to v improved through u?
                fringe.append(v)  # add to fringe
                edge_count[v] = edge_count[u] + 1  # update edge count
    return D, P


G = {0: {0: 0, 1: 10, 2: 20}, 1: {1: 0}, 2: {2: 0}}
inf = float('inf')
assert init_distance(G, 0) == {0: 0, 1: inf, 2: inf}
assert init_predecessor(G, 0) == {0: 0, 1: 1, 2: 2}
G1 = {0: {0: 0, 1: 20, 2: 10}, 1: {1: 0}, 2: {2: 0, 1: 5}}
D1 = {0: 0, 1: 20, 2: 10}
P1 = {0: 0, 1: 0, 2: 0}
assert relax(2, 1, G1, D1, P1) == True
DD, PP = bellman_ford_neg_detection_by_iteration_count(G1, 0)
assert DD == {0: 0, 1: 15, 2: 10}

G2 = {0: {0: 0, 1: 20, 2: 10}, 1: {0: 5, 1: 0}, 2: {2: 0, 1: -20}} # with negative cycle
G3 = {0: {0: 0, 1: 20, 2: 10}, 1: {1: 0}, 2: {2: 0, 1: -20}}
D3, P3 = bellman_ford_neg_detection_by_edge_count(G3, 0)
assert D3 == {0: 0, 1: -10, 2: 10}
# mypy b_graph_bellman_ford.py

