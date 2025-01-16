# from typing import List
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if(s==''): return 0
#         if(s==' '): return 1
#         ans=0
#         for i in range(len(s)):
#             temp=''
#             L=i
#             R=i
#             for j in range(i+1, len(s)):
#                 if(s[j] not in temp): 
#                     R+=1
#                     temp+=s[j]
#                 else: break
#             tempSum=R-L
#             ans=max(ans, tempSum)
#         return ans

from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s==''): return 0
        if(s==' '): return 1
        ans = 0
        for i in range(len(s)):
            temp = ''
            L = i
            R = i
            for j in range(i, len(s)):
                if s[j] not in temp:
                    R = j 
                    temp += s[j]
                else:
                    break
            tempSum = R - L + 1 
            ans = max(ans, tempSum)
        return ans
