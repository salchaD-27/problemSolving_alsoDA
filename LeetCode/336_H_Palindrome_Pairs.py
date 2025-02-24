# from typing import List
# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         res=[]
#         for i in range(len(words)):
#             for j in range(len(words)):
#                 if(i==j): continue
#                 temp=words[i]+words[j]
#                 if(temp==temp[::-1]): res.append([i,j])
#         return res

from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_dict = {word: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                # Suffix is a palindrome, and the reversed prefix exists in the list
                if suffix == suffix[::-1]:  
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_dict and word_dict[reversed_prefix] != i: res.append([i, word_dict[reversed_prefix]])                
                # Prefix is a palindrome, and the reversed suffix exists in the list
                if j > 0 and prefix == prefix[::-1]:
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_dict and word_dict[reversed_suffix] != i: res.append([word_dict[reversed_suffix], i])
        return res