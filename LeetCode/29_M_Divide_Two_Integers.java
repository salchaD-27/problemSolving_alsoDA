// class Solution {
//     public int divide(int dividend, int divisor) {
//         if (dividend == Integer.MIN_VALUE && divisor == -1){return Integer.MAX_VALUE;}
//         int count = 0, sign = 1;
//         if ((divisor * dividend) != (Math.abs(divisor * dividend))){sign = -1;}
//         divisor = Math.abs(divisor);
//         dividend = Math.abs(dividend);
//         while (dividend >= divisor) {
//             dividend -= divisor;
//             count++;
//         }
//         return count * sign;
//     }
// }

class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1){return Integer.MAX_VALUE;}
        int sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1;
        long longDividend = Math.abs((long) dividend);
        long longDivisor = Math.abs((long) divisor);
        long result = 0;
        while (longDividend >= longDivisor) {
            long tempDivisor = longDivisor, multiple = 1;
            while (longDividend >= (tempDivisor << 1)) {
                tempDivisor <<= 1;
                multiple <<= 1;
            }
            longDividend -= tempDivisor;
            result += multiple;
        }
        result = sign * result;
        return (int) Math.min(Math.max(result, Integer.MIN_VALUE), Integer.MAX_VALUE);
    }
}