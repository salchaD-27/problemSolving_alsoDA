# from typing import List
# class Solution:
#     def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
#         count = len(startTime)
#         prefixSum = [0] * (count + 1)
#         maxFree = 0
#         for i in range(count):
#             prefixSum[i + 1] = prefixSum[i] + (endTime[i] - startTime[i])
#         for i in range(k - 1, count):
#             occupied = prefixSum[i + 1] - prefixSum[i - k + 1]
#             windowEnd = eventTime if i == count - 1 else startTime[i + 1]
#             windowStart = 0 if i == k - 1 else endTime[i - k]
#             freeTime = windowEnd - windowStart - occupied
#             maxFree = max(maxFree, freeTime)
#         return maxFree

# from typing import List
# class Solution:
#     def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
#         totalBusy = sum(end - start for start, end in zip(startTime, endTime))
#         return max(0, eventTime - totalBusy)

from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        if n == 0: return eventTime
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[n - 1]
        largestRight = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            largestRight[i] = max(largestRight[i + 1], gaps[i + 1])
        maxFree = 0
        largestLeft = 0
        for i in range(1, n + 1):
            duration = endTime[i - 1] - startTime[i - 1]
            canFitLeft = largestLeft >= duration
            canFitRight = largestRight[i] >= duration
            if canFitLeft or canFitRight:
                merged = gaps[i - 1] + gaps[i] + duration
                maxFree = max(maxFree, merged)
            maxFree = max(maxFree, gaps[i - 1] + gaps[i])
            largestLeft = max(largestLeft, gaps[i - 1])
        return maxFree