"""
Topologically sort a Directed Acyclic Graph (DAG) by 
counting incoming edges of each nodes.

Every DAG, G, there is exactly 1 node, u, with no incoming edge,
find u, (pretent to) remove all the outgoing edge from u, resulting a
new DAG G' (with updated incoming edge count for each node), 
repeat recursively until all nodes are removed from the DAG. 

Note:
The following implement does not acutally remove nodes,
it simply keep updating the incoming edge count of all nodes.
"""

from typing import Dict, List, Set

Node = int 
Dag = Dict[Node, Set[Node]]


def topo_sort_by_edge_count(G: Dag) -> List[Node]:
    """return a list of nodes in topological order"""
    topo_order: List[Node] = []
    # scan and count
    incoming_edge_counts = {u: 0 for u in G}
    for u in G:
        for v in G[u]:
            incoming_edge_counts[v] += 1
    nodes_without_in_edge: List[Node] = []
    # the starting node
    for u in incoming_edge_counts:
        if not incoming_edge_counts[u]:
            nodes_without_in_edge.append(u)
    # remove, update, repeat
    while nodes_without_in_edge:
        u = nodes_without_in_edge.pop()
        topo_order.append(u)
        for v in G[u]:
            incoming_edge_counts[v] -= 1
            if not incoming_edge_counts[v]:
                nodes_without_in_edge.append(v)
    return topo_order 


def test():
    dag_1 = {0: {1, 2},
             1: {3},
             2: {1},
             3: set()}
    order_1 = topo_sort_by_edge_count(dag_1)
    assert order_1 == [0, 2, 1, 3]

    dag_2 = {0: {1, 2, 3},
             1: {3},
             2: {1},
             3: set()}
    order_2 = topo_sort_by_edge_count(dag_2)
    assert order_2 == [0, 2, 1, 3]


# mypy topo_sort_by_edge_count.py 
if __name__ == "__main__":
    test()
