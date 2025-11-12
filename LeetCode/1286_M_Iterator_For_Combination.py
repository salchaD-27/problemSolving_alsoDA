class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.n = len(characters)
        self.k = combinationLength
        self.idx = list(range(self.k))
        self.ok = True
    def next(self) -> str:
        res = ''.join(self.s[i] for i in self.idx)
        i = self.k - 1
        while i >= 0 and self.idx[i] == self.n - self.k + i:
            i -= 1
        if i < 0: self.ok = False
        else:
            self.idx[i] += 1
            for j in range(i + 1, self.k):
                self.idx[j] = self.idx[j - 1] + 1
        return res
    def hasNext(self) -> bool:
        return self.ok