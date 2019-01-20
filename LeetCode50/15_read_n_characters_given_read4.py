from typing import List

class Reader4(object):

    _inputs: List[str] = None
    _current: int = 0

    def __init__(self, i):
        self._inputs = i

    def read4(self, buf: List[str]) -> int:
        pass

