from .BaseRuleSet import BaseRuleSet, np

class RowRule(BaseRuleSet):

    def run(self) -> bool:
        for i in range(0,self._board.shape[0]):
            [row_idx,col_idx]=self.getAffectedPlaces(i,0)
            values=self._board.board[row_idx,col_idx]
            # remove duplicates
            filledValues = np.delete(values, np.where(values == self._board.dummy)[0])
            if np.unique(filledValues).size != filledValues.size:
                return False
        return True

    def __getPlaces(self,i: np.int, j : np.int):
        row_idx=np.full(self._board.shape[0],i,dtype=np.int)
        col_idx=np.array(range(0,self._board.shape[1]),dtype=np.int)
        return [row_idx,col_idx]