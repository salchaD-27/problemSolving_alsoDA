from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        result = []
        def backtrack(start, path):
            if start == len(s):
                result.append(" ".join(path))
                return
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet: backtrack(end, path + [word])
        backtrack(0, [])
        return result