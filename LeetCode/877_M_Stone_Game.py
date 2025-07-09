# from typing import List
# from collections import deque
# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         queue = deque()
#         queue.append((piles[0], 0, 'A', piles[1:]))
#         queue.append((piles[-1], 0, 'A', piles[:-1]))
#         win = False
#         while queue:
#             aliceScore, bobScore, lastTurn, leftPiles = queue.popleft()
#             if not leftPiles:
#                 if aliceScore > bobScore: win = True
#                 continue
#             if lastTurn == 'A':
#                 queue.append((aliceScore, bobScore + leftPiles[0], 'B', leftPiles[1:]))
#                 queue.append((aliceScore, bobScore + leftPiles[-1], 'B', leftPiles[:-1]))
#             else:
#                 queue.append((aliceScore + leftPiles[0], bobScore, 'A', leftPiles[1:]))
#                 queue.append((aliceScore + leftPiles[-1], bobScore, 'A', leftPiles[:-1]))
#         return win

from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # in even len optimal play with odd total sum, first player always wins
        return True