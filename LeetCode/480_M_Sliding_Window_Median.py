# import heapq
# class Solution:
#     def medianSlidingWindow(self, nums, k):
#         def get_median(max_heap, min_heap, k):
#             if k % 2 == 1: return float(-max_heap[0])
#             else: return (float(-max_heap[0]) + float(min_heap[0])) / 2.0

#         max_heap = []
#         min_heap = []
#         result = []
#         for i in range(len(nums)):
#             if len(max_heap) == 0 or nums[i] <= -max_heap[0]: heapq.heappush(max_heap, -nums[i])
#             else: heapq.heappush(min_heap, nums[i])
#             # balancing heaps
#             if len(max_heap) > len(min_heap) + 1: heapq.heappush(min_heap, -heapq.heappop(max_heap))
#             if len(min_heap) > len(max_heap): heapq.heappush(max_heap, -heapq.heappop(min_heap))
#             if i >= k - 1:
#                 result.append(get_median(max_heap, min_heap, k))
#                 element_to_remove = nums[i - k + 1]
#                 if element_to_remove <= -max_heap[0]:
#                     max_heap.remove(-element_to_remove)
#                     heapq.heapify(max_heap)
#                 else:
#                     min_heap.remove(element_to_remove)
#                     heapq.heapify(min_heap)
#                 # rebalancing heaps
#                 if len(max_heap) > len(min_heap) + 1: heapq.heappush(min_heap, -heapq.heappop(max_heap))
#                 if len(min_heap) > len(max_heap): heapq.heappush(max_heap, -heapq.heappop(min_heap))
#         return result

from sortedcontainers import SortedList
from typing import List
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()
        result = []
        for i in range(len(nums)):
            window.add(nums[i])
            if len(window) > k: window.remove(nums[i - k])
            if len(window) == k:
                if k % 2 == 1: result.append(window[k // 2])
                else: result.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
        return result