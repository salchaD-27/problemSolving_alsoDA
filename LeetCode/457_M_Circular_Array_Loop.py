# from typing import List
# class Solution:
#     def circularArrayLoop(self, nums: List[int]) -> bool:
#         n = len(nums)
#         def next_index(i): return (i + nums[i]) % n

#         for i in range(n):
#             if nums[i] == 0: continue
#             direction = nums[i] > 0
#             slow = i
#             fast = i
#             while True:
#                 next_slow = next_index(slow)
#                 next_fast = next_index(fast)
#                 if (nums[fast] > 0) != direction or nums[fast] == 0: break
#                 if (nums[next_fast] > 0) != direction or nums[next_fast] == 0: break
#                 next_fast = next_index(next_fast)
#                 if (nums[next_fast] > 0) != direction or nums[next_fast] == 0: break
#                 if slow == next_slow: break
#                 if fast == next_fast: break
#                 slow = next_slow
#                 fast = next_fast
#                 if slow == fast: return True
#             index = i
#             while nums[index] != 0 and (nums[index] > 0) == direction:
#                 next_i = next_index(index)
#                 nums[index] = 0
#                 index = next_i
#         return False
    
class Solution(object):
    def circularArrayLoop(self, nums):
        if not nums or len(nums) < 2: return False
        n = len(nums)
        for i in range(n):           
            if type(nums[i]) != int: continue
            if nums[i] % n == 0: continue
            direction = (nums[i] > 0)
            mark = str(i)
            while (type(nums[i]) == int) and (direction ^ (nums[i] < 0)) and (nums[i] % n != 0):
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % n
            if nums[i] == mark: return True    
        return False