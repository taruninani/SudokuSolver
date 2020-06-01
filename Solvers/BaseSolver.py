from ..Utils import Logger, getLogger, BaseException


class BaseSolver(object):
    log: Logger

    def __init__(self):
        self.log = getLogger(self.__class__.__name__)

    def solve(self):
        raise BaseException('Implement this!')
