# from typing import List
# class Solution:
#     def minimumLengthEncoding(self, words: List[str]) -> int:
#         words.sort(reverse=True)
#         s=[words[0]]
#         for i in range(1, len(words)):
#             lastWord,currWord=s[-1],words[i]
#             if len(lastWord)>=len(currWord) and lastWord[-len(currWord):]==currWord: continue
#             else: s.append(words[i])
#         totalLen=0
#         for i in range(len(s)):
#             totalLen+=len(s[i])+1
#         return totalLen

from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        for word in list(words):
            for i in range(1, len(word)):
                words.discard(word[i:])
        return sum(len(word) + 1 for word in words)