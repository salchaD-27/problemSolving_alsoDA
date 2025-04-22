# class Solution:
#     def idealArrays(self, n: int, maxValue: int) -> int:
#         count = 0
#         MOD = 10**9 + 7

#         def formArr(currArr):
#             nonlocal count
#             if len(currArr) == n:
#                 count = (count + 1) % MOD
#                 return
#             last_elem = currArr[-1]
#             for i in range(1, maxValue + 1):
#                 if i % last_elem == 0: formArr(currArr + [i])
#         for i in range(1, maxValue + 1):
#             formArr([i])
#         return count

# class Solution:
#     def idealArrays(self, n: int, maxValue: int) -> int:
#         MOD = 10**9 + 7
#         dp = [0] * (maxValue + 1)
#         for i in range(1, maxValue + 1):
#             dp[i] = 1
#         for _ in range(2, n + 1):
#             new_dp = [0] * (maxValue + 1)
#             for i in range(1, maxValue + 1):
#                 for j in range(i, maxValue + 1, i):
#                     new_dp[j] = (new_dp[j] + dp[i]) % MOD
#             dp = new_dp
#         return sum(dp) % MOD

MOD = 10**9 + 7
MAX_N = 10**4 + 10
MAX_P = 15
sieve = [0] * MAX_N
for i in range(2, MAX_N):
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            sieve[j] = i
ps = [[] for _ in range(MAX_N)]
for i in range(2, MAX_N):
    x = i
    while x > 1:
        p = sieve[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        ps[i].append(cnt)
c = [[0] * (MAX_P + 1) for _ in range(MAX_N + MAX_P)]
c[0][0] = 1
for i in range(1, MAX_N + MAX_P):
    c[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        for x in range(1, maxValue + 1):
            mul = 1
            for p in ps[x]:
                mul = mul * c[n + p - 1][p] % MOD
            ans = (ans + mul) % MOD
        return ans