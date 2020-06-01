from .IterativeSolver import IterativeSolver
import numpy as np


class BackTrackSolver(IterativeSolver):

    def solve(self):
        self.recursivePass()
        self.backTrack(0)

    def backTrack(self, depth):
        self.log.debug('Depth in the decision tree : {0}'.format(depth))
        if self._board.isBoardComplete():
            self.log.debug('Leaving depth {0} in the decision tree'.format(depth))
            return True

        possibleValuesCount = np.sum(self._board.possibilityMat, 2)
        [all_i, all_j] = np.where(possibleValuesCount != 0)

        if all_i.size == 0:
            self.log.warning('Exhausted all options at this point')
            self.log.debug('Leaving depth {0} in the decision tree'.format(depth))
            return False

        for (i, j) in zip(all_i, all_j):
            possibleValues = np.where(self._board.possibilityMat[i, j] == True)[0] + 1

            for val in possibleValues:
                self.log.info('AssumptionMade : ({0},{1}) has value {2}'.format(i, j, val))
                self._board.placeNumberAt(i, j, val)
                updatedPos = self.recursivePass()

                result = self.backTrack(depth + 1)
                if result:
                    self.log.debug('Leaving depth {0} in the decision tree'.format(depth))
                    return True

                # undo all moves done by recursivePass
                for temp in updatedPos:
                    self._board.undoOneMove()
                # undo the assumption made above
                self._board.undoOneMove()

        self.log.debug('Leaving depth {0} in the decision tree'.format(depth))
