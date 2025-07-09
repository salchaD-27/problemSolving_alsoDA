# from typing import List
# class Solution:
#     def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
#         def delete(total: list, remove: list) -> list:
#             x, y = remove
#             result = []
#             for start, end in total:
#                 if end < x or start > y: result.append([start, end]) # no overlap
#                 else:
#                     # partial/full overlap
#                     if start < x: result.append([start, x - 1])
#                     if end > y: result.append([y + 1, end])
#             return result

#         total=[[0,eventTime]]
#         for i in range(len(startTime)):
#             total=delete(total, [startTime[i],endTime[i]])
#         totalLen=[tot[1]-tot[0]+1 for tot in total]
#         totalLen.sort(reverse=True)
#         return sum(totalLen[:k])

from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        count = len(startTime)
        prefixSum = [0] * (count + 1)
        maxFree = 0
        for i in range(count):
            prefixSum[i + 1] = prefixSum[i] + (endTime[i] - startTime[i])
        for i in range(k - 1, count):
            occupied = prefixSum[i + 1] - prefixSum[i - k + 1]
            windowEnd = eventTime if i == count - 1 else startTime[i + 1]
            windowStart = 0 if i == k - 1 else endTime[i - k]
            freeTime = windowEnd - windowStart - occupied
            maxFree = max(maxFree, freeTime)
        return maxFree