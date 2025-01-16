# from typing import List
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         ans=''
#         for i in range(len(s)):
#             j=i
#             while(True):
#                 if(j+2*(j - 1)-1 < len(s)-1): j+=2*(j - 1)-1
#                 else: break
#                 ans+=s[j]
#         return ans
    


from typing import List
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        ans = ''
        for i in range(numRows):
            j = i
            while j < len(s):
                ans += s[j]
                if i != 0 and i != numRows - 1:
                    zigzag_index = j + (numRows - i - 1) * 2
                    if zigzag_index < len(s): ans += s[zigzag_index]
                j += (numRows - 1) * 2
        return ans