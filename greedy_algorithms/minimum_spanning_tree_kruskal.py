"""
find a minimun (weight) spanning tree of a connected weighted graph
"""

from typing import Dict, List, Tuple

Node = int
Edge = Tuple[Node, Node]
Weight = int
Graph = Dict[Node, Dict[Node, Weight]]

def minimum_spanning_tree_kruskal(G: Graph) -> List[Edge]:
    """
    G: weighted connected graph, 

    assume: G[u][v] == G[v][u] (non-directed)
    """
    minimum_spanning_tree_edges: List[Edge] = []
    parents = {u: u for u in G}
    subtree_sizes = {u: 1 for u in G}
    sorted_edges = sorted([(u, v) for u in G for v in G[u]], 
                          key=lambda edge: G[edge[0]][edge[1]])
    for (u, v) in sorted_edges:
        root_u = get_root(parents, u)
        root_v = get_root(parents, v)
        if root_u is root_v:
            continue
        merge_roots(parents, subtree_sizes, root_u, root_v) 
        minimum_spanning_tree_edges.append((u, v)) 
    return minimum_spanning_tree_edges
    

def get_root(parents: Dict[Node, Node], u: Node) -> Node:
    """
    return the root node of the subtree containing u

    parents: parent nodes of all nodes

    assume: root node's parent is itself
    """
    assert u in parents
    if (v := parents[u]) is u:
        return u 
    parents[u] = get_root(parents, v) # path compression
    return parents[u]


def merge_roots(parents: Dict[Node, Node], sizes: Dict[Node, int], 
                u: Node, v: Node) -> None:
    """
    merge smaller tree to bigger tree
    
    parents: parent nodes of all nodes
    sizes: sizes of all subtress
    u: the root node of a subtree
    v: the root node of another subtree
    """
    assert ((u in parents) 
             and (v in parents) 
             and (u in sizes) 
             and (v in sizes))
    bigger = u if sizes[u] >= sizes[v] else v
    smaller = v if bigger is u else u 
    sizes[bigger] += sizes[smaller]
    parents[smaller] = bigger
    del sizes[smaller]
    

def sum_edge_weight(G: Graph, edges: List[Edge]) -> int:
    """
    return the total weight of edges

    note: for testing
    """
    return sum([G[u][v] for (u, v) in edges])
