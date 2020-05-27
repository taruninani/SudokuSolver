from .BaseRuleSet import BaseRuleSet, np
import itertools

class KingsRule(BaseRuleSet):

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

    def __getPlaces(self,i: np.int, j : np.int):
        temp = list(itertools.product([-1, 1], [1, -1]))
        temp += list(itertools.product([-1, 1], [0]))
        temp += list(itertools.product([0], [-1, 1]))
        row_idx=np.array([x[0] for x in temp],dtype=np.int)+i
        col_idx=np.array([x[1] for x in temp],dtype=np.int)+j
        return [row_idx,col_idx]
