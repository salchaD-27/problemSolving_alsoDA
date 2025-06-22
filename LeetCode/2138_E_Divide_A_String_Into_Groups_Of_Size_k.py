from typing import List
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        for i in range(len(s)):
            if not res: res.append(s[i])
            elif len(res[-1])>=k: res.append(s[i])
            else: res[-1]+=s[i]
        while len(res[-1])<k:
            res[-1]+=fill
        return res

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        curr = 0
        while curr < n:
            res.append(s[curr : curr + k])
            curr += k
        res[-1] += fill * (k - len(res[-1]))
        return res