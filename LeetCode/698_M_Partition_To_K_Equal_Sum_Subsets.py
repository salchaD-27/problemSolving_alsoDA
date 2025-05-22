from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target: return False
        buckets = [0] * k

        def backtrack(index):
            if index == len(nums): return all(b == target for b in buckets)
            for i in range(k):
                if buckets[i] + nums[index] <= target:
                    buckets[i] += nums[index]
                    if backtrack(index + 1): return True
                    buckets[i] -= nums[index]
                if buckets[i] == 0: break
            return False
        return backtrack(0)