# func max(nums []int, L int, R int) int {
# 	ans := nums[L]
# 	for i := L; i <= R; i++ {
# 		if nums[i] > ans {
# 			ans = nums[i]
# 		}
# 	}
# 	return ans
# }
# func maxSlidingWindow(nums []int, k int) []int {
# 	ans := make([]int, 0)
# 	L := 0
# 	R := k - 1
# 	for R < len(nums) {
# 		ans = append(ans, max(nums, L, R))
# 		L++
# 		R++
# 	}
# 	return ans
# }

# from typing import List
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         def bufferIndex(nums, l, r): return [i for i in range(l, r+1) if nums[i] == max(nums[l:r+1])][0]
#         ans=[]
#         lastMax=max(nums[0:k])
#         ans.append(lastMax)
#         buffer=bufferIndex(nums, 0, k-1)
#         L,R=1,k
#         while(R<len(nums)):
#             if(nums[R]<lastMax and buffer):
#                 ans.append(lastMax)
#                 buffer-=1
#             else:
#                 lastMax=max(nums[L:R+1])
#                 buffer=bufferIndex(nums, L, R)
#                 ans.append(lastMax)
#             L+=1
#             R+=1
#         return ans

from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1: dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1: ans.append(nums[dq[0]])
        return ans