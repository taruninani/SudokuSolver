from SudokuSolver.SudokuBoard import SudokuBoard
import numpy as np
import itertools

class SudokuBoardMiracle(SudokuBoard):

    def updatePossibilityMat(self, i, j):
        super().updatePossibilityMat(i,j)

        val=self.board[i,j]
        # miracle sudoku requires knights move to also not be the same value
        knightPos=self.getKnightsPositionForPlace(i,j)
        for pos in knightPos:
            self.removeValueAsPossiblity(pos[0], pos[1], val)

        # miracle sudoku requires kings move to also not be the same value
        kingsPos=self.getKingsPositionForPlace(i,j)
        for pos in kingsPos:
            self.removeValueAsPossiblity(pos[0], pos[1], val)

        # orthogonally adjacent cells cannot cannot have consecutive value
        adjacentPos=self.getOrthogonalAdjacentPositionForPlace(i,j)
        consecutiveVal=np.array([val+1,val-1])
        validConsecutiveVal=np.logical_and(consecutiveVal>=1,consecutiveVal<=9)
        consecutiveVal=consecutiveVal[validConsecutiveVal]

        for cV in consecutiveVal:
            for pos in adjacentPos:
                self.removeValueAsPossiblity(pos[0], pos[1], int(cV))

    def getKnightsPositionForPlace(self,i,j):
        idx_i  = list(itertools.product([1, 2], [-1,  1]))
        idx_i += list(itertools.product([1, 2], [ 1, -1]))
        idx_j  = list(itertools.product([2, 1], [ 1, -1]))
        idx_j += list(itertools.product([2, 1], [ 1, -1]))
        idx_i = [x[0] * x[1] for x in idx_i]
        idx_j = [x[0] * x[1] for x in idx_j]
        temp=list(zip(idx_i,idx_j))
        return self.__getValidPos__(i,j,temp)

    def getKingsPositionForPlace(self,i,j):
        temp = list(itertools.product([-1, 1], [1, -1]))
        temp += list(itertools.product([-1,1], [0]))
        temp += list(itertools.product([0], [-1, 1]))
        return self.__getValidPos__(i,j,temp)

    def getOrthogonalAdjacentPositionForPlace(self,i,j):
        temp = list(itertools.product([-1, 1], [0]))
        temp += list(itertools.product([0], [-1, 1]))
        return self.__getValidPos__(i,j,temp)


    def __getValidPos__(self,i,j,positions):
        idx_i = np.array([x[0] for x in positions])
        idx_j = np.array([x[1] for x in positions])
        temp_i = idx_i + i
        temp_j = idx_j + j

        invalid_i = np.logical_or(temp_i < 0, temp_i >= 9)
        invalid_j = np.logical_or(temp_j < 0, temp_j >= 9)
        valid_pos = np.logical_not(np.logical_or(invalid_i, invalid_j))

        return list(zip(temp_i[valid_pos], temp_j[valid_pos]))

    def doesValueHaveAtleastOnePlace(self,val):
        possiblePlaces=self.getPossiblePlacesForValue(val)
        filledPlaces=self.getFilledPlacesForValue(val)
        places=np.logical_or(filledPlaces, possiblePlaces)

        # check if each row has a value
        for i in range(0,self.numRows):
            if ( True in possiblePlaces[i,:] ):
                continue
            return False

        # check if each row has a value
        for i in range(0,self.numCols):
            if ( True in possiblePlaces[:,i] ):
                continue
            return False

        return True

    def refinePossibilityPlacesForValues(self,val):
        possiblePlaces=self.getPossiblePlacesForValue(val)
        for i in range(0,self.numRows):
            for j in range(0,self.numCols):
                if possiblePlaces[i,j] == 1:
                    self.possibleMat[i][j]
