"""
The eight queens puzzle is the problem of placing eight chess queens 
on an 8×8 chessboard so that no two queens threaten each other; 
thus, a solution requires that no two queens share the same row, 
column, or diagonal. The eight queens puzzle is an example of the 
more general n queens problem of placing n non-attacking queens on 
an n×n chessboard, for which solutions exist for all natural numbers 
n with the exception of n = 2 and n = 3.

(an 8×8 board, 92 solutions)

https://en.wikipedia.org/wiki/Eight_queens_puzzle
"""

from typing import Generator, List, Optional, Set, Tuple


class Chessboard:
    queen = 1
    def __init__(self, queen_coordinates: Optional[List[Tuple[int, int]]] = None) -> None:
        self.size = 8
        self.board = [[0 for _ in range(self.size)] 
                      for _ in range(self.size)]
        if queen_coordinates:
            for (i, j) in queen_coordinates:
                self._set_chess(row=i, column=j, chess=self.queen)
    
    def __repr__(self) -> str:
        name = 'Chessboard: '
        first_line = '  ' + '  '.join([str(i) for i in range(self.size)])
        other_lines = [str(i) + str(row) for (i, row) in enumerate(self.board)]
        return '\n'.join( [name, first_line] + other_lines)

    def _set_chess(self, row: int, column: int, chess: int) -> None:
        self.board[row][column] = chess 
    
    def _get_chess(self, row: int, column: int) -> int:
        return self.board[row][column]
    
    def _row(self, row: int) -> Set[int]:
        return set(self.board[row])
        
    def _column(self, column: int) -> Set[int]:
        return {self._get_chess(i, column) for i in range(self.size)}
    
    def _diagonals(self, row: int, column: int) -> Set[int]:
        return {self.board[i][j] 
                for i in range(self.size) 
                for j in range(self.size) 
                if (i+j) == (row+column) or (i-j) == (row-column)}
    
    def is_compatible(self, row: int, column: int) -> bool:
        if self.queen in (self._row(row) 
                          | self._column(column) 
                          | self._diagonals(row, column)):
            return False
        return True
  

def eight_queens(placements: Optional[List[Tuple[int, int]]] = None) -> Generator:
    if placements is None:
        for column in range(8):
            yield from eight_queens([(0, column)])
    else:
        if len(placements) == 8:
            yield placements
            return
        chessboard = Chessboard(queen_coordinates=placements)
        new_row = len(placements)
        for column in range(8):
            if chessboard.is_compatible(row=new_row, column=column):
                yield from eight_queens(list(placements) + [(new_row, column)])
