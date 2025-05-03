# from typing import List
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         crossTrue=False
#         for i in range(len(isConnected)):
#             for j in range(len(isConnected[i])):
#                 if(isConnected[i][j]==1):
#                     if(i!=j):
#                         isConnected[i][i]='T'
#                         isConnected[j][j]='T'
#                         crossTrue=True
#         if not crossTrue: return len(isConnected)
#         else:
#             count=0
#             for i in range(len(isConnected)):
#                 for j in range(len(isConnected[i])):
#                     if(isConnected[i][j]=='T'): count+=1
#             return count

from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        
        n = len(isConnected)
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1
        return count