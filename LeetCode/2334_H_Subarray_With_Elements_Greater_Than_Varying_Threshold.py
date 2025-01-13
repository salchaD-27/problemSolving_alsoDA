# from typing import List
# class Solution:
#     def validSubarraySize(self, nums: List[int], threshold: int) -> int:
#         n = len(nums)
#         def isValid(k: int) -> bool:
#             for i in range(n - k + 1):
#                 if all(num > threshold / k for num in nums[i:i + k]): return True
#             return False

#         for k in range(1, n + 1):
#             if isValid(k): return k        
#         return -1


from typing import List
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = [-1] * n 
        right = [n] * n 
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack: left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack: right[i] = stack[-1]
            stack.append(i)
        for i in range(n):
            k = right[i] - left[i] - 1
            if nums[i] > threshold / k: return k
        return -1