# from typing import List
# class Solution:
#     def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
#         def sort(s): return "".join(sorted(list(s)))
#         toInclude=''.join(words2)
#         toInclude=sort(toInclude)
#         return [word for word in words1 if toInclude in sort(word)]

from typing import List
from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word): return Counter(word)
        required = Counter()
        for word in words2:
            word_count = count(word)
            for char in word_count:
                required[char] = max(required[char], word_count[char])
        res = []
        for word in words1:
            word_count = count(word)
            if all(word_count[char] >= required[char] for char in required): res.append(word)
        return res