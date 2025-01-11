# from typing import List

# class Solution:
#     def getAverages(self, nums: List[int], k: int) -> List[int]:
#         if len(nums) < (2 * k + 1): return [-1] * len(nums)
#         avg=[]
#         avg.extend([-1] * k)
#         for i in range(k, len(nums) - k):
#             avg.append(sum(nums[i - k:i + k + 1])//len(nums[i - k:i + k + 1]))
#         avg.extend([-1] * k)
#         return avg


from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        if n < window_size: return [-1]*n
        
        avg = [-1] * n
        window_sum = sum(nums[:window_size - 1])
        for i in range(k, n - k):
            window_sum += nums[i + k]
            avg[i] = window_sum // window_size
            window_sum -= nums[i - k]
        return avg