from ..Utils import getLogger, Logger, Mark, BaseException
from ..RuleSets import BaseRuleSet
from typing import List
import numpy as np


class BoardsBase(object):
    log: Logger
    ruleSet: List[BaseRuleSet]
    board: np.array
    leftValues = None
    dummy = None
    moves: List[Mark]
    possibilityMat: np.array

    def __init__(self, shape: tuple):
        super().__init__()
        self.log = getLogger(self.__class__.__name__)
        self.dummy = np.int(0)
        self.board = np.full(shape=shape, dtype=np.int, fill_value=self.dummy)
        self.moves = []
        self.ruleSet = []
        self.possibilityMat = np.ones(shape=(9, 9, 9), dtype=np.bool)
        self.log.info('Initialized Board')

    def getNumberAt(self, i, j) -> np.int:
        number = self.board[i, j]
        self.log.debug('Position ({0},{1}) has value {2}'.format(i, j, number))
        return number

    def getPlacementOfNumber(self, number: np.int) -> np.array:
        self.log.debug('Requested which position is the number {0} placed.'.format(number))
        return (self.board == number) * 1

    def isPlaceEmpty(self, i, j) -> np.bool:
        return np.bool(self.board[i, j] == self.dummy)

    def placeNumberAt(self, i, j, number):
        self.log.info('Placing number {0} at ({1},{2})'.format(number, i, j))
        self.board[i, j] = number
        # number-1 is the position of the number in the array
        markedIdx = []
        for rule in self.ruleSet:
            # returns back i,j too
            [idx_i, idx_j] = rule.getAffectedPlaces(i, j)
            for (ii, jj) in zip(idx_i, idx_j):
                if self.possibilityMat[ii, jj, number - 1]:
                    self.possibilityMat[ii, jj, number - 1] = False
                    markedIdx.append((ii, jj))
        # create Mark object and mark the number
        mark = Mark(i, j, number, markedIdx)
        self.moves.append(mark)

    def undoOneMove(self):
        if len(self.moves) == 0:
            self.log.error('No moves to undo!')
            raise BaseException('No moves to undo!')
        mark = self.moves.pop()
        self.board[mark.i, mark.j] = self.dummy
        for (ii, jj) in mark.possibilityUpdated:
            self.possibilityMat[ii, jj, mark.number - 1] = True
        self.log.info('Move Undone. Position ({0},{1}) has no number'.format(mark.i, mark.j))

    def isBoardComplete(self):
        isComplete = ~np.any(self.board == self.dummy) and self.isBoardValid()
        if isComplete:
            self.log.info('Board is complete!')
        return isComplete

    def isBoardValid(self):
        # run the ruleSet validators
        for rule in self.ruleSet:
            check = rule.run()
            if check is False:
                return False

        self.log.debug('Board is valid.')
        return True

    def addRule(self, rule: type(BaseRuleSet)):
        self.log.info('Adding rule : {0}'.format(rule.__name__))
        self.ruleSet.append(rule(self))

    @property
    def shape(self) -> tuple:
        return self.board.shape
