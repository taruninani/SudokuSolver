from SudokuSolver.Boards import ClassicBoard
from SudokuSolver.Solvers import BackTrackSolver
import numpy as np

board = ClassicBoard()
# hard board
input = [
    [0, 0, 0, 0, 8, 0, 0, 0, 5],
    [8, 5, 1, 4, 0, 9, 0, 0, 0],
    [4, 0, 0, 0, 2, 0, 8, 0, 0],
    [0, 6, 8, 0, 0, 7, 9, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [1, 9, 0, 0, 0, 3, 2, 0, 4],
    [0, 0, 4, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 1, 9, 6, 7, 0, 0, 0, 0]
]

board.boardInput(np.array(input), 0)

backTracker = BackTrackSolver(board)
backTracker.solve()

assert (board.isBoardComplete())
