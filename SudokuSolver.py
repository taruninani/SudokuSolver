from SudokuSolver.Logger import Logger, LOGLEVEL
from SudokuSolver.SudokuBoard import SudokuBoard
import numpy as np

class SudokuSolver(object):
    logger: Logger
    board: SudokuBoard

    def log(self,string):
        """
        Logger
        Parameters
        ----------
        string

        Returns
        -------

        """
        print(string)

    def __init__(self,board):
        """

        """
        #Initialize
        self.logger=Logger()
        self.board=board

    def iterativePass(self):
        updateMade=False
        updated_i=[]
        updated_j=[]
        # iterate through each row
        shape=self.board.getBoardShape()
        for i in range(0,shape[0]):
            for j in range(0,shape[1]):
                possibleValues=self.board.getPossibleValues(i,j)
                if possibleValues.size == 1:
                    self.board.markValue(i,j,possibleValues[0])
                    updateMade=True
                    updated_i+=[i]
                    updated_j+=[j]

        # check for each subcell 3x3 if one of the possible Values occurs just once
        for subcell_i in range(0, int(shape[0] / 3)):
            for subcell_j in range(0, int(shape[1] / 3)):
                values = np.zeros(self.board.getValidValues().shape)
                # count how many possible cells does each value can be assigned to
                for ii in range(0, int(shape[0]/ 3)):
                    for jj in range(0, int(shape[1]/ 3)):
                        idx_i = ii + subcell_i * 3
                        idx_j = jj + subcell_j * 3
                        possibleValues=self.board.getPossibleValues(idx_i,idx_j)
                        for val in possibleValues:
                            values[val-1]+=1
                # check if one of the numbers can be filled in only one cell
                [all_i,]=np.where(values==1)
                for idx in all_i:
                    # count of the valid values how many times does the
                    val = idx + 1
                    for ii in range(0, int(shape[0] / 3)):
                        for jj in range(0, int(shape[1] / 3)):
                            idx_i = ii + subcell_i * 3
                            idx_j = jj + subcell_j * 3
                            possibleValues = self.board.getPossibleValues(idx_i, idx_j)
                            if np.any(possibleValues==(val)):
                                # if true then this value can be only assigned here
                                self.board.markValue(idx_i,idx_j,val)
                                updateMade = True
                                updated_i += [idx_i]
                                updated_j += [idx_j]

        # check for each row if one of the possible Values occurs just once
        for i in range(0,shape[0]):
            values = np.zeros(self.board.getValidValues().shape)
            for j in range(0, shape[1]):
                possibleValues = self.board.getPossibleValues(i, j)
                for val in possibleValues:
                    values[val - 1] += 1
            # check if one of the numbers can be filled in only one cell
            [all_i, ] = np.where(values == 1)
            for idx in all_i:
                # count of the valid values how many times does the
                val = idx + 1
                for j in range(0, shape[1]):
                    possibleValues = self.board.getPossibleValues(i, j)
                    if np.any(possibleValues==(val)):
                        # if true then this value can be only assigned here
                        self.board.markValue(i,j,val)
                        updateMade = True
                        updated_i += [i]
                        updated_j += [j]

        # check for each col if one of the possible Values occurs just once
        for j in range(0, shape[1]):
            values = np.zeros(self.board.getValidValues().shape)
            for i in range(0, shape[0]):
                possibleValues = self.board.getPossibleValues(i, j)
                for val in possibleValues:
                    values[val - 1] += 1
            # check if one of the numbers can be filled in only one cell
            [all_j, ] = np.where(values == 1)
            for idx in all_j:
                # count of the valid values how many times does the
                val = idx + 1
                for i in range(0, shape[0]):
                    possibleValues = self.board.getPossibleValues(i, j)
                    if np.any(possibleValues == (val)):
                        # if true then this value can be only assigned here
                        self.board.markValue(i, j, val)
                        updateMade = True
                        updated_i += [i]
                        updated_j += [j]

        return [updateMade,updated_i,updated_j]

    def bruteForceAssume(self,i,j,values):
        atLeastOneChangeMade=False
        for val in values:
            self.logger.info('AssumptionMade : {0},{1} has value {2}'.format(i,j,val))
            self.board.markValue(i,j,val)
            [atLeastOneChangeMade,updated_i,updated_j]=self.fullIterativePass()

            if not self.board.isBoardValid() or not atLeastOneChangeMade:
                self.logger.warn('Assumption didnt work resetting board.')
                self.board.clearValues(updated_i,updated_j)
                atLeastOneChangeMade=False
                updated_i=[]
                updated_j=[]

        return [atLeastOneChangeMade,updated_i,updated_j]

    def fullIterativePass(self):
        # run with no assumptions
        [updatedBoard,updated_i,updated_j] = self.iterativePass()
        atLeastOneChangeMade = False
        inc = 1
        while updatedBoard:
            inc += 1
            atLeastOneChangeMade = True
            [updatedBoard,new_updated_i,new_updated_j] = self.iterativePass()
            updated_i+=new_updated_i
            updated_j+=new_updated_j
            self.logger.info('Iteration Number : {0}'.format(inc))

        return [atLeastOneChangeMade,updated_i,updated_j]


    def solve(self):
        """
        Solve the given sudoku board

        Returns
        -------

        """

        self.fullIterativePass()

        self.backtrack(0)

    def backtrack(self,depth):
        self.logger.debug('Enter AT depth : {0}'.format(depth))
        if self.board.isBoardComplete():
            return True
        # get the first input with the least possible values
        possibleValuesCount=self.board.getPossibleValuesCount()
        [all_i,all_j]=np.where(possibleValuesCount != 0)
        if all_i.size == 0:
            self.logger.warn('Exhausted all options')
            return False
        for idx in range(0,all_i.size):
            i=all_i[idx]
            j=all_j[idx]
            possibleValues=self.board.getPossibleValues(i,j)

            for val in possibleValues:
                self.logger.info('AssumptionMade : {0},{1} has value {2}'.format(i,j,val))
                self.board.markValue(i,j,val)
                [atLeastOneChangeMade,updated_i,updated_j]=self.fullIterativePass()

                # if not self.board.isBoardValid():
                #     self.log('Assumption didnt work resetting board.')
                #     self.board.clearValues(updated_i,updated_j)
                updated_i+=[i]
                updated_j+=[j]
                result = self.backtrack(depth+1)
                if result:
                    return True

                self.board.clearValues(updated_i, updated_j)

        self.logger.debug('Left AT depth : {0}'.format(depth))
