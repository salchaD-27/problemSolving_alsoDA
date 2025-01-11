// class Solution {
//     public int minOfSubarr(int[] arr, int L, int R){
//         if(L==R){return arr[L];}
//         int min=arr[L];
//         for(int i=L; i<=R; i++){
//             if(arr[i]<min){
//                 min=arr[i];
//             }
//         }
//         return min;
//     }
//     public int sumOfSubarr(int[] arr, int L, int R){
//         int sum=0;
//         for(int i=L; i<=R; i++){
//             sum+=arr[i];
//         }
//         return sum;
//     }
//     public int totalStrength(int[] strength){
//         int totalStr=0;
//         for(int i=0; i<strength.length; i++){
//             int L=i, R=i;
//             for(int j=i; j<strength.length; j++){
//                 totalStr+=minOfSubarr(strength, L, R)*sumOfSubarr(strength, L, R);
//                 R++;
//             }
//         }
//         return totalStr;
//     }
// }

import java.util.Stack;

class Solution {
    public int totalStrength(int[] strength) {
        int MOD = 1_000_000_007;
        int n = strength.length;

        long[] prefixSum = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = (prefixSum[i] + strength[i]) % MOD;
        }

        int[] prevLess = new int[n];
        int[] nextLess = new int[n];

        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && strength[stack.peek()] >= strength[i]) {
                stack.pop();
            }
            prevLess[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && strength[stack.peek()] > strength[i]) {
                stack.pop();
            }
            nextLess[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }
        long totalStrength = 0;
        for (int i = 0; i < n; i++) {
            long leftCount = i - prevLess[i];
            long rightCount = nextLess[i] - i;
            long sum = (prefixSum[nextLess[i]] - prefixSum[i]) % MOD;
            long contribution = strength[i] * leftCount % MOD * rightCount % MOD * sum % MOD;
            totalStrength = (totalStrength + contribution) % MOD;
        }
        return (int) totalStrength;
    }
}
