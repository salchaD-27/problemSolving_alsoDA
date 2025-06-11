# from collections import Counter
# class Solution:
#     def maxDifference(self, s: str, k: int) -> int:
#         def subMaxDifference(substr):
#             count = Counter(substr)
#             minOddA, maxEvenB = float('inf'), 0
#             for freq in count.values():
#                 if freq % 2 == 0: maxEvenB = max(maxEvenB, freq)
#                 else: minOddA = min(minOddA, freq)
#             if minOddA == float('inf'): minOddA = 0
#             return minOddA - maxEvenB

#         res = float('-inf')
#         for i in range(len(s) - k + 1):
#             substr = s[i:i + k]
#             res = max(res, subMaxDifference(substr))
#         return res

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def getStatus(cnt_a: int, cnt_b: int) -> int: return ((cnt_a & 1) << 1) | (cnt_b & 1)
        n = len(s)
        ans = float("-inf")
        for a in ["0", "1", "2", "3", "4"]:
            for b in ["0", "1", "2", "3", "4"]:
                if a == b: continue
                best = [float("inf")] * 4
                cnt_a = cnt_b = 0
                prev_a = prev_b = 0
                left = -1
                for right in range(n):
                    cnt_a += s[right] == a
                    cnt_b += s[right] == b
                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = getStatus(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                        left += 1
                        prev_a += s[left] == a
                        prev_b += s[left] == b
                    right_status = getStatus(cnt_a, cnt_b)
                    if best[right_status ^ 0b10] != float("inf"):
                        ans = max(ans, cnt_a - cnt_b - best[right_status ^ 0b10])
        return ans