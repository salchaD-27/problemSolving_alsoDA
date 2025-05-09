# class Solution:
#     def countBalancedPermutations(self, num: str) -> int:
#         MOD=10**9+7
#         def splitIntoEqualSumSubsets(nums: List[int]) -> List[List[int]]:
#             total = sum(nums)
#             if total % 2 != 0: return []
#             target = total // 2
#             n = len(nums)
#             memo = {}

#             def backtrack(i, current_sum):
#                 if (i, current_sum) in memo: return None
#                 if current_sum == target: return []
#                 if current_sum > target or i >= n: return None
#                 # with nums[i]
#                 with_curr = backtrack(i + 1, current_sum + nums[i])
#                 if with_curr is not None: return [nums[i]] + with_curr
#                 # without nums[i]
#                 without_curr = backtrack(i + 1, current_sum)
#                 memo[(i, current_sum)] = None
#                 return without_curr

#             subset = backtrack(0, 0)
#             if subset is None: return []
#             used = subset.copy()
#             remaining = []
#             used_counts = {}
#             for x in used:
#                 used_counts[x] = used_counts.get(x, 0) + 1
#             for x in nums:
#                 if used_counts.get(x, 0): used_counts[x] -= 1
#                 else: remaining.append(x)
#             return [subset, remaining]

#         nums=[int(i) for i in num]
#         groups=splitIntoEqualSumSubsets(nums)
#         if len(groups)<2: return 0
#         return (len(set(groups[0]))*len(set(groups[1])))%MOD

class Solution(object):
    def countBalancedPermutations(self, num):
        mod = 10**9+7
        n = len(num)
        total = sum(int(c) for c in num)
        if total % 2: return 0
        fact = [1]*(n+1)
        inv = [1]*(n+1)
        invFact = [1]*(n+1)
        for i in range(1,n+1): fact[i] = fact[i-1]*i % mod
        for i in range(2,n+1): inv[i] = mod - (mod//i)*inv[mod%i] % mod
        for i in range(1,n+1): invFact[i] = invFact[i-1]*inv[i] % mod
        halfSum = total//2
        halfLen = n//2
        dp = [[0]*(halfLen+1) for _ in range(halfSum+1)]
        dp[0][0] = 1
        digits = [0]*10
        for c in num:
            d = int(c)
            digits[d] += 1
            for i in range(halfSum, d-1, -1):
                for j in range(halfLen, 0, -1):
                    dp[i][j] = (dp[i][j] + dp[i-d][j-1]) % mod
        res = dp[halfSum][halfLen]
        res = res * fact[halfLen] % mod * fact[n-halfLen] % mod
        for cnt in digits: res = res * invFact[cnt] % mod
        return res