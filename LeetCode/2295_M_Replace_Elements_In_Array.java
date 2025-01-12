// class Solution {
//     public int[] arrayChange(int[] nums, int[][] operations) {
//         for(int i=0; i<operations.length; i++){
//             for(int j=0; j<nums.length; j++){
//                 if(nums[j]==operations[i][0]){
//                     nums[j]=operations[i][1];
//                     break;
//                 }
//             }
//         }
//         return nums;
//     }
// }

import java.util.HashMap;
class Solution {
    public int[] arrayChange(int[] nums, int[][] operations) {
        HashMap<Integer, Integer> valueToIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++){valueToIndex.put(nums[i], i);}
        for (int[] op : operations) {
            int oldVal = op[0];
            int newVal = op[1];
            if (valueToIndex.containsKey(oldVal)) {
                int index = valueToIndex.get(oldVal);
                nums[index] = newVal;
                valueToIndex.put(newVal, index); 
                valueToIndex.remove(oldVal); 
            }
        }
        return nums;
    }
}