from .BoardsBase import BoardsBase
from ..RuleSets import RowRule, ColumnRule, SubGridRule


class ClassicBoard(BoardsBase):

    def __init__(self, shape: tuple = (9, 9)):
        super().__init__(shape)
        self.addRule(RowRule)
        self.addRule(ColumnRule)
        self.addRule(SubGridRule)
