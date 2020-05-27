from ..Utils import getLogger, Logger
from ..RuleSets import BaseRuleSet
from typing import List
import numpy as np

class BoardsBase(object):
    log : Logger
    ruleSet : List[BaseRuleSet]
    board : np.array
    leftValues = None
    dummy = None

    def __init__(self,shape):
        super().__init__()
        self.log=getLogger(__name__)
        self.dummy=np.int(0)
        self.board=np.full(shape=shape,dtype=np.int,fill_value=self.dummy)

    def getNumberAt(self,i,j) -> np.int:
        return self.board[i,j]

    def getPlacementOfNumber(self,number : np.int ) -> np.array:
        return (self.board==number)*1

    def isPlaceEmpty(self,i,j) -> np.bool:
        return np.bool(self.board[i,j]==self.dummy)

    def placeNumberAt(self,i,j,number):
        self.board[i,j]=number

    def isBoardComplete(self):
        return ~np.any(self.board==self.dummy) and self.isBoardValid()

    def isBoardValid(self):
        # run the ruleSet validators
        for rule in self.ruleSet:
            check = rule.run()
            if check is False:
                return False

        return True

    @property
    def shape(self) -> tuple:
        return self.board.shape