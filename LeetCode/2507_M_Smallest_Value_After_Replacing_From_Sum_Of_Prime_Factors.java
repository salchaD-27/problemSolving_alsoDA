class Solution {
    public boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++){if (n % i == 0) return false;}
        return true;
    }
    public int sumOfPrimeFactors(int n) {
        int sum = 0;
        for (int i = 2; i * i <= n; i++) {
            while (n % i == 0) {
                sum += i;
                n /= i;
            }
        }
        if (n > 1) sum += n;
        return sum;
    }
    public int smallestValue(int n) {
        if(isPrime(n)){return n;}
        if(n==4){return 4;}
        while (!isPrime(n)){n = sumOfPrimeFactors(n);}
        return n;
    }
}