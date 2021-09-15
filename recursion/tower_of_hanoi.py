"""
In the Tower of Hanoi puzzle, we are given a platform with three rod, a,
b, and c. On peg a is a stack of n disks, each larger than
the next, so that the smallest is on the top and the largest is on the bottom.

The puzzle is to move all the disks from peg a to peg c, moving one disk
at a time, so that we never place a larger disk on top of a smaller one.
"""

from typing import List

Disc = int
Rod = List


def move_top_discs(a: Rod, b: Rod, c: Rod, n: int):
    """move the top n discs from a to c through b"""
    # check if disc are placed properly
    for rod in [a, b, c]:
        if rod:
            assert rod == sorted(rod)
    # base case
    if n == 1:
       c.append(a.pop())
    else:
        # first move the top (n-1) discs from a to b through c
        move_top_discs(a, c, b, n-1)
        # then move the nth disc from a to c
        move_top_discs(a, b, c, 1)
        # then move the top (n-1) discs from b to c through a
        move_top_discs(b, a, c, n-1)


def tower_of_hanoi(num_disc: int = 4) -> None:
    """perform the game tower of hanoi

    rods are represented as list, []
    disc are represented as int, from 1, 2, ... 

    rule: 
    in any rod, all disc are placed from small to large, 
    with the largest in the bottom, the smallest on the top.

    so, a rod with proper disc placement is represented as a sorted list.
    """
    A: Rod = list(range(1, num_disc+1))
    B: Rod = []
    C: Rod = []
    print(f'before: A: {A}, B: {B}, C: {C}')
    move_top_discs(A, B, C, num_disc)
    print(f'after : A: {A}, B: {B}, C: {C}') 


def test():
    n = 8
    tower_of_hanoi(n)


# mypy tower_of_hanoi.py
if __name__ == "__main__": test()
