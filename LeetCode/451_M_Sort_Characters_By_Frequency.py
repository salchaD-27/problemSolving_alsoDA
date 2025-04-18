class Solution:
    def frequencySort(self, s: str) -> str:
        countMap = {}
        for char in s:
            countMap[char] = countMap.get(char, 0) + 1
        sorted_chars = sorted(countMap.items(), key=lambda x: x[1], reverse=True)
        result = ''
        for char, freq in sorted_chars:
            result += char * freq
        return result
    
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        res = ""
        for char, freq in count:
            res += (char * freq)
        return res