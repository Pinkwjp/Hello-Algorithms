"""
In the Tower of Hanoi puzzle, we are given a platform with three rod, A,
B, and C. On peg A is a stack of n disks, each larger than
the next, so that the smallest is on the top and the largest is on the bottom.

The puzzle is to move all the disks from peg A to peg C, moving one disk
at a time, so that we never place a larger disk on top of a smaller one.
"""

from functools import total_ordering
from typing import List, Optional


@total_ordering
class Disk:
    def __init__(self, size: int) -> None:
        self.size = size
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.size}'
    
    def _is_valid_operand(self, other) -> bool:
        return isinstance(other, Disk)
    
    def __eq__(self, other) -> bool:
        if not self._is_valid_operand(other):
            raise ValueError(f'{other} is not a disk.')
        return (self.size == other.size)
        
    def __lt__(self, other) -> bool:
        if not self._is_valid_operand(other):
            raise ValueError(f'{other} is not a disk.')
        return (self.size < other.size)
        

class Rod:
    def __init__(self) -> None:
        self.stack: List[Disk] = [] 
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.stack}'
    
    def get_disk_number(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        if self.stack:
            return False
        return True
    
    def _get_top_disk(self) -> Optional[Disk]:
        result = None
        if not self.is_empty():
            result = self.stack[-1] 
        return result 

    def add_disk(self, disk: Disk) -> None:
        top_disk = self._get_top_disk()
        if top_disk and top_disk < disk:
            raise ValueError(f'{disk} is too big.')    
        self.stack.append(disk)

    def pop_top_disk(self) -> Disk:
        """remove and return top disk or None"""
        if self.is_empty():
            raise ValueError('no disk to pop out')
        return self.stack.pop() 


def move_disks(n: int, A: Rod, B: Rod, C: Rod) -> None:
    """move (top) n disks from A to C through B"""
    if n == 1:
        C.add_disk(A.pop_top_disk())   
    else:
        move_disks(n-1, A, C, B)
        move_disks(1, A, B, C)
        move_disks(n-1, B, A, C)


def tower_of_hanoi(num_disc: int = 4) -> None:
    A, B, C = (Rod() for _ in range(3))
    all_disks = [Disk(i) for i in range(1, 1+num_disc)]
    while all_disks:
        A.add_disk(all_disks.pop())
    print()
    print(f'A: {A}, B: {B}, C: {C}')

    move_disks(num_disc, A, B, C)
    print()
    print(f'A: {A}, B: {B}, C: {C}')
