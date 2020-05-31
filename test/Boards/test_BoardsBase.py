from unittest import TestCase
from SudokuSolver.Boards.BoardsBase import BoardsBase
import numpy as np
from SudokuSolver.Utils import BaseException
import pytest


class TestBoardsBase(TestCase):
    def test_getNumberAt(self):
        board = BoardsBase((9, 9))
        # check initial position at 4,5 is dummy value
        self.assertEqual(board.getNumberAt(4, 5), board.dummy)
        # mark 4,5 position as a value
        board.board[4, 5] = 4
        self.assertEqual(board.getNumberAt(4, 5), 4)

    def test_getPlacementOfNumber(self):
        board = BoardsBase((9, 9))
        # mark 4,5 position as a value
        board.board[4, 5] = 4
        board.getPlacementOfNumber(4)
        output = board.getPlacementOfNumber(4)
        expected = np.zeros(shape=(9, 9))
        expected[4, 5] = 1
        np.testing.assert_equal(output, expected)

    def test_isPlaceEmpty(self):
        board = BoardsBase((9, 9))
        # mark 4,5 position as a value
        board.board[4, 5] = 4
        # any other position should be empty
        for i in range(0, 9):
            for j in range(0, 9):
                val = True
                if i == 4 and j == 5:
                    val = False
                self.assertEqual(board.isPlaceEmpty(i, j), val)

    def test_placeNumberAt(self):
        board = BoardsBase((9, 9))
        board.placeNumberAt(4, 5, 5)
        self.assertEqual(board.board[4, 5], 5)
        self.assertEqual(len(board.moves), 1)
        mark = board.moves[0]
        self.assertEqual(mark.i, 4)
        self.assertEqual(mark.j, 5)
        self.assertEqual(mark.number, 5)
        self.assertEqual(mark.possibilityUpdated, [])

    def test_undoOneMove(self):
        board = BoardsBase((9, 9))
        board.placeNumberAt(4, 5, 5)
        self.assertEqual(board.board[4, 5], 5)
        self.assertEqual(len(board.moves), 1)

        board.undoOneMove()
        self.assertEqual(len(board.moves), 0)
        self.assertEqual(board.board[4, 5], board.dummy)

        # one more undo would raise an error as no moves left to undo
        self.assertRaises(BaseException, board.undoOneMove)

    # @pytest.skip('No way of testing this right now')
    def test_isBoardComplete(self):
        pass

    # @pytest.skip('No way of testing this right now')
    def test_isBoardValid(self):
        pass

    def test_shape(self):
        board = BoardsBase((9, 9))
        self.assertEqual(board.shape, (9, 9))
