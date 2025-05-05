from typing import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        slidingLen=len(s1)
        count=Counter(s1)
        for i in range(0,len(s2)-slidingLen+1):
            tempCount=Counter(s2[i:i+slidingLen])
            if(tempCount==count): return True
        return False
    
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2: return False
        count1 = Counter(s1)
        count2 = Counter(s2[:len1])
        if count1 == count2: return True
        for i in range(len1, len2):
            start_char = s2[i - len1]
            end_char = s2[i]
            count2[end_char] += 1
            count2[start_char] -= 1
            if count2[start_char] == 0: del count2[start_char]
            if count1 == count2: return True
        return False