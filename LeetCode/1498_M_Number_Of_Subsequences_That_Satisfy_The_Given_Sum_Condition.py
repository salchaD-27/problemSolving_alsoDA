# from typing import List
# from collections import deque
# class Solution:
#     def numSubseq(self, nums: List[int], target: int) -> int:
#         n=len(nums)-1
#         queue=deque()
#         queue.append([str(nums[0]), 0])
#         queue.append(['', 0])
#         res=0
#         while queue:
#             currSubseq,lastAddedIdx=queue.popleft()
#             temp=[int(num) for num in currSubseq]
#             if temp and min(temp)+max(temp)<=target: res+=1
#             if lastAddedIdx==n: continue
#             queue.append([currSubseq+str(nums[lastAddedIdx+1]), lastAddedIdx+1])
#             queue.append([currSubseq, lastAddedIdx+1])
#         return res

from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        n = len(nums)
        res = 0
        left, right = 0, n - 1
        pow2 = [1] * (n)
        for i in range(1, n):
            pow2[i] = pow2[i-1] * 2 % mod
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + pow2[right - left]) % mod
                left += 1
            else: right -= 1
        return res