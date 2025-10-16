class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        while j + k < len(s):
            if s[i + k] == s[j + k]: k += 1
            elif s[i + k] > s[j + k]:
                j = j + k + 1
                k = 0
            else:
                if i + k + 1 > j: i = j + k - 1
                else: i = j
                j = i + 1
                k = 0
        return s[i:]