# from itertools import permutations as perm
# class Solution:
#     def countArrangement(self, n: int) -> int:
#         count=0
#         perms=list(perm([i for i in range(1, n+1)]))
#         for i in range(len(perms)):
#             flag=True
#             for j in range(len(perms[i])):
#                 if not (perms[i][j]%(j+1)==0 or (j+1)%perms[i][j]==0): flag=False
#             if(flag): count+=1
#         return count

class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(pos, visited):
            if pos > n: return 1
            count = 0
            for i in range(1, n + 1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = True
                    count += backtrack(pos + 1, visited)
                    visited[i] = False
            return count
        visited = [False] * (n + 1)
        return backtrack(1, visited)