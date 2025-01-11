// class Solution {
//     private boolean isInvalidString(String s) {
//         int first0 = s.indexOf('0');
//         int first1 = s.indexOf('1');
//         if (first0 == -1 || first1 == -1){return true;}

//         int last0 = s.lastIndexOf('0');
//         int last1 = s.lastIndexOf('1');
//         if (last0 < first1 || last1 < first0){return true;}
//         return false;
//     }
//     public long numberOfWays(String s) {
//         if (isInvalidString(s)) {return 0;}
//         long count0 = 0, count1 = 0;  
//         long count01 = 0, count10 = 0; 
//         long count010 = 0, count101 = 0; 

//         for (char c : s.toCharArray()) {
//             if (c == '0') {
//                 count010 += count10; 
//                 count10 += count1;   
//                 count0++;            
//             } else if (c == '1') {
//                 count101 += count01; 
//                 count01 += count0;   
//                 count1++;            
//             }
//         }
//         return count010 + count101;
//     }    
// }

class Solution {
    public long numberOfWays(String s) {
        int n = s.length();
        long[] prefix0 = new long[n];
        long[] prefix1 = new long[n];
        long[] suffix0 = new long[n];
        long[] suffix1 = new long[n];
        // Prefix counts 
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                prefix0[i] = prefix0[i - 1];
                prefix1[i] = prefix1[i - 1];
            }
            if (s.charAt(i) == '0'){prefix0[i]++;}
            else{prefix1[i]++;}
        }
        // Suffix counts
        for (int i = n - 1; i >= 0; i--) {
            if (i < n - 1) {
                suffix0[i] = suffix0[i + 1];
                suffix1[i] = suffix1[i + 1];
            }
            if (s.charAt(i) == '0'){suffix0[i]++;}
            else{suffix1[i]++;}
        }

        long count = 0;
        // Valid combinations
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0'){count += prefix1[i] * suffix1[i];}
            else{count += prefix0[i] * suffix0[i];}
        }
        return count;
    }
}
