# from typing import List
# class Solution:
#     def ambiguousCoordinates(self, s: str) -> List[str]:
#         res = []
#         def getValidNumbers(part: str) -> List[str]:
#             if len(part) == 0: return []
#             if len(part) == 1: return [part]
#             result = []
#             # no decimal point, not start with 0
#             if part[0] != '0': result.append(part)
#             # decimal at each pos
#             for i in range(1, len(part)):
#                 left = part[:i]
#                 right = part[i:]
#                 if (left == "0" or (left[0] != '0')) and right[-1] != '0': result.append(left + "." + right)
#                 if left == "0" and right[-1] != '0': 
#                     result.append("0." + right)
#                     break
#             return result
        
#         s = s[1:-1]
#         for i in range(1, len(s)):
#             left = s[:i]
#             right = s[i:]
#             left_options = getValidNumbers(left)
#             right_options = getValidNumbers(right)
#             for l in left_options:
#                 for r in right_options:
#                     res.append(f"({l}, {r})")
#         return res

from typing import List
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def getValidNumbers(s: str) -> List[str]:
            n = len(s)
            res = []
            if n == 0: return res
            if s == "0" or s[0] != '0': res.append(s)
            for i in range(1, n):
                left, right = s[:i], s[i:]
                if (left == "0" or left[0] != '0') and right[-1] != '0': res.append(left + "." + right)
            return res

        s = s[1:-1]
        n = len(s)
        seen = set()
        result = []
        for i in range(1, n):
            left, right = s[:i], s[i:]
            left_parts = getValidNumbers(left)
            right_parts = getValidNumbers(right)
            for l in left_parts:
                for r in right_parts:
                    coord = f"({l}, {r})"
                    if coord not in seen:
                        seen.add(coord)
                        result.append(coord)
        return result