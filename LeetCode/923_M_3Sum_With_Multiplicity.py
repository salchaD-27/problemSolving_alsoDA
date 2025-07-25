from collections import Counter
class Solution:
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count)
        result = 0
        for i in range(len(keys)):
            a = keys[i]
            for j in range(i, len(keys)):
                b = keys[j]
                c = target - a - b
                if c < b: continue
                if c not in count: continue
                if a == b == c: result += count[a] * (count[a] - 1) * (count[a] - 2) // 6
                elif a == b != c: result += count[a] * (count[a] - 1) // 2 * count[c]
                elif a < b == c: result += count[a] * count[b] * (count[b] - 1) // 2
                elif a < b < c: result += count[a] * count[b] * count[c]
        return result % MOD