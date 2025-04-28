from typing import List
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s, t):
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]: i += 1
                j += 1
            return i == len(s)

        strs.sort(key=lambda x: -len(x))
        for i in range(len(strs)):
            is_uncommon = True
            for j in range(len(strs)):
                if i != j and isSubsequence(strs[i], strs[j]):
                    is_uncommon = False
                    break
            if is_uncommon: return len(strs[i])
        return -1