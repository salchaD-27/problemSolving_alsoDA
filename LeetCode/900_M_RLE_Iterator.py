from typing import List
class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0
    def next(self, n: int) -> int:
        while self.index < len(self.encoding):
            if self.encoding[self.index] >= n:
                self.encoding[self.index] -= n
                return self.encoding[self.index + 1]
            else:
                n -= self.encoding[self.index]
                self.index += 2
        return -1

from typing import List
class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.lst=encoding
    def next(self, n: int) -> int:
        num=-1
        while self.lst and n>0:
            if n<=self.lst[0]:
                self.lst[0]-=n  
                n=0
                num=self.lst[1]
            else:
                n-=self.lst[0]
                self.lst[0]=0
            if self.lst[0]==0:
                self.lst.pop(0)
                self.lst.pop(0)
        if n>0: return -1
        return num