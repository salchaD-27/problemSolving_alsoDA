// class Solution {
//     public int reverse(int x) {
//         if(x==1534236469){return 0;}
//         int revNum=0;
//         while(x!=0){
//             int temp=x%10;
//             x=x/10;
//             revNum*=10;
//             revNum+=temp;
//         }
//         if(revNum<=Integer.MAX_VALUE && revNum>=Integer.MIN_VALUE){return revNum;}
//         return 0;
//     }
// }

class Solution {
    public int reverse(int x) {
        int revNum = 0;
        while (x != 0) {
            int temp = x % 10;
            x = x / 10;
            if (revNum > Integer.MAX_VALUE / 10 || (revNum == Integer.MAX_VALUE / 10 && temp > 7)) {return 0;}
            if (revNum < Integer.MIN_VALUE / 10 || (revNum == Integer.MIN_VALUE / 10 && temp < -8)) {return 0;}
            revNum = revNum * 10 + temp;
        }
        return revNum;
    }
}