from SudokuSolver.Utils.Logger import ColoredLogger,getLogger
from typing import List
import numpy as np

class BoardsBase(object):
    log : ColoredLogger
    ruleSet : List[int]
    board : np.array
    leftValues = None
    shape = None
    dummy = None

    def __init__(self,shape,ruleSet):
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
        return ~np.any(self.board==self.dummy)

    def isBoardValid(self):
        # run the ruleSet validators

        return True
