# from typing import List
# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool:
#         if(len(matchsticks)<4): return False
#         matchsticks.sort()
#         L=0
#         R=len(matchsticks)-1
#         while(L<R):
#             if(sum(matchsticks[:L+1])>sum(matchsticks[R:])): R-=1
#             if(sum(matchsticks[:L+1])<sum(matchsticks[R:])): L+=1
#             else: 
#                 L+=1
#                 R-=1
#         if(sum(matchsticks[:L+1])==sum(matchsticks[R:])): return True
#         return False

from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4: return False
        total = sum(matchsticks)
        if total % 4 != 0: return False
        side = total // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        
        def dfs(index):
            if index == len(matchsticks): return sides[0] == sides[1] == sides[2] == sides[3] == side
            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1): return True
                    sides[i] -= matchsticks[index]
            return False

        return dfs(0)