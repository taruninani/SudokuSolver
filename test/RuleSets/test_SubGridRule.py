from unittest import TestCase
import pytest
from SudokuSolver.Boards.BoardsBase import BoardsBase
from SudokuSolver.RuleSets.SubGridRule import SubGridRule
import numpy as np


class TestSubGridRule(TestCase):

    # @pytest.skip('No way of testing this right now')
    def test_run(self):
        pass

    def test_getAffectedPlaces(self):
        board = BoardsBase((9, 9))
        rule = SubGridRule(board)

        # case 1 : pick an corner position
        expected_i = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
        expected_j = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2])

        [output_i, output_j] = rule.getAffectedPlaces(0, 0)
        np.testing.assert_equal(expected_j, output_j)
        np.testing.assert_equal(expected_i, output_i)

        # case 2 : pick somewhere in the middle of an edge
        expected_i = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
        expected_j = np.array([3, 4, 5, 3, 4, 5, 3, 4, 5])

        [output_i, output_j] = rule.getAffectedPlaces(0, 4)
        np.testing.assert_equal(expected_j, output_j)
        np.testing.assert_equal(expected_i, output_i)

        # case 3 : pick somehwere in the middle of the board
        expected_i = np.array([3, 3, 3, 4, 4, 4, 5, 5, 5])
        expected_j = np.array([3, 4, 5, 3, 4, 5, 3, 4, 5])

        [output_i, output_j] = rule.getAffectedPlaces(4, 4)
        np.testing.assert_equal(expected_j, output_j)
        np.testing.assert_equal(expected_i, output_i)
