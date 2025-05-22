from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        # (-frequency, word)
        sorted_words = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        return [word for word, _ in sorted_words[:k]]