import numpy as np
from typing import List


class Mark(object):
    i: np.int
    j: np.int
    number: np.int
    possibilityUpdated: List[tuple]

    def __init__(self, i: np.int, j: np.int, number: np.int, possibilityUpdated: List[tuple]):
        self.i = i
        self.j = j
        self.number = number
        self.possibilityUpdated = possibilityUpdated
