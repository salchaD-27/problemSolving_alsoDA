# from typing import List
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         def countCont(s, char):
#             firstOcc = 0
#             for i in range(len(s)):
#                 if s[i] == char: 
#                     firstOcc = i
#                     break
#             count = 0
#             for j in range(i, len(s)):
#                 if s[j] == char:
#                     count += 1
#                 else:
#                     break
#             return count

#         def casIter(s):
#             i = 0
#             ans = ''
#             while i < len(s):
#                 count = countCont(s, s[i])
#                 char = s[i]
#                 ans += str(count)
#                 ans += char
#                 i += count
#             return ans
        
#         ansStr = '1'
#         for i in range(1, n):
#             ansStr = casIter(ansStr)

#         return ansStr

from typing import List
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(1, n):
            next_result = []
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                next_result.append(str(count) + result[i])
                i += 1
            result = ''.join(next_result)
        return result