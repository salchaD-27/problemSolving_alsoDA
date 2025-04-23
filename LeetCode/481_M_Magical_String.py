# class Solution:
#     def magicalString(self, n: int) -> int:
#         s = [1, 2]
#         index = 2 
#         count = 1
#         while len(s) < n:
#             num = s[index]
#             for _ in range(num):
#                 if s[-1] == 1: s.append(2)
#                 else: s.append(1)
#                 if s[-1] == 1: count += 1
#             index += 1
#         return count if n < len(s) else count

class Solution(object):
    def magicalString(self, n):
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            s += [3 - s[-1]] * s[i]
            i += 1
        return s[:n].count(1)