# 1 2 3  4  5  6  7
# 1 1 1  0  2  1  1
# 1 3 6 10 15 21 28
# 6

# 1 3 5
# 1 1 2
# 1 4 9
# 4

# from typing import List
# class Solution:
#     def numOfSubarrays(self, arr: List[int]) -> int:
#         dp=[0]*len(arr)
#         prefixSum=[]
#         for num in arr:
#             if(not prefixSum): prefixSum.append(num)
#             prefixSum.append(prefixSum[-1]+num)
#         for i in range(len(dp)):
#             # Both num and prefixSum odd
#             if(arr[i]%2!=0 and prefixSum[i]%2!=0): dp[i]=2
#             # Num odd but prefixSum even, or, num even, prefixSum odd
#             elif((arr[i]%2!=0 and prefixSum[i]%2==0) or (arr[i]%2==0 and prefixSum[i]%2!=0)): dp[i]=1
#             # Both num and prefixSum even
#             else: dp[i]=0
#         return sum(dp)
    
from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1
        prefix_sum = 0
        result = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                result += odd_count
                even_count += 1
            else:
                result += even_count
                odd_count += 1
            result %= MOD
        return result