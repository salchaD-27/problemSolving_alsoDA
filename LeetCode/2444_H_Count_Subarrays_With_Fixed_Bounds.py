#include <stdio.h>
#include <limits.h>
# long long countSubarrays(int* nums, int numsSize, int minK, int maxK) {
#     long long ans = 0;
#     int leftBound = -1, lastMinK = -1, lastMaxK = -1; 
#     for (int i = 0; i < numsSize; i++){if (nums[i] < minK || nums[i] > maxK){leftBound = i;}
#         if (nums[i] == minK){lastMinK = i;}
#         if (nums[i] == maxK){lastMaxK = i;}
#         if (lastMinK != -1 && lastMaxK != -1){ans += (long long)(i - leftBound);}
#     }
#     return ans;
# }

from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        minPos = maxPos = -1
        start = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                start = i
                minPos = maxPos = -1
            if num == minK: minPos = i
            if num == maxK: maxPos = i
            if minPos != -1 and maxPos != -1: count += max(0, min(minPos, maxPos) - start)
        return count