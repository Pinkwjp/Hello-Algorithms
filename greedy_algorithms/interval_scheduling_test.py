from unittest import TestCase, main

from algorithms_refined.greedy_algorithms.interval_scheduling import (Interval,
    interval_scheduling)


class IntervalSchedulingTestCase(TestCase):
    def setUp(self) -> None:
        #             (intervals, max compatible number)
        self.cases = [([(1, 2), (3, 4), (5, 6)], 3),
                      ([(1, 9), (3, 4), (5, 6)], 2),
                      ([(1, 9), (1, 4), (1, 5)], 1)]

    def test(self):
        for case in self.cases:
            with self.subTest():
                intervals = [Interval(*pair) for pair in case[0]]
                compatibles = interval_scheduling(intervals)
                self.assertEqual(len(compatibles), case[1])


if __name__ == "__main__": 
    main()
