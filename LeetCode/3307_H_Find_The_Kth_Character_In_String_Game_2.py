# import string
# from typing import List
# class Solution:
#     def kthCharacter(self, k: int, operations: List[int]) -> str:
#         nextChar = {}
#         letters = string.ascii_lowercase  #'abcdefghijklmnopqrstuvwxyz'
#         for i in range(len(letters)):
#             nextChar[letters[i]] = letters[(i + 1) % 26]
#         res='a'
#         i=0
#         while len(res)<k:
#             if operations[i]==1:
#                 tempRes=[nextChar[i] for i in res]
#                 res+=''.join(tempRes)
#             else: res+=res
#             i+=1
#         return res[k-1]

# from typing import List
# class Solution:
#     def kthCharacter(self, k: int, operations: List[int]) -> str:
#         pos = k - 1
#         letter = 'a'
#         for op in reversed(operations):
#             if op == 0: pos //= 2 # str doubled, so orig half
#             else: letter = chr((ord(letter) - ord('a') - 1) % 26 + ord('a')) # this char is nextChar of the orig, reverse nextChar, get prev char
#         return letter

from typing import List
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n, i = 1, 0
        while n < k:
            n *= 2
            i += 1
        d = 0
        while n > 1:
            if k > n // 2:
                k -= n // 2
                d += operations[i - 1]
            n //= 2
            i -= 1
        return chr(d % 26 + ord("a"))