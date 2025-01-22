# from typing import List
# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         nums=[i for i in range(1, n+1)]
#         def generate_permutations(current, remaining):
#             if not remaining: return [current]
#             permutations = []
#             for i in range(len(remaining)):
#                 num = remaining[i]
#                 new_remaining = remaining[:i] + remaining[i+1:]
#                 permutations.extend(generate_permutations(current + [num], new_remaining))
#             return permutations
#         def pattern(n):
#             numbers = list(range(1, n + 1))
#             return generate_permutations([], numbers)
#         patterns=pattern(len(nums))
#         ans=[]
#         for pat in patterns:
#             ans.append([nums[num-1] for num in pat])
#         kthSeq=''
#         for num in ans[k-1]:
#             kthSeq+=str(num)
#         return kthSeq


from typing import List
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [math.factorial(i) for i in range(n)]
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        result = []
        for i in range(n - 1, -1, -1):
            index = k // factorial[i]
            result.append(nums.pop(index))
            k %= factorial[i]
        return ''.join(result)