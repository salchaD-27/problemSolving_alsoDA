// import java.lang.Math;
// class Solution {
//     public int sumTo(int[] nums, int index) {
//         int sum = 0;
//         for (int i = 0; i <= index; i++){sum += nums[i];}
//         return sum;
//     }
//     public int sumFrom(int[] nums, int index) {
//         int sum = 0;
//         for (int i = index + 1; i < nums.length; i++){sum += nums[i];}
//         return sum;
//     }
//     public int minimumAverageDifference(int[] nums) {
//         int minVal = Integer.MAX_VALUE, minIndex = Integer.MAX_VALUE;
//         for (int i = 0; i < nums.length; i++) {
//             int diff = Math.abs((sumTo(nums, i) / (i + 1)) - ((nums.length - i - 1) == 0 ? 0 : (sumFrom(nums, i) / (nums.length - i - 1))));
//             if (diff < minVal || (diff == minVal && i < minIndex)) {
//                 minVal = diff;
//                 minIndex = i;
//             }
//         }
//         return minIndex;
//     }
// }

import java.lang.Math;
class Solution {
    public int minimumAverageDifference(int[] nums) {
        int n = nums.length;
        long totalSum = 0;
        for (int num:nums){totalSum += num;}
        long leftSum = 0;
        long minDiff = Long.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < n; i++) {
            leftSum += nums[i];
            long leftAvg = leftSum / (i + 1);
            long rightSum = totalSum - leftSum;
            long rightAvg = (n - i - 1) == 0 ? 0 : rightSum / (n - i - 1);
            long diff = Math.abs(leftAvg - rightAvg);
            if (diff < minDiff) {
                minDiff = diff;
                minIndex = i;
            }
        }
        return minIndex;
    }
}