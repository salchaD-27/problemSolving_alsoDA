# nums1 = [3,4,6,5]
# nums2 = [9,1,2,5,8,3]
# k = 5
# [_ _ _ _] [_ _ _ _ _ _]
# (1) _   6 5 _ 
# (2) 9 8 _ _ 3
#     9 8 6 5 3

# 1. start for first index of final number to be formed
# 2. for firt index, pick greater num of two given nums array
# (Add this to intermediate arr specified for respective num, i.e if greater value for ith index coming from nums1, then add to k1[i] else to k2[i])
# 3. move to next index, pick greater num of two given nums array
# (If this value is bigger than either k1[i-1] or k2[i-1] then alter to maintain monotonic stack for both)
# (If value is coming from nums1, and k1[i-1] is -1 (i.e no value was at that index taken from nums1) then check for k2, if greater than k2[i-1], shift the indexes for both)
# (In cases where values disobey monotnic stack within same intermediate array, we delete them, else for cross arrays, we just shift)
# 4. repeat for further indexes, by contiously poppying greater element from nums1[0] or nums2[0] and adding to k1[i] or k2[i] resp
# 5. when both nums1 and nums2 are empty, then k1 and k2 will be merged for final result
# 6. starting from first index, at every index, there will be value in either k1[i] or k2[i], take where val!=-1 and form the final result
# 7. return this final result

from typing import List
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxSingleNumber(nums, k):
            stack = []
            to_pop = len(nums) - k
            for num in nums:
                while to_pop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)
            return stack[:k]

        def merge(nums1, nums2):
            result = []
            while nums1 or nums2:
                if nums1 > nums2: result.append(nums1.pop(0))
                else: result.append(nums2.pop(0))
            return result

        max_result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            temp1 = maxSingleNumber(nums1, i)
            temp2 = maxSingleNumber(nums2, k - i)
            combined = merge(temp1, temp2)
            if combined > max_result: max_result = combined
        return max_result