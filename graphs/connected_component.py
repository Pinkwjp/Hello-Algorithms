"""explore and return the connected component of G containing s"""

from typing import Dict, List, Set

Graph = Dict[int, Set] 
Node = int
Component = Set[Node]


def connected_component(G: Graph, s: Node) -> Component:
    """return the connected component of G containing s"""
    C: Component = set()
    to_explore: Set[Node] = {s}
    while to_explore:
        # explore the nodes in a somewhat random order
        u = to_explore.pop()
        C.add(u)
        for v in G[u]:
            if v not in C:
                to_explore.add(v)
    return C


def all_connected_component(G: Graph) -> List[Component]:
    all_comps: List[Component] = []
    seen: Set[Node] = set()
    for u in G:
        if u in seen: continue
        comp = connected_component(G, u)
        all_comps.append(comp)
        seen.update(comp)
    return all_comps 


def test():
    G = {# component 1
         0: {1, 2}, 
         1: {0, 2},
         2: {0, 1},
         # compnent 2
         3: {4},
         4: {3}}
    component = connected_component(G, 1)
    assert component == {0, 1, 2}
    comps = all_connected_component(G)
    print(f'all components: {comps}')


# mypy connected_component.py
if __name__ == '__main__':
    test()
    


