from .BaseRuleSet import BaseRuleSet, np
from ..Boards import BoardsBase
from ..Utils import BaseException
import itertools


@BaseRuleSet.register
class SubGridRule(BaseRuleSet):

    def __init__(self, board: BoardsBase):
        super().__init__(board)
        if board.shape != (9, 9):
            raise BaseException('Rule only works for boards of shape (9, 9). Shape passed in ' + str(board.shape))

    def run(self) -> bool:
        for i in range(0, self._board.shape[0], 3):
            for j in range(0, self._board.shape[1], 3):
                [row_idx, col_idx] = self.getAffectedPlaces(i, j)
                values = self._board.board[row_idx, col_idx]
                # remove duplicates
                filledValues = np.delete(values, np.where(values == self._board.dummy)[0])
                if np.unique(filledValues).size != filledValues.size:
                    return False
        return True

    def __getPlaces__(self, i: np.int, j: np.int):
        subgrid_i = np.int(i / 3)
        subgrid_j = np.int(j / 3)
        temp = list(itertools.product([0, 1, 2], [0, 1, 2]))

        row_idx = np.array([x[0] for x in temp], dtype=np.int) + subgrid_i * 3
        col_idx = np.array([x[1] for x in temp], dtype=np.int) + subgrid_j * 3
        return [row_idx, col_idx]
