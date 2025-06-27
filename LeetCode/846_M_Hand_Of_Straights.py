# from typing import List
# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         if len(hand)%groupSize!=0: return False
#         hand.sort()
#         groupsToFulfill=len(hand)//groupSize
#         while groupsToFulfill:
#             firstNum=hand.pop(0)
#             for i in range(groupSize-1):
#                 if firstNum+i not in hand: return False
#                 hand.remove(firstNum+i)
#             groupsToFulfill-=1
#         return True

import heapq
from typing import List
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for i in range(groupSize):
                num = first + i
                if count[num] == 0: return False
                count[num] -= 1
                if count[num] == 0:
                    if num != min_heap[0]: return False
                    heapq.heappop(min_heap)
        return True