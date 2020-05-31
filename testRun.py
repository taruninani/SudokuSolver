import numpy as np
import SudokuSolver.SudokuSolver as solver
import SudokuSolver.SudokuBoard as board

# easy board
input=[
    [0,0,5,3,6,0,4,0,0],
    [9,6,2,0,0,4,0,7,0],
    [3,0,4,0,2,9,0,6,0],
    [8,2,0,9,4,0,0,1,3],
    [0,4,9,0,3,0,0,5,7],
    [0,0,0,2,0,0,9,8,0],
    [4,0,6,0,0,1,0,0,2],
    [0,0,0,6,9,3,0,0,5],
    [0,0,3,0,8,0,0,0,0]
]

# medium
input=[
    [0,0,0,0,1,0,3,7,0],
    [0,0,0,3,0,7,4,0,0],
    [3,0,4,0,0,0,5,6,0],
    [0,0,1,2,0,0,0,8,4],
    [0,0,0,0,3,0,2,5,0],
    [8,0,0,9,0,0,0,0,3],
    [4,0,6,0,0,1,0,0,0],
    [0,1,8,6,9,0,0,0,0],
    [7,0,0,0,0,0,0,9,6]
]

# hard
input=[
    [0,0,0,0,8,0,0,0,5],
    [8,5,1,4,0,9,0,0,0],
    [4,0,0,0,2,0,8,0,0],
    [0,6,8,0,0,7,9,0,0],
    [0,4,0,0,0,0,0,0,7],
    [1,9,0,0,0,3,2,0,4],
    [0,0,4,0,0,0,0,6,0],
    [0,0,0,0,0,2,0,0,0],
    [0,1,9,6,7,0,0,0,0]
]


# expert
input = [
    [0,0,0,0,0,1,0,7,0],
    [0,0,0,0,4,0,8,0,1],
    [0,0,6,0,2,7,0,0,0],
    [0,0,0,0,0,0,0,0,4],
    [5,4,0,0,1,0,3,0,0],
    [0,0,8,0,0,6,0,5,0],
    [0,0,5,3,0,0,0,0,0],
    [9,0,0,0,0,0,0,6,0],
    [0,0,0,0,6,0,4,1,0]
]

# custom sourced
input = [
    [0, 0, 0, 0, 5, 1, 4, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 2, 0],
    [0, 0, 8, 0, 0, 0, 0, 0, 3],
    [0, 1, 0, 0, 0, 0, 0, 0, 8],
    [5, 0, 0, 0, 4, 0, 0, 0, 9],
    [7, 0, 0, 0, 0, 0, 0, 6, 0],
    [4, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 2, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 3, 9, 8, 0, 0, 0, 0]
]

input=np.array(input)

self=board.SudokuBoard(input)

#self.getPossibleValues(0,0)


self=solver.SudokuSolver(self)
#
# self.solve()
#
# self.board.isBoardComplete()
#
# self.board.isBoardValid()
#
# self.board.board


import SudokuSolver.SudokuBoardMiracle as boardMiracle

input =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


input=np.array(input)

self=boardMiracle.SudokuBoardMiracle(input)

#
# miracle=solver.SudokuSolver(self)
# miracle.fullIterativePass()
#
# miracle.solve()



## New structure
# Possibility.py : class which manages the possibility matrix, input is a ruleset and shape of board
#
# rules.py : interface for implementing the rules
# ClassicRuleSet.py : extends rules.py to create the classic rules of sudoku
# KnightsRuleSet.py : extends rules.py to create the KNights move Rule set
# KingsRuleSet.py : extends rules.py to create the Kings move Rule set
# ...
#
# board.py : interface for implementing a Sudoku Board
# ClassicSudoku.py : inherit board.py with ClassicRulesets
# MiracleSudoku.py :
