from .BaseRuleSet import BaseRuleSet, np

class ColumnRule(BaseRuleSet):

    def run(self) -> bool:
        for j in range(0,self._board.shape[1]):
            [row_idx,col_idx]=self.getAffectedPlaces(0,j)
            values=self._board.board[row_idx,col_idx]
            # remove duplicates
            filledValues = np.delete(values, np.where(values == self._board.dummy)[0])
            if np.unique(filledValues).size != filledValues.size:
                return False
        return True

    def __getPlaces(self,i: np.int, j : np.int):
        row_idx=np.array(range(0,self._board.shape[0]),dtype=np.int)
        col_idx=np.full(self._board.shape[1],j,dtype=np.int)

        return [row_idx,col_idx]