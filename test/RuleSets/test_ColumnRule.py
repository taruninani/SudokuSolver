from unittest import TestCase
import pytest
from SudokuSolver.Boards.BoardsBase import BoardsBase
from SudokuSolver.RuleSets.ColumnRule import ColumnRule
import numpy as np


class TestColumnRule(TestCase):

    # @pytest.skip('No way of testing this right now')
    def test_run(self):
        pass

    def test_getAffectedPlaces(self):
        board = BoardsBase((9, 9))
        rule = ColumnRule(board)

        [expected_i, expected_j] = [np.array(range(0, 9), dtype=np.int),
                                    np.zeros(shape=(9,), dtype=np.int)]
        [output_i, output_j] = rule.getAffectedPlaces(0, 0)
        np.testing.assert_equal(expected_j, output_j)
        np.testing.assert_equal(expected_i, output_i)
