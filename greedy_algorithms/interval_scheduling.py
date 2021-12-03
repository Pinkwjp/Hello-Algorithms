from typing import List


class Interval:
    """simple interval data class"""
    def __init__(self, start: int, finish: int) -> None:
        assert 0 <= start < finish
        self.start = start
        self.finish = finish


def interval_scheduling(intervals: List[Interval]) -> List[Interval]:
    """return maximum compatible intervals"""
    intervals.sort(key=lambda interval: interval.finish)
    result: List[Interval] = [intervals[0]]
    for interval in intervals[1:]:
        if result[-1].finish < interval.start:
            result.append(interval)
    return result
