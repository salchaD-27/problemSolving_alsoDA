from typing import List
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:    
        def maxSum(L:int, M:int) -> int:
            maxL = ans = 0
            for i in range(L + M, len(prefixSum)):
                maxL = max(maxL, prefixSum[i - M] - prefixSum[i - L - M])
                ans = max(ans, maxL + prefixSum[i] - prefixSum[i - M])
            return ans
        
        prefixSum = [0] * (len(A) + 1)
        for i, a in enumerate(A):
            prefixSum[i + 1] = prefixSum[i] + a
        return max(maxSum(L, M), maxSum(M, L))