from typing import List
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        count = 0
        for c in s:
            current = waiting.pop(c, [])
            for it in current:
                nxt = next(it, None)
                if nxt: waiting[nxt].append(it)
                else: count += 1
        return count