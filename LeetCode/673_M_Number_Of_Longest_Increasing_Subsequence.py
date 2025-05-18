class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        if n == 0: return 0
        length = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]: count[i] += count[j]
        max_len = max(length)
        return sum(c for l, c in zip(length, count) if l == max_len)