# from typing import List
# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:
#         def leftOf(currCode): return str(int(currCode)-1)
#         def topOf(currCode): return str(int(currCode)-100)

#         targetCounts=[]
#         def bfs(lastCode, count):
#             if lastCode=='0001' or lastCode=='0100': 
#                 targetCounts.append(count+1)
#                 return
#             # left possible
#             if lastCode[-1]!='0': 
#                 leftCode=leftOf(lastCode)
#                 if leftCode not in deadends: bfs(leftCode, count+1)
#             # top possible
#             if lastCode[0]!='0' and lastCode[1]!='0':
#                 topCode=topOf(lastCode)
#                 if topCode not in deadends: bfs(topCode, count+1)
#             return
#         return min(targetCounts) if targetCounts else -1

# from typing import List
# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:
#         targetCounts=[]
#         def bfs(lastCode, count):
#             codeDigits=[int(i) for i in lastCode]
#             neighbours=[]
#             for i in range(len(codeDigits)):
#                 tempStrN, tempStrP='', ''
#                 for j in range(len(codeDigits)):
#                     if i==j:
#                         tempStrN+=str(codeDigits[j]-1)
#                         tempStrP+=str(codeDigits[j]+1)
#                     else: 
#                         tempStrN+=str(codeDigits[j])
#                         tempStrP+=str(codeDigits[j])
#                 neighbours.append(tempStrN)
#                 neighbours.append(tempStrP)

#             if '0000' in neighbours: 
#                 targetCounts.append(count+1)
#                 return
#             for neighbour in neighbours:
#                 if neighbour not in deadends: bfs(neighbour, count+1)
#         return min(targetCounts) if targetCounts else -1

from typing import List
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead: return -1
        visited = set("0000")
        queue = deque([("0000", 0)])
        while queue:
            code, steps = queue.popleft()
            if code == target: return steps
            codeDigits = [int(c) for c in code]
            for i in range(4):
                for diff in [-1, 1]:
                    newDigits = codeDigits[:]
                    newDigits[i] = (newDigits[i] + diff) % 10
                    newCode = ''.join(str(d) for d in newDigits)
                    if newCode not in visited and newCode not in dead:
                        visited.add(newCode)
                        queue.append((newCode, steps + 1))
        return -1