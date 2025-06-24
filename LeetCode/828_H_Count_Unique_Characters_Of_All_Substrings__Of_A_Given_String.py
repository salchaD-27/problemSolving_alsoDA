class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {}
        for i, c in enumerate(s):
            if c not in index: index[c] = [-1] #padding
            index[c].append(i)
        for c in index:
            index[c].append(len(s)) #padding
        res = 0
        for positions in index.values():
            for i in range(1, len(positions) - 1):
                prev = positions[i - 1]
                curr = positions[i]
                next_ = positions[i + 1]
                res += (curr - prev) * (next_ - curr)
        return res