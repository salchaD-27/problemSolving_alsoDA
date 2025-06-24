# from typing import List
# class Solution:
#     def numFriendRequests(self, ages: List[int]) -> int:
#         ages.sort(reverse=True)
#         def binarySearchLessThan(target):
#             left, right = 0, len(ages) - 1
#             ans = -1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if ages[mid] < target:
#                     ans = mid
#                     right = mid - 1
#                 else: left = mid + 1
#             return ans
#         def binarySearchMoreThan(target):
#             left, right = 0, len(ages) - 1
#             ans = -1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if ages[mid] > target:
#                     ans = mid
#                     left = mid + 1
#                 else: right = mid - 1
#             return ans

#         first100Idx=0
#         for i in reversed(range(len(ages))):
#             if ages[i]>=100:
#                 first100Idx=i
#                 break
#         count=0
#         for i in range(len(ages)):
#             maxCond1Idx=binarySearchLessThan(0.5*ages[i]+7)
#             maxCond2Idx=binarySearchMoreThan(ages[i])
#             if ages[i]<100: count+=i-min(maxCond1Idx, maxCond2Idx, first100Idx)
#             else: count+=i-min(maxCond1Idx, maxCond2Idx)
#         return count

from typing import List
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort(reverse=True)
        def binarySearchLessThan(target):
            left, right = 0, len(ages) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if ages[mid] < target:
                    ans = mid
                    right = mid - 1
                else: left = mid + 1
            return ans
        def binarySearchMoreThan(target):
            left, right = 0, len(ages) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if ages[mid] > target:
                    ans = mid
                    left = mid + 1
                else: right = mid - 1
            return ans
        
        count = 0
        for i in range(len(ages)):
            age = ages[i]
            minAge = 0.5 * age + 7
            if age <= 14: continue
            lower = binarySearchLessThan(minAge + 1e-9)
            upper = binarySearchMoreThan(age)
            # valid range [lower, upper]
            start = max(lower, upper + 1)
            totalValid = i - start
            if totalValid > 0: count += totalValid
        return count