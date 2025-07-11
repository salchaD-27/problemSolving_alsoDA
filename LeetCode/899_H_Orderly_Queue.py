class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1: return min(s[i:] + s[:i] for i in range(len(s)))
        else: return ''.join(sorted(s))

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k==1:
            min_str=s
            for i in range(len(s)):
                if s<min_str: min_str=s
                s=s[1:]+s[0]    
            return min_str
        else: return "".join(sorted(s))    