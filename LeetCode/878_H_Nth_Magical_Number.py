# from math import gcd
# class Solution:
#     def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
#         MOD = 10**9 + 7
#         i = j = 1
#         count = 0
#         num = 0
#         while count < n:
#             nextA = i * a
#             nextB = j * b
#             if nextA < nextB:
#                 num = nextA
#                 i += 1
#             elif nextB < nextA:
#                 num = nextB
#                 j += 1
#             else:
#                 num = nextA
#                 i += 1
#                 j += 1
#             count += 1
#         return num % MOD

from math import gcd
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        lcm = a * b // gcd(a, b)
        left, right = 1, n * min(a, b)
        while left < right:
            mid = (left + right) // 2
            count = mid // a + mid // b - mid // lcm
            if count < n: left = mid + 1
            else: right = mid
        return left % MOD