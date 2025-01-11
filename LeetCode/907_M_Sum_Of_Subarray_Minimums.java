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
//     public int sumSubarrayMins(int[] arr) {
//         int sum=0;
//         for(int i=0; i<arr.length; i++){
//             int L=i, R=i;
//             for(int j=i; j<arr.length; j++){
//                 sum+=minOfSubarr(arr, L, R);
//                 R++;
//             }
//         }
//         return sum;
//     }
// }

import java.util.Stack;

class Solution {
    public int sumSubarrayMins(int[] arr) {
        int MOD = 1_000_000_007;
        int n = arr.length;

        int[] left = new int[n];
        int[] right = new int[n];

        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            left[i] = stack.isEmpty() ? i + 1 : i - stack.peek();
            stack.push(i);
        }
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop();
            }
            right[i] = stack.isEmpty() ? n - i : stack.peek() - i;
            stack.push(i);
        }
        long sum = 0;
        for (int i = 0; i < n; i++) {
            long contribution = (long) arr[i] * left[i] * right[i];
            sum = (sum + contribution) % MOD;
        }
        return (int) sum;
    }
}

