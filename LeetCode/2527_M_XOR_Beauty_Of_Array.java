class Solution {
    public int xorBeauty(int[] nums) {
        int result = 0;
        for (int num : nums){result ^= num;}
        return result;
    }
}