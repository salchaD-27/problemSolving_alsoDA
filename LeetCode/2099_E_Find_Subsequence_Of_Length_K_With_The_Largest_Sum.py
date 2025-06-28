# from typing import List
# from collections import deque
# class Solution:
#     def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
#         # subSeq, lastVisitedIdx, count
#         queue=deque()
#         queue.append([str(nums[0]), 0, 1])
#         queue.append(['', 0, 0])
#         res=0
#         while queue:
#             subSeq, lastVisitedIdx, count = queue.popleft()
#             if count>k or lastVisitedIdx==len(nums)-1: continue
#             if count==k: res=max(res, sum([int(num) for num in list(subSeq)]))
#             queue.append([subSeq+str(nums[lastVisitedIdx+1]), lastVisitedIdx+1, count+1])
#             queue.append([subSeq, lastVisitedIdx+1, count+1])
#         return res

from typing import List
from collections import deque
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort(reverse=True, key=lambda x: x[0])
        selected = sorted(indexed_nums[:k], key=lambda x: x[1])
        return [num for num, idx in selected]