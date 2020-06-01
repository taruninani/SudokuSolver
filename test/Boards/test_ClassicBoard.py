from unittest import TestCase
from SudokuSolver.Boards.ClassicBoard import ClassicBoard
from SudokuSolver.RuleSets import RowRule, ColumnRule, SubGridRule
import numpy as np


class TestClassicBoard(TestCase):

    def test_initBoard(self):
        board = ClassicBoard()

        self.assertEqual(board.shape, (9, 9))

        expectedRulesTypes = [RowRule, ColumnRule, SubGridRule]
        self.assertTrue(all([type(x) in expectedRulesTypes for x in board.ruleSet]))

    def test_placeNumberAt(self):
        board = ClassicBoard()
        board.placeNumberAt(4, 5, 5)
        self.assertEqual(board.board[4, 5], 5)
        self.assertEqual(len(board.moves), 1)

        mark = board.moves[0]
        self.assertEqual(mark.i, 4)
        self.assertEqual(mark.j, 5)
        self.assertEqual(mark.number, 5)
        self.assertEqual(mark.possibilityUpdated, [(4, 0, 4),
                                                   (4, 1, 4),
                                                   (4, 2, 4),
                                                   (4, 3, 4),
                                                   (4, 4, 4),
                                                   (4, 5, 4),
                                                   (4, 6, 4),
                                                   (4, 7, 4),
                                                   (4, 8, 4),
                                                   (0, 5, 4),
                                                   (1, 5, 4),
                                                   (2, 5, 4),
                                                   (3, 5, 4),
                                                   (5, 5, 4),
                                                   (6, 5, 4),
                                                   (7, 5, 4),
                                                   (8, 5, 4),
                                                   (3, 3, 4),
                                                   (3, 4, 4),
                                                   (5, 3, 4),
                                                   (5, 4, 4),
                                                   (4, 5, 0),
                                                   (4, 5, 1),
                                                   (4, 5, 2),
                                                   (4, 5, 3),
                                                   (4, 5, 5),
                                                   (4, 5, 6),
                                                   (4, 5, 7),
                                                   (4, 5, 8)])

    def test_undoOneMove(self):
        board = ClassicBoard()
        board.placeNumberAt(4, 5, 5)
        self.assertEqual(board.board[4, 5], 5)
        self.assertEqual(len(board.moves), 1)

        board.undoOneMove()
        self.assertEqual(len(board.moves), 0)
        self.assertEqual(board.board[4, 5], board.dummy)

        # one more undo would raise an error as no moves left to undo
        self.assertRaises(BaseException, board.undoOneMove)

    def test_isBoardComplete(self):
        completeBoard = np.array([
            [1, 8, 5, 3, 6, 7, 4, 2, 9],
            [9, 6, 2, 5, 1, 4, 3, 7, 8],
            [3, 7, 4, 8, 2, 9, 5, 6, 1],
            [8, 2, 7, 9, 4, 5, 6, 1, 3],
            [6, 4, 9, 1, 3, 8, 2, 5, 7],
            [5, 3, 1, 2, 7, 6, 9, 8, 4],
            [4, 9, 6, 7, 5, 1, 8, 3, 2],
            [2, 1, 8, 6, 9, 3, 7, 4, 5],
            [7, 5, 3, 4, 8, 2, 1, 9, 6]
        ])
        board = ClassicBoard()
        board.board = completeBoard
        self.assertTrue(board.isBoardComplete())

    def test_isBoardValid(self):
        validBoard = np.array([
            [0, 0, 0, 0, 0, 1, 0, 7, 0],
            [0, 0, 0, 0, 4, 0, 8, 0, 1],
            [0, 0, 6, 0, 2, 7, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 4],
            [5, 4, 0, 0, 1, 0, 3, 0, 0],
            [0, 0, 8, 0, 0, 6, 0, 5, 0],
            [0, 0, 5, 3, 0, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 0, 0, 6, 0],
            [0, 0, 0, 0, 6, 0, 4, 1, 0]
        ])
        board = ClassicBoard()
        board.board = validBoard
        self.assertTrue(board.isBoardValid())
