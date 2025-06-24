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
        
#         count = 0
#         for i in range(len(ages)):
#             age = ages[i]
#             minAge = 0.5 * age + 7
#             if age <= 14: continue
#             lower = binarySearchLessThan(minAge + 1e-9)
#             upper = binarySearchMoreThan(age)
#             # valid range [lower, upper]
#             start = max(lower, upper + 1)
#             totalValid = i - start
#             if totalValid > 0: count += totalValid
#         return count

class Solution(object):
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages:
            count[age] += 1
        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA
        return ans