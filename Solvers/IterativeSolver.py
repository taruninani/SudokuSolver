from SudokuSolver.Boards import ClassicBoard, BoardsBase
from SudokuSolver.RuleSets import BaseRuleSet
import numpy as np
from typing import List
from SudokuSolver.Solvers.BaseSolver import BaseSolver


class IterativeSolver(BaseSolver):
    _board: BoardsBase

    def __init__(self, board: BoardsBase):
        super().__init__()
        self._board = board

    def singlePass(self) -> List[tuple]:
        self.log.info('Commencing a single iterative pass')
        updatedPos = []
        ## For each position
        #    Check if any position has just one possibility
        #       -- if so then place that number
        for i in range(0, self._board.shape[0]):
            for j in range(0, self._board.shape[1]):
                possibleValuesPos = np.where(self._board.possibilityMat[i, j] == True)[0]
                if possibleValuesPos.size == 1:
                    self.log.info('Only one possibility at ({0},{1})'.format(i, j))
                    # only one element and add 1 because the current value is the idx of the value
                    self._board.placeNumberAt(i, j, possibleValuesPos[0] + 1)
                    updatedPos.append((i, j))

        ## For Each Rule check
        ### For Each number
        #     Check if possibility in affectedPlaces allow for just one place
        #       -- if so then place that number
        # assume the numbers are from 1 to length of the row of the board (n)
        # but we iterate over 0 to n-1
        for i in range(0, self._board.shape[0]):
            (posi, posj) = np.where(self._board.possibilityMat[:, :, i] == True)
            for (ii, jj) in zip(posi, posj):
                for rule in self._board.ruleSet:
                    [affected_i, affected_j] = rule.getAffectedPlaces(ii, jj)
                    # vector of bool stating if the affected places can have the number i
                    possiblePlaces = np.where(self._board.possibilityMat[[affected_i, affected_j, [i]]] == True)[0]
                    # if only one place is possible then
                    if possiblePlaces.size == 1:
                        possiblePlaces = possiblePlaces[0]
                        self.log.info(
                            'Only one possibility at ({0},{1}) due to rule {2}'.format(affected_i[possiblePlaces],
                                                                                       affected_j[possiblePlaces],
                                                                                       rule.__class__.__name__))
                        # number is actually i+1, i is the idx of the number in the array
                        self._board.placeNumberAt(affected_i[possiblePlaces], affected_j[possiblePlaces], i + 1)
                        updatedPos.append((affected_i[possiblePlaces], affected_j[possiblePlaces]))

        self.log.info('Completed the single iterative pass')

        return updatedPos

    def recursivePass(self) -> List[tuple]:
        self.log.info('Running Recursive Iterative Passes...')
        allUpdatedPos = []
        updatedPos = self.singlePass()
        while len(updatedPos) != 0:
            allUpdatedPos += updatedPos
            updatedPos = self.singlePass()

        self.log.info('Completed Recursive Iterative Pass.')
        return allUpdatedPos

    def solve(self):
        self.recursivePass()
