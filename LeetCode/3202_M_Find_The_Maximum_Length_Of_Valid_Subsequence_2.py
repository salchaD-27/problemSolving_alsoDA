from typing import List
class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        # tracking rem transitions
        dp = [[0] * k for _ in range(k)]  # dp[prev_rem][curr_rem]
        maxLength = 0
        for num in nums:
            current_rem = num % k
            for prev_rem in range(k):
                # if transition poss
                dp[prev_rem][current_rem] = dp[current_rem][prev_rem] + 1
                maxLength = max(maxLength, dp[prev_rem][current_rem])
        return maxLength