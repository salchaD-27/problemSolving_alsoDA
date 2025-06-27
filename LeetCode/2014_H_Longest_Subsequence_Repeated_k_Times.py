# class Solution:
#     def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
#         def isSubseq(matchS, withS):
#             i, j = 0, 0
#             while i < len(matchS) and j < len(withS):
#                 if matchS[i] == withS[j]: i += 1
#                 j += 1
#             return i == len(matchS)

#         longLen = 0
#         longStr = []
#         def backtrack(currStr, currIdx):
#             nonlocal longStr, longLen
#             if isSubseq(currStr * k, s):
#                 if len(currStr) > longLen:
#                     longStr = [currStr]
#                     longLen = len(currStr)
#                 elif len(currStr) == longLen: longStr.append(currStr)
#             if currIdx + 1 < len(s):
#                 backtrack(currStr + s[currIdx + 1], currIdx + 1)
#                 backtrack(currStr, currIdx + 1)

#         if not s: return ""
#         backtrack('', -1)
#         return sorted(longStr)[-1] if longStr else ''

# from collections import deque, Counter
# class Solution:
#     def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
#         def is_k_subseq(candidate: str) -> bool:
#             i = 0
#             count = 0
#             for c in s:
#                 if c == candidate[i]:
#                     i += 1
#                     if i == len(candidate):
#                         i = 0
#                         count += 1
#                         if count == k: return True
#             return False

#         freq = Counter(s)
#         valid_chars = [ch for ch in freq if freq[ch] >= k]
#         valid_chars.sort(reverse=True)
#         queue = deque([""])
#         result = ""
#         while queue:
#             curr = queue.popleft()
#             for ch in valid_chars:
#                 next_candidate = curr + ch
#                 if is_k_subseq(next_candidate):
#                     result = next_candidate
#                     queue.append(next_candidate)
#         return result

from collections import deque
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isK(sub: str, t: str, k: int) -> bool:
            count = i = 0
            for ch in t:
                if i < len(sub) and ch == sub[i]:
                    i += 1
                    if i == len(sub):
                        i = 0
                        count += 1
                        if count == k: return True
            return False

        res = ""
        q = deque([""])
        while q:
            curr = q.popleft()
            for ch in map(chr, range(ord('a'), ord('z') + 1)):
                nxt = curr + ch
                if isK(nxt, s, k):
                    res = nxt
                    q.append(nxt)
        return res