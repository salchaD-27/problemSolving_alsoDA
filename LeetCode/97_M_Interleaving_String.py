# from typing import List
# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if(s1=='' and s2=='' and s3==''): return True
#         s1index=0
#         s2index=0
#         s3index=0
#         lastStrChecked=1
#         while(s3index<len(s3)):
#             if(lastStrChecked==1):
#                 if(s3[s3index]==s2[s2index]):
#                     s2index+=1
#                     s3index+=1
#                     lastStrChecked=2
#                 if(s3[s3index]!=s2[s2index] and s3[s3index]!=s1[s1index]): return False
#             if(lastStrChecked==2):
#                 if(s3[s3index]==s1[s1index]):
#                     s1index+=1
#                     s3index+=1
#                     lastStrChecked=1
#                 if(s3[s3index]!=s2[s2index] and s3[s3index]!=s1[s1index]): return False
#         return True
    
from typing import List
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        if(s1=='' and s2=='' and s3==''): return True
    
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]: dp[i][j] = True
                if j > 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]: dp[i][j] = True
        return dp[len(s1)][len(s2)]