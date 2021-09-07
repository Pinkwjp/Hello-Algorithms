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


def depth_first_search(G: Dag, 
                       ordered: List[Node],
                       finished: Set[Node], 
                       u: Node) -> None:
    """perform a simple depth first search in a DAG"""
    for v in G[u]:
        if v in finished: continue
        depth_first_search(G, ordered, finished, v)
    finished.add(u) 
    # nodes collected in increasing finish time
    ordered.append(u)


def topo_sort_by_depth_first_search(G: Dag) -> List[Node]:
    """return a list of nodes in topological order"""
    topo_order: List[Node] = []
    nodes_finished: Set[Node] = set()
    # can start in any order
    for u in G:
        if u in nodes_finished: continue
        depth_first_search(G, topo_order, nodes_finished, u)
    # reverse to decreasing finish time
    topo_order.reverse()
    return topo_order 


def test():
    dag_1 = {0: {1, 2},
             1: {3},
             2: {1},
             3: set()}
    order_1 = topo_sort_by_depth_first_search(dag_1)
    assert order_1 == [0, 2, 1, 3]

    dag_2 = {0: {1, 2, 3},
             1: {3},
             2: {1},
             3: set()}
    order_2 = topo_sort_by_depth_first_search(dag_2)
    assert order_2 == [0, 2, 1, 3]

    dag_3 = {0: {1, 2, 3},
             1: {2, 4},
             2: set(),
             3: {2, 4},
             4: set()}
    order_3 = topo_sort_by_depth_first_search(dag_3)
    print(order_3)  # [0, 3, 1, 4, 2] is a topological order


# mypy topo_sort_by_depth_first_search.py
if __name__ == "__main__":
    test()
