from unittest import TestCase
import pytest
from SudokuSolver.Boards.BoardsBase import BoardsBase
from SudokuSolver.RuleSets import KingsRule
import numpy as np


class TestKingsRule(TestCase):

    # @pytest.skip('No way of testing this right now')
    def test_run(self):
        pass

    def test_getAffectedPlaces(self):
        board = BoardsBase((9, 9))
        rule = KingsRule(board)

        # case 1 : pick an corner position
        expected_i = np.array([1, 1, 0, 0])
        expected_j = np.array([1, 0, 1, 0])

        [output_i, output_j] = rule.getAffectedPlaces(0, 0)
        np.testing.assert_equal(expected_j, output_j)
        np.testing.assert_equal(expected_i, output_i)

        # case 2 : pick somewhere in the middle of an edge
        expected_i = np.array([1, 1, 1, 0, 0, 0])
        expected_j = np.array([5, 3, 4, 3, 5, 4])

        [output_i, output_j] = rule.getAffectedPlaces(0, 4)
        np.testing.assert_equal(expected_j, output_j)
        np.testing.assert_equal(expected_i, output_i)

        # case 3 : pick somehwere in the middle of the board
        expected_i = np.array([1, 1, 3, 3, 1, 3, 2, 2, 2])
        expected_j = np.array([5, 3, 5, 3, 4, 4, 3, 5, 4])

        [output_i, output_j] = rule.getAffectedPlaces(2, 4)
        np.testing.assert_equal(expected_j, output_j)
        np.testing.assert_equal(expected_i, output_i)
