class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrome(s): return s==s[::-1]
        count=0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if palindrome(s[i:j+1]): count+=1
        return count
    
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            l2, r2 = i, i+1
            while l2 >= 0 and r2 < len(s) and s[l2] == s[r2]:
                res += 1
                l2 -= 1
                r2 += 1
        return res