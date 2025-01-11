#import java.util.Arrays;
#class Solution {
#    private int[] getSliceOfArray(int[] arr, int start, int end) {
#        int[] slice = new int[end - start];
#        for (int i = 0; i < slice.length; i++) {
#            slice[i] = arr[start + i];
#        }
#        return slice;
#    }
#    public int[] recoverArray(int[] nums) {
#        int[] res = new int[nums.length / 2];
#        int[] lower = getSliceOfArray(nums, 0, nums.length / 2);
#        int[] higher = getSliceOfArray(nums, nums.length / 2, nums.length);
#        Arrays.sort(lower);
#        Arrays.sort(higher);
#        for (int i = 0; i < res.length; i++) {res[i] = (lower[i] + higher[i]) / 2;}
#        return res;
#    }
#}

from collections import Counter
from typing import List
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        k = 0
        for i in range(1, n):
            diff = nums[i] - nums[0]
            if diff > 0 and diff % 2 == 0:
                k = diff // 2
                break
        # result array and a frequency map
        res = []
        freq = Counter(nums)
        # valid pairs
        for num in nums:
            if freq[num] == 0: continue
            pair = num + 2 * k
            if freq[pair] > 0:
                res.append(num + k) 
                freq[num] -= 1 
                freq[pair] -= 1
        return res