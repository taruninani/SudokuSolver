from SudokuSolver.Boards import ClassicBoard
from SudokuSolver.Solvers import IterativeSolver
import numpy as np

board = ClassicBoard()
# medium board
input = [
    [0, 0, 0, 0, 1, 0, 3, 7, 0],
    [0, 0, 0, 3, 0, 7, 4, 0, 0],
    [3, 0, 4, 0, 0, 0, 5, 6, 0],
    [0, 0, 1, 2, 0, 0, 0, 8, 4],
    [0, 0, 0, 0, 3, 0, 2, 5, 0],
    [8, 0, 0, 9, 0, 0, 0, 0, 3],
    [4, 0, 6, 0, 0, 1, 0, 0, 0],
    [0, 1, 8, 6, 9, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 9, 6]
]

board.boardInput(np.array(input), 0)

self = IterativeSolver(board)
self.recursivePass()

assert (board.isBoardComplete())
