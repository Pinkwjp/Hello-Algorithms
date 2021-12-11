from unittest import TestCase, main 

from algorithms_refined.recursion.eight_queens import (Chessboard, eight_queens)


class ChessboardTestCase(TestCase):
    def test_set_get(self):
        board = Chessboard()
        board._set_chess(row=0, column=0, chess=100) 
        self.assertEqual(board._column(0), set([0]*7 + [100]))
    
    def test_is_compatible(self):
        board = Chessboard()
        board._set_chess(row=3, column=3, chess=board.queen) 
        self.assertFalse(board.is_compatible(row=0, column=3)) 
        self.assertFalse(board.is_compatible(row=3, column=0)) 
        self.assertTrue(board.is_compatible(row=2, column=1)) 
    
    def test_repr(self):
        board = Chessboard()
        board._set_chess(row=3, column=3, chess=board.queen) 
        print()
        print(board)


class EightQueensTestCase(TestCase):
    def test_correctness(self):
        placements = list(eight_queens())
        for placement in placements:
            board = Chessboard()
            for (row, column) in placement:
                with self.subTest():
                    board.is_compatible(row=row, column=column)
                    board._set_chess(row=row, column=column, chess=board.queen)

    def test_placement_count(self):
        placements = list(eight_queens())
        self.assertEqual(len(placements), 92)
        

if __name__ == '__main__':
    main()