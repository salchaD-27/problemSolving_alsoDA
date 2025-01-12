// class Solution {
//     public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
//         int bagIndex=0;
//         while(additionalRocks!=0 && bagIndex<capacity.length){
//             if(rocks[bagIndex]==capacity[bagIndex]){bagIndex++;}
//             else{
//                 rocks[bagIndex]++;
//                 additionalRocks--;
//             }
//         }
//         int full=0;
//         for(int i=0; i<capacity.length; i++){if(rocks[i]==capacity[i]){full++;}}
//         return full;   
//     }
// }


import java.util.*;
class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int n = capacity.length;
        int[] remainingRocks = new int[n];
        for (int i = 0; i < n; i++){remainingRocks[i] = capacity[i] - rocks[i];}
        Arrays.sort(remainingRocks);
        int fullBags = 0;
        for (int i = 0; i < n; i++) {
            if (additionalRocks >= remainingRocks[i]) {
                additionalRocks -= remainingRocks[i];
                fullBags++;
            }else{break;}
        }
        return fullBags;   
    }
}