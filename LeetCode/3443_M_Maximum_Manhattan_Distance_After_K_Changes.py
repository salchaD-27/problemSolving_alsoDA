# class Solution:
#     def maxDistance(self, s: str, k: int) -> int:
#         def dist(str):
#             x,y,dist=0,0,float('-inf')
#             for i in range(len(str)):
#                 if str[i]=='N': x+=1
#                 elif str[i]=='E': y+=1
#                 elif str[i]=='W': y-=1
#                 elif str[i]=='S': x-=1
#                 dist=max(dist,abs(x)+abs(y))
#             return dist

#         ncount,scount,wcount,ecount=0,0,0,0
#         for i in range(len(s)):
#             if s[i]=='N': ncount+=1
#             elif s[i]=='S': scount+=1
#             elif s[i]=='W': wcount+=1
#             elif s[i]=='E': ecount+=1
#         if ncount>scount:
#             verticalOpposingCount=scount
#             verticalOpposing='S'
#         else: 
#             verticalOpposingCount=ncount
#             verticalOpposing='N'
#         if wcount>ecount:
#             horizOpposingCount=ecount
#             horizOpposing='E'
#         else: 
#             horizOpposingCount=wcount
#             horizOpposing='W'
#         if verticalOpposingCount>horizOpposingCount: toChangeFirst='V'
#         else: toChangeFirst='H'
        
#         newS=''
#         if toChangeFirst=='V':
#             if verticalOpposing=='N':
#                 while k:
#                     for i in range(len(s)):
#                         if s[i]=='N': 
#                             newS+='S'
#                             ncount-=1
#                             k-=1
#                         else: newS+=s[i]
#             else: 
#                 while k:
#                     for i in range(len(s)):
#                         if s[i]=='S': 
#                             newS+='N'
#                             ncount-=1
#                             k-=1
#                         else: newS+=s[i]
#         else:
#             if horizOpposing=='E':
#                 while k:
#                     for i in range(len(s)):
#                         if s[i]=='E': 
#                             newS+='W'
#                             ncount-=1
#                             k-=1
#                         else: newS+=s[i]
#             else: 
#                 while k:
#                     for i in range(len(s)):
#                         if s[i]=='W': 
#                             newS+='E'
#                             ncount-=1
#                             k-=1
#                         else: newS+=s[i]
#         return dist(newS)

# from functools import lru_cache
# class Solution:
#     def maxDistance(self, s: str, k: int) -> int:
#         directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

#         @lru_cache(maxsize=None)
#         def dfs(i, x, y, k_left):
#             if i == len(s): return abs(x) + abs(y)
#             res = 0
#             # no change
#             dx, dy = directions[s[i]]
#             res = max(res, dfs(i + 1, x + dx, y + dy, k_left))
#             # change
#             if k_left > 0:
#                 for d, (dx, dy) in directions.items():
#                     if d != s[i]: res = max(res, dfs(i + 1, x + dx, y + dy, k_left - 1))
#             return res

#         return dfs(0, 0, 0, k)

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = north = south = east = west = 0
        for i in range(len(s)):
            c = s[i]
            if c == 'N': north += 1
            elif c == 'S': south += 1
            elif c == 'E': east += 1
            elif c == 'W': west += 1
            x = abs(north - south)
            y = abs(east - west)
            MD = x + y
            dis = MD + min(2 * k, i + 1 - MD)
            ans = max(ans, dis)
        return ans