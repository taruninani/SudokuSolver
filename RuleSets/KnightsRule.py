from .BaseRuleSet import BaseRuleSet, np
import itertools


@BaseRuleSet.register
class KnightsRule(BaseRuleSet):

    def run(self) -> bool:
        for i in range(0,self._board.shape[0]):
            for j in range(0,self._board.shape[1]):
                [row_idx,col_idx]=self.getAffectedPlaces(i,j)
                values=self._board.board[row_idx,col_idx]
                # remove duplicates
                filledValues = np.delete(values, np.where(values == self._board.dummy)[0])
                if np.unique(filledValues).size != filledValues.size:
                    return False
        return True

    def __getPlaces__(self, i: np.int, j: np.int):
        idx_i = list(itertools.product([1, 2], [-1, 1]))
        idx_i += list(itertools.product([1, 2], [1, -1]))
        idx_j = list(itertools.product([2, 1], [1, -1]))
        idx_j += list(itertools.product([2, 1], [1, -1]))
        row_idx = np.array([x[0] * x[1] for x in idx_i],dtype=np.int) + i
        col_idx = np.array([x[0] * x[1] for x in idx_j],dtype=np.int) + j

        return [row_idx,col_idx]
