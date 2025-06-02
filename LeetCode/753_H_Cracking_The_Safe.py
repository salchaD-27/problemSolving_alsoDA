# n=3 k=4
# _   _   _
# 0-3 0-3 0-3

# from itertools import product
# class Solution:
#     def crackSafe(self, n: int, k: int) -> str:
#         nums=[i for i in range(k)]
#         passwords=list(product(nums, repeat=n))
#         minStr,minStrLen='',float('inf')

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()
        result = []
        def dfs(node):
            for x in range(k):
                neighbor = node + str(x)
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor[1:])
                    result.append(str(x))

        start = "0" * (n - 1)
        dfs(start)
        return start + ''.join(reversed(result))