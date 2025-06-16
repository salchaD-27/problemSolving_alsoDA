# from typing import List
# from itertools import product
# from collections import Counter
# class Solution:
#     def expressiveWords(self, s: str, words: List[str]) -> int:
#         def formWords(letters):
#             unique_letters = []
#             counts = []
#             prev = None
#             count = 0
#             for ch in letters:
#                 if ch == prev: count += 1
#                 else:
#                     if prev is not None:
#                         unique_letters.append(prev)
#                         counts.append(count)
#                     prev = ch
#                     count = 1
#             if prev is not None:
#                 unique_letters.append(prev)
#                 counts.append(count)
#             ranges = [range(0, c + 1) for c in counts]
#             result = []
#             for combo in product(*ranges):
#                 if all(x == 0 for x in combo): continue
#                 word = ''.join([ch * n for ch, n in zip(unique_letters, combo)])
#                 result.append(word)
#             return result

#         letters=[s[0], s[1]]
#         for i in range(2, len(s)):
#             if s[i]==s[i-1] and s[i]==s[i-2]: continue
#             else: letters.append(s[i])
#         count=0
#         poss=formWords(letters)
#         for word in words:
#             if word not in poss: count+=1
#         return count

from typing import List
from itertools import groupby
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def encode(word): return [(char, len(list(group))) for char, group in groupby(word)]
        def is_expressive(s_encoded, w_encoded):
            if len(s_encoded) != len(w_encoded): return False
            for (sc, sc_count), (wc, wc_count) in zip(s_encoded, w_encoded):
                if sc != wc: return False
                if sc_count < 3:
                    if sc_count != wc_count: return False
                else:
                    if wc_count > sc_count: return False
            return True
    
        s_encoded = encode(s)
        return sum(is_expressive(s_encoded, encode(word)) for word in words)