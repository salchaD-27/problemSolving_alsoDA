from typing import List
class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        max_word = ''
        def canBuild(word):
            for i in range(1, len(word)):
                if word[:i] not in word_set: return False
            return True
        
        for word in words:
            if canBuild(word):
                if len(word) > len(max_word) or (len(word) == len(max_word) and word < max_word): max_word = word
        return max_word