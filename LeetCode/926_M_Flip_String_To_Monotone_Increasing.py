class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        prefix_ones = [0] * (n + 1)
        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + (s[i] == '1')
        min_flips = float('inf')
        for i in range(n + 1):
            # L: 1s in s[0:i] => flip to 0
            ones_left = prefix_ones[i]
            # R: 0s in s[i:] => flip to 1
            zeros_right = (n - i) - (prefix_ones[n] - prefix_ones[i])
            min_flips = min(min_flips, ones_left + zeros_right)
        return min_flips

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        num = 0
        for c in s:
            if c == '0': ans = min(num, ans + 1)
            else: num += 1
        return ans