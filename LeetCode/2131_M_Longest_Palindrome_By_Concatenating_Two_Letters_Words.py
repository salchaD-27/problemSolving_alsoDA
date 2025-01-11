# from typing import List
# class Solution:
#     def cons(self, str):
#         ch=str[0]
#         for i in range(len(str)):
#             if(str[i]!=ch): return False
#         return True
#     def allCons(self, words):
#         for i in range(len(words)):
#             if(not self.cons(words[i])): return False
#         return False
#     def longestPalindrome(self, words: List[str]) -> int:
#         if(self.allCons(words)): return max([len(words[i]) for i in range(len(words))])
#         pals=set()
#         for i in range(len(words)):
#             if words[i][::-1] in words: pals.add(words[i])
#         return len("".join(pals))
    

from typing import List
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = {}
        palindrome_length = 0
        middle_used = False
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        for word in words:
            reversed_word = word[::-1]
            if word == reversed_word:
                if word_count[word] > 1:
                    pairs = word_count[word] // 2
                    palindrome_length += pairs * 4
                    word_count[word] -= pairs * 2
                if word_count[word] > 0 and not middle_used:
                    palindrome_length += 2
                    middle_used = True
            elif reversed_word in word_count:
                pairs = min(word_count[word], word_count[reversed_word])
                palindrome_length += pairs * 4
                word_count[word] -= pairs
                word_count[reversed_word] -= pairs
        return palindrome_length