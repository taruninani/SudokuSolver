from SudokuSolver.Boards import ClassicBoard
from SudokuSolver.Solvers import BackTrackSolver
import numpy as np

board = ClassicBoard()
# expert board
input = [
    [0, 0, 0, 0, 0, 1, 0, 7, 0],
    [0, 0, 0, 0, 4, 0, 8, 0, 1],
    [0, 0, 6, 0, 2, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [5, 4, 0, 0, 1, 0, 3, 0, 0],
    [0, 0, 8, 0, 0, 6, 0, 5, 0],
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 6, 0, 4, 1, 0]
]

board.boardInput(np.array(input), 0)

backTracker = BackTrackSolver(board)
backTracker.recursivePass()

backTracker.solve()

assert (board.isBoardComplete())
