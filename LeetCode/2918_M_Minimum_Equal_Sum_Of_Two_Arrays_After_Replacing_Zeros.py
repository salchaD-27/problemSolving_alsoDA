# from typing import List
# class Solution:
#     def minSum(self, nums1: List[int], nums2: List[int]) -> int:
#         sum1, zeros1 = sum(x for x in nums1 if x != 0), nums1.count(0)
#         sum2, zeros2 = sum(x for x in nums2 if x != 0), nums2.count(0)
#         min_sum1 = sum1 + zeros1
#         min_sum2 = sum2 + zeros2
#         if min_sum1 == min_sum2: return min_sum1
#         if min_sum1 < min_sum2:
#             max_possible = min_sum1 + 9 * zeros1
#             if max_possible >= min_sum2: return min_sum2
#             else: return -1
#         else:
#             max_possible = min_sum2 + 9 * zeros2
#             if max_possible >= min_sum1: return min_sum1
#             else: return -1

class Solution(object):
    def minSum(self, nums1, nums2):
        sum1, sum2 = 0, 0
        zeros1, zeros2 = 0, 0
        for num in nums1:
            if num == 0: zeros1 += 1
            sum1 += num
        for num in nums2:
            if num == 0: zeros2 += 1
            sum2 += num
        if zeros1 == 0 and zeros2 == 0: return sum1 if sum1 == sum2 else -1
        elif zeros1 == 0: return sum1 if sum2 + zeros2 <= sum1 else -1
        elif zeros2 == 0: return sum2 if sum1 + zeros1 <= sum2 else -1
        return max(sum1 + zeros1, sum2 + zeros2)