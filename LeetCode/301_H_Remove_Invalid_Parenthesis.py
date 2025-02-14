# from typing import List
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         def isValid(sS: str) -> bool:
#             count = 0
#             for char in sS:
#                 if char == '(': count += 1
#                 elif char == ')':
#                     count -= 1
#                     if count < 0: return False
#             return count == 0
#         def solveExtraOpen(sS: List[str], openCount: int, closeCount: int) -> List[str]:
#             result = []
#             if openCount > closeCount:
#                 for i in range(len(sS)):
#                     if sS[i] == '(':
#                         sS.pop(i)
#                         if isValid(''.join(sS)): result.append(''.join(sS))
#                         sS.insert(i, '(')
#             return result
#         def solveExtraClose(sS: List[str], openCount: int, closeCount: int) -> List[str]:
#             result = []
#             if closeCount > openCount:
#                 for i in range(len(sS)):
#                     if sS[i] == ')':
#                         sS.pop(i)
#                         if isValid(''.join(sS)): result.append(''.join(sS))
#                         sS.insert(i, ')')
#             return result
#         openCount, closeCount = 0, 0
#         for char in s:
#             if char == '(': openCount += 1
#             elif char == ')': closeCount += 1
#         sS = list(s)
#         if openCount > closeCount: return list(set(solveExtraOpen(sS, openCount, closeCount)))
#         elif closeCount > openCount: return list(set(solveExtraClose(sS, openCount, closeCount)))
#         else: return list(set([s]))

from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            count = 0
            for char in s:
                if char == '(': count += 1
                elif char == ')':
                    count -= 1
                    if count < 0: return False
            return count == 0
        
        result = set()
        queue = {s}
        found = False
        while queue:
            level = set()
            for curr in queue:
                if isValid(curr):
                    result.add(curr)
                    found = True
                if not found:
                    for i in range(len(curr)):
                        if curr[i] not in ('(', ')'): continue
                        next_str = curr[:i] + curr[i+1:]
                        level.add(next_str)
            if found: break
            queue = level
        return list(result)