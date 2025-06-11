from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(path, index):
            if index == len(s):
                res.append(path)
                return
            if s[index].isalpha():
                backtrack(path + s[index].lower(), index + 1)
                backtrack(path + s[index].upper(), index + 1)
            else: backtrack(path + s[index], index + 1)

        backtrack("", 0)
        return res