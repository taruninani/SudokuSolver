from SudokuSolver.Logger import Logger, LOGLEVEL
import numpy as np
import copy

class SudokuBoard(object):
    logger = None
    board = None
    leftValues = None
    numRows = None
    numCols = None
    possibleMat=None
    dummy=None

    def __init__(self,input):
        # Initialize
        self.logger = Logger()
        self.numRows=9
        self.numCols=9
        self.dummy=0
        self.board = np.zeros(shape=(self.numRows,self.numCols))
        self.possibleMat=[]
        for i in range(0,self.numRows):
            self.possibleMat+=[[self.dummy]*9]
            for j in range(0,self.numCols):
                self.possibleMat[i][j]=self.getValidValues()

        assert(self.numCols==self.numRows)

        maxVal=max(self.numRows,self.numCols)

        self.leftValues = np.array([maxVal] * maxVal)  # all numbers must come only 9 times

        # check which numbers have been entered and remove them from the leftValues
        for i in range(0, input.shape[0]):
            for j in range(0, input.shape[1]):
                if input[i][j] != self.dummy:
                    self.markValue(i, j, input[i][j])

    def getValidValues(self):
        return np.array(list(range(1,self.numRows+1)))

    def clearValue(self, i, j):
        self.markValue(i,j,self.dummy)
        self.rebuildPossiblityMat()

    def clearValues(self,all_i,all_j):
        for idx in range(0,len(all_i)):
            self.markValue(all_i[idx],all_j[idx],self.dummy)
        self.rebuildPossiblityMat()

    def rebuildPossiblityMat(self):
        self.leftValues = np.array([self.numRows] * self.numRows)  # all numbers must come only 9 times
        for i in range(0,self.numRows):
            for j in range(0,self.numCols):
                self.possibleMat[i][j]=self.getValidValues()

        for i in range(0,self.numRows):
            for j in range(0,self.numCols):
                if self.board[i,j] != self.dummy:
                    self.markValue(i,j,self.getValue(i,j).astype(int))

    def markValue(self, i, j, val):
        self.board[i, j] = val
        if val==self.dummy:
            # add the removed value back in
            self.leftValues[self.board[i,j].astype(int)-1]+=1
            return
        else:
            self.leftValues[val - 1] -= 1

        # update the possiblity matrix
        if self.numRows == 9:
              # remove the possibilities for that position
            self.possibleMat[i][j] = np.array([])
            # remove it for column and row elements
            for k in range(0, self.numRows):
                self.possibleMat[i][k] = np.setdiff1d(self.possibleMat[i][k], val)
                self.possibleMat[k][j] = np.setdiff1d(self.possibleMat[k][j], val)

            # remove it for the subcell 3x3
            subcell_i = int(i / 3)
            subcell_j = int(j / 3)
            for ii in range(0, int(self.numRows / 3)):
                for jj in range(0, int(self.numCols / 3)):
                    idx_i = ii + subcell_i * 3
                    idx_j = jj + subcell_j * 3
                    self.possibleMat[idx_i][idx_j] = np.setdiff1d(self.possibleMat[idx_i][idx_j], val)

            # iterate through each

    def getPossibleValues(self,i,j) -> np.array:
        return self.possibleMat[i][j]

    def getPossibleValuesCount(self) -> np.array:
        output=np.zeros(shape=(self.numRows,self.numCols))
        for i in range(0,self.numRows):
            for j in range(0,self.numCols):
                output[i,j]=self.possibleMat[i][j].size

        return output

    def getPossiblePlacesForValue(self,val):
        output=np.zeros(shape=(self.numRows,self.numCols))
        for i in range(0,self.numRows):
            for j in range(0,self.numCols):
                if val in self.possibleMat[i][j]:
                    output[i,j]=1
        return output

    def isBoardComplete(self):
        validValues=self.getValidValues()
        for i in range(0,self.numRows):
            values=self.getRow(i)
            diff=np.setdiff1d(validValues,values)
            if diff.size != 0:
                return False
        return True

    def isBoardValid(self):
        # validate rows
        for i in range(0,self.numRows):
            values=self.getRow(i)
            filledValues=np.delete(values,np.where(values==self.dummy)[0])
            if np.unique(filledValues).size != filledValues.size:
                return False

        # validate cols
        for i in range(0,self.numCols):
            values=self.getCol(i)
            filledValues=np.setdiff1d(values,self.dummy)
            if np.unique(filledValues).size != filledValues.size:
                return False

        # validate subcell 3x3
        for subcell_i in range(0,int(self.numRows / 3)):
            for subcell_j in range(0,int(self.numCols / 3)):
                values=[]
                for ii in range(0, int(self.numRows / 3)):
                    for jj in range(0, int(self.numCols / 3)):
                        idx_i = ii + subcell_i * 3
                        idx_j = jj + subcell_j * 3
                        values+=[self.board[idx_i,idx_j]]
                values=np.array(values)
                filledValues=np.setdiff1d(values,self.dummy)
                if np.unique(filledValues).size != filledValues.size:
                    return False

        return True

    def isPlaceEmpty(self,i,j):
        return self.board[i,j]==self.dummy

    def getValue(self,i,j):
        return self.board[i,j]

    def getCol(self,i):
        return self.board[:,i]

    def getRow(self,i):
        return self.board[i,:]

    def getBoardShape(self):
        return self.board.shape

    def log(self,string):
        print(string)

    def getEmptyPlacesForRow(self,i):
        output = []
        for j in range(0, self.board.shape[1]):
            if self.isPlaceEmpty(i,j):
                output += [j]
        return np.array(output)

    def getEmptyPlacesForCol(self,j):
        output = []
        for i in range(0, self.board.shape[0]):
            if self.isPlaceEmpty(i,j):
                output += [i]
        return np.array(output)

    def getMissingValuesForRow(self,i):
        values=self.getRow(i)
        possible=self.getValidValues()
        output=np.array(list(set(possible).difference(set(values))))
        return output

    def getMissingValuesForCol(self,i):
        values=self.getCol(i)
        possible = self.getValidValues()
        output=np.array(list(set(possible).difference(set(values))))
        return output

    def isValueInRow(self,val,i):
        return val in self.board[i,:]

    def isValueInCol(self,val,j):
        return val in self.board[:,j]

    def getCopy(self):
        return copy.deepcopy(self)
