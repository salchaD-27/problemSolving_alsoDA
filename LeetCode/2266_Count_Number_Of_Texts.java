class Solution {
    public int countTexts(String pressedKeys) {
        final int MOD = 1_000_000_007;
        int n = pressedKeys.length();
        long[] dp = new long[n + 1];
        dp[0] = 1;
        
        for (int i = 1; i <= n; i++) {
            char currentKey = pressedKeys.charAt(i - 1);
            dp[i] = dp[i - 1];
            int limit = (currentKey == '7' || currentKey == '9') ? 4 : 3;
            for (int j = 2; j <= limit; j++) {
                if (i - j >= 0 && pressedKeys.charAt(i - j) == currentKey){dp[i] = (dp[i] + dp[i - j]) % MOD;}
                else{break;}
            }
        }
        return (int) dp[n];
    }
}