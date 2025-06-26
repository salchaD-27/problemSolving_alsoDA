# class Solution:
#     def longestSubsequence(self, s: str, k: int) -> int:
#         def matchSubSeq(matchS, toS):
#             i, j = 0, 0
#             while i < len(matchS) and j < len(toS):
#                 if matchS[i] == toS[j]:
#                     i += 1
#                     j += 1
#                 else: j += 1
#             return i == len(matchS)
#         def binToDec(binS): return int(binS, 2)
#         def decToBin(decS): return bin(decS)[2:]

#         sDec = binToDec(s)
#         if sDec <= k: return len(s)
#         for i in range(len(s), 0, -1):
#             for num in range(k, -1, -1):
#                 b = decToBin(num)
#                 if len(b) == i and matchSubSeq(b, s): return i
#         return 0

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        ones = 0
        value = 0
        power = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if value + power > k: continue
                value += power
                ones += 1
            power <<= 1
            if power > k: break
        return zeros + ones