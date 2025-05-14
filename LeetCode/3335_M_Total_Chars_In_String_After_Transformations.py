# a: +25 to z, +1 to ab, +25 to yz, +1 to zab, +1 to abbc, 
# 26-2
# 52-3
# 53-4

from collections import Counter
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):
                if freq[i] == 0: continue
                if i == 25:  # z-ab
                    new_freq[0] = (new_freq[0] + freq[i]) % MOD
                    new_freq[1] = (new_freq[1] + freq[i]) % MOD
                else: new_freq[i + 1] = (new_freq[i + 1] + freq[i]) % MOD
            freq = new_freq
        return sum(freq) % MOD