package Java;

// L=LCM(p,q)
// m=L/p: the number of times the ray reaches the east or west wall
// n=L/q: the number of times the ray reaches the north or south wall

class Solution {
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    private int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }

    public int mirrorReflection(int p, int q) {
        int lcm = lcm(p, q);
        int m = lcm / p; 
        int n = lcm / q;
        if (m % 2 == 1 && n % 2 == 1) return 1;
        if (m % 2 == 1 && n % 2 == 0) return 2;
        return 0;
    }
}