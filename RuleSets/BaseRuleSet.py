from abc import abstractmethod
from ..Boards import BoardsBase
from typing import List
import numpy as np

class BaseRuleSet(object):

    _board : BoardsBase

    def __init__(self,board : BoardsBase):
        self._board=board

    def getAffectedPlaces(self, i : np.int, j : np.int) -> [np.array,np.array]:
        [idx_i,idx_j]=self.__getPlaces(i,j)
        [idx_i,idx_j]=self.__filterPos__(idx_i,idx_j)
        return [idx_i,idx_j]

    def __filterPos__(self,idx_i : np.array, idx_j : np.array) -> [np.array,np.array]:
        invalid_i = np.logical_or(idx_i < 0, idx_i >= self._board.shape[0])
        invalid_j = np.logical_or(idx_j < 0, idx_j >= self._board.shape[1])
        valid_pos = np.logical_not(np.logical_or(invalid_i, invalid_j))

        return [idx_i[valid_pos], idx_j[valid_pos]]

    @abstractmethod
    def run(self) -> bool:
        pass

    @abstractmethod
    def __getPlaces(self,i: np.int, j : np.int) -> [np.array,np.array]:
        pass

