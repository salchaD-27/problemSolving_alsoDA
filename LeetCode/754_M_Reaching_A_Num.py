# class Solution:
#     def reachNumber(self, target: int) -> int:
#         numMoves=target**2
#         reachingMoves=[]
#         def fs(currLoc, currI, count):
#             if currLoc==target: 
#                 reachingMoves.append(count)
#                 return
#             if abs(currLoc-target)==currI: 
#                 reachingMoves.append(count+1)
#                 return
#             if currI>numMoves: return
#             if currI<=numMoves:
#                 fs(currLoc-currI, currI+1, count+1)
#                 fs(currLoc+currI, currI+1, count+1)

#         fs(0, 1, 0)
#         return min(reachingMoves)

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        total = 0
        steps = 0
        while total < target or (total - target) % 2 != 0:
            steps += 1
            total += steps
        return steps