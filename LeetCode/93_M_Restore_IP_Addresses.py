# from typing import List
# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         a=1
#         b=2
#         c=3
#         ans=[]
#         while(a<len(s)-2):
#             while(b<len(s)-1):
#                 while(c<len(s)):
#                     temp=[int(s[:a]), int(s[a:b]), int(s[b:c]), int(s[c:])]
#                     flag=True
#                     for num in temp:
#                         if (num<0 or num>255):
#                             flag=False
#                             break
#                     if(flag): ans.append(".".join(str(temp)))
#                     c+=1
#                 b+=1
#             a+=1
#         return ans

from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment: str) -> bool: return 0 <= int(segment) <= 255 and (segment == "0" or segment[0] != "0")
        
        n = len(s)
        ans = []
        for a in range(1, min(4, n - 2)):
            for b in range(a + 1, min(a + 4, n - 1)):
                for c in range(b + 1, min(b + 4, n)):
                    part1 = s[:a]
                    part2 = s[a:b]
                    part3 = s[b:c]
                    part4 = s[c:]
                    if is_valid(part1) and is_valid(part2) and is_valid(part3) and is_valid(part4): ans.append(f"{part1}.{part2}.{part3}.{part4}")
        return ans