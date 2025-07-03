from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        removed = 0
        for count in freq.values():
            if count >= 3: removed += 2 * ((count - 1) // 2)
        return len(s) - removed