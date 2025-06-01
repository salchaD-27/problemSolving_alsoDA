# from itertools import product
# class Solution:
#     def distributeCandies(self, n: int, limit: int) -> int:
#         nums=[i for i in range(limit+1)]
#         prods=list(product(nums, repeat=3))
#         count=0
#         for i in range(len(prods)):
#             if sum(prods[i])==n: count+=1
#         return count

# class Solution:
#     def distributeCandies(self, n: int, limit: int) -> int:
#         count = 0
#         for x in range(min(n, limit) + 1):
#             for y in range(min(n - x, limit) + 1):
#                 z = n - x - y
#                 if 0 <= z <= limit: count += 1
#         return count

class Solution(object):
    def distributeCandies(self, n, limit):
        res = 0
        for i in range(min(limit, n) + 1):
            if n - i <= 2 * limit: res += min(n - i, limit) - max(0, n - i - limit) + 1
        return res