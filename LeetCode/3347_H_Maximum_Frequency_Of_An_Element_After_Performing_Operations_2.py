from typing import List
from collections import Counter
from bisect import bisect_left,bisect_right
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        arrayValMaxFreq = self.maxFrequencyOfArrayVal(nums, k , numOperations)  # this part implements yesterday's solution to deal with in-array target values
        left = 0 #sliding window solution assuming every element requires an operation:
        otherValMaxFreq = 0
        for right in range(len(nums)): # we adjust the starting point until the sorted subarray is valid
            while nums[right] > nums[left] + 2*k:
                left += 1
            otherValMaxFreq = max(otherValMaxFreq, right - left + 1) #recording current window length
            if otherValMaxFreq >= numOperations: #if the length exceeds the number of operations, we have reached the longest possible window
                otherValMaxFreq = numOperations
                break            
        return max(arrayValMaxFreq, otherValMaxFreq)

    def maxFrequencyOfArrayVal(self, nums, k, numOperations):
        count = Counter(nums) # NB: nums is already sorted
        maxFreq = 0
        for val in count.keys(): # we enumerate the values existing in the original array and deal with them
            left = bisect_left(nums, val - k)
            right = bisect_right(nums, val + k) - 1
            freq = min(right - left + 1, numOperations + count[val])
            maxFreq = max(maxFreq, freq)
        return maxFreq