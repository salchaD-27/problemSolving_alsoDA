# class Solution:
#     def isValid(self, word: str) -> bool:
#         if len(word)<3: return False
#         oneVowel=oneCons=False
#         for char in word:
#             if char not in '0123456789' or char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ': return False
#             if char in 'aeiouAEIOU': oneVowel=True
#             elif char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ': oneCons=True
#         return oneVowel and oneCons

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        oneVowel = False
        oneCons = False
        for char in word:
            if not (char.isdigit() or char.isalpha()): return False
            if char in 'aeiouAEIOU': oneVowel = True
            elif char.isalpha(): oneCons = True
        return oneVowel and oneCons