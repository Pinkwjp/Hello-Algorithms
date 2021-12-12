from typing import List
from random import randint

from unittest import TestCase, main

from algorithms_refined.linear.greatest_slice import greatest_slice


def brute_force(numbers: List[int]) -> int:
    return max(sum(numbers[i:j]) 
               for i in range(len(numbers)) 
               for j in range(i+1, len(numbers)+1))


class GreatestSliceTestCase(TestCase):
    def test_edge_cases(self):
        cases = [([0, 0, 0], 0),
                 ([-2, -1, -3], -1),
                 ([1, 1, 1], 3)
                 ]
        for numbers, result in cases:
            with self.subTest(f'numbers: {numbers}, result: {result}'):
                self.assertEqual(brute_force(numbers), result)
                gs_result, _, _ = greatest_slice(numbers)
                self.assertEqual(gs_result, result)
    
    def test_many(self):
        for _ in range(1000):
            numbers = [randint(-200, 200) for _ in range(20)]
            with self.subTest(f'numbers: {numbers}'):
                self.assertEqual(brute_force(numbers), greatest_slice(numbers)[0])


if __name__ == '__main__':
    main()