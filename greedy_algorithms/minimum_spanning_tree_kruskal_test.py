from unittest import TestCase, main

from algorithms_refined.greedy_algorithms.minimum_spanning_tree_kruskal import (get_root, merge_roots,
    minimum_spanning_tree_kruskal, sum_edge_weight)


class MinimumSpanningTreeKruskalTestCase(TestCase):
    def test(self):
        G = {0: {1: 30, 2: 20}, 
             1: {0: 30, 2: 10},
             2: {0: 20, 1: 10}}
        min_tree_edges = minimum_spanning_tree_kruskal(G)
        self.assertEqual(sum_edge_weight(G=G, edges=min_tree_edges), 10+20)
    
    def test_more(self):
        G = {0: {1: 30, 2: 20}, 
             1: {0: 30, 2: 10},
             2: {0: 20, 1: 10},
             3: {1: 5,  2: 50}}
        min_tree_edges = minimum_spanning_tree_kruskal(G)
        self.assertEqual(sum_edge_weight(G=G, edges=min_tree_edges), 10+20+5)


class SumEdgeWeightTestCase(TestCase):
    def test(self):
        G = {0: {1: 30, 2: 20}, 
             1: {0: 30, 2: 10},
             2: {0: 20, 1: 10}}
        cases = [([(0, 1), (1, 2)], 30+10), 
                 ([(0, 2), (2, 0)], 20+20),
                 ([(0, 1), (1, 2), (2, 0)], 30+10+20)] 
        for (edges, weight) in cases:
            with self.subTest():
                self.assertEqual(sum_edge_weight(G=G, edges=edges), weight)


class GetRootTestCase(TestCase):
    def test(self):
        cases = [({1:2, 2:3, 3:4, 4:4}, 4), 
                 ({1:1}, 1)]
        for (parents, root) in cases:
            with self.subTest():
                self.assertEqual(get_root(parents=parents, u=1), root)


class MergeRootsTestCase(TestCase):
    def test_same_size(self):
        u = 1
        v = 2
        parents = {u: u, v: v}
        sizes = {u: 1, v: 1}
        merge_roots(parents=parents, sizes=sizes, u=u, v=v)
        self.assertEqual(parents[v], u)
        self.assertNotIn(v, sizes)
        self.assertEqual(sizes[u], 2)
    
    def test_different_size(self):
        u = 1
        v = 2
        parents = {u: u, v: v}
        sizes = {u: 1, v: 4}
        merge_roots(parents=parents, sizes=sizes, u=u, v=v)
        self.assertEqual(parents[u], v)
        self.assertNotIn(u, sizes)
        self.assertEqual(sizes[v], 5)


if __name__ == '__main__':
    main()