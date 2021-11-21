"""
Topologically sort a Directed Acyclic Graph (DAG) by 
performing depth first search.

A node is finished after all its descendent nodes are finished,
by collecting the nodes when they are finished, we have the 
topological order.
"""

from typing import Dict, List, Set

Node = int
Dag = Dict[Node, Set[Node]]

# topo sort by dfs
def depth_first_search(G: Dag, 
                       total_order: List[Node],
                       discovered_nodes: Set[Node], 
                       u: Node) -> None:
    for v in G[u]:
        if v in discovered_nodes: continue
        depth_first_search(G, total_order, discovered_nodes, v)
    total_order.append(u)
    discovered_nodes.add(u) 


def topo_sort_by_depth_first_search(G: Dag) -> List[Node]:
    """return a list of nodes in topological order"""
    topo_order: List[Node] = []
    nodes_finished: Set[Node] = set()
    for u in G:
        if u in nodes_finished: continue
        depth_first_search(G, topo_order, nodes_finished, u)
    topo_order.reverse() # reverse to decreasing finish time
    return topo_order 


# topo sort by edge count
def count_incoming_edges_number(G: Dag) -> Dict[Node, int]:
    incoming_edge_counts = {u: 0 for u in G}
    for u in G:
        for v in G[u]:
            incoming_edge_counts[v] += 1
    return incoming_edge_counts


def topo_sort_by_counting_incoming_edges(G: Dag) -> List[Node]:
    """return a list of nodes in a topological order"""
    topo_order: List[Node] = []
    incoming_edge_counts: Dict[Node, int] = count_incoming_edges_number(G)
    nodes_without_incoming_edge: List[Node] = []
    for u in incoming_edge_counts:
        if incoming_edge_counts[u] == 0:
            nodes_without_incoming_edge.append(u)
    while nodes_without_incoming_edge:
        u = nodes_without_incoming_edge.pop()
        topo_order.append(u)
        for v in G[u]:
            incoming_edge_counts[v] -= 1
            if not incoming_edge_counts[v]:
                nodes_without_incoming_edge.append(v)
    return topo_order 


# for testing
def is_topological_order(nodes: List[Node], G: Dag) -> bool:
    all_nodes = set(G.keys())
    if not all_nodes == set(nodes):
        return False
    for i, node in enumerate(nodes):
        for node_finished_earlier in nodes[i+1:]:
            if node in G[node_finished_earlier]:
                return False
    return True 


def test_is_topological_order():
    dag_1 = {0: {1, 2},
             1: {3},
             2: {1},
             3: set()}
    assert is_topological_order([0, 2, 1, 3], dag_1)

    dag_2 = {0: {1, 2, 3},
             1: {3},
             2: {1},
             3: set()}
    assert is_topological_order([0, 2, 1, 3], dag_2)

    dag_3 = {0: {1, 2, 3},
             1: {2, 4},
             2: set(),
             3: {2, 4},
             4: set()}
    assert is_topological_order([0, 3, 1, 4, 2], dag_3)


def test():
    dag_1 = {0: {1, 2},    # topo order: [0, 2, 1, 3]
             1: {3},
             2: {1},
             3: set()}
    dag_2 = {0: {1, 2, 3}, # topo order: [0, 2, 1, 3]
             1: {3},
             2: {1},
             3: set()}
    dag_3 = {0: {1, 2, 3}, # topo order: [0, 3, 1, 4, 2]
             1: {2, 4},
             2: set(),
             3: {2, 4},
             4: set()}
    for dag in (dag_1, dag_2, dag_3):
        order_nodes = topo_sort_by_depth_first_search(dag)
        order_nodes1 = topo_sort_by_counting_incoming_edges(dag)
        assert is_topological_order(order_nodes, dag)
        assert is_topological_order(order_nodes1, dag)


# mypy topological_sort_by_depth_first_search.py
if __name__ == "__main__":
    #test_is_topological_order()
    test()
