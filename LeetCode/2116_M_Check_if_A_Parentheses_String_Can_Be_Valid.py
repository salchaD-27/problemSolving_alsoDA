# class Solution:
#     def canBeValid(self, s: str, locked: str) -> bool:
#         if len(s) % 2 != 0: return False
#         # l to r check
#         open_count = 0
#         flexible = 0  # no of unlocked pos
#         for i in range(len(s)):
#             if locked[i] == '1':
#                 if s[i] == '(': open_count += 1
#                 else: open_count -= 1
#             else:
#                 flexible += 1 # ( or )
#                 open_count += 1
#             if open_count < 0:
#                 if flexible > 0:
#                     open_count += 2
#                     flexible -= 1
#                 else: return False
#         # r to l check
#         close_count = 0
#         flexible = 0
#         for i in reversed(range(len(s))):
#             if locked[i] == '1':
#                 if s[i] == ')': close_count += 1
#                 else: close_count -= 1
#             else:
#                 flexible += 1
#                 close_count += 1
#             if close_count < 0:
#                 if flexible > 0:
#                     close_count += 2
#                     flexible -= 1
#                 else: return False
#         return True

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stringLength = len(s)
        if stringLength % 2 == 1: return False
        openIndices = []
        unlockedIndices = []
        for i in range(stringLength):
            if locked[i] == '0': unlockedIndices.append(i)
            elif s[i] == '(': openIndices.append(i)
            elif s[i] == ')':
                if openIndices: openIndices.pop()
                elif unlockedIndices: unlockedIndices.pop()
                else: return False
        while openIndices and unlockedIndices and openIndices[-1] < unlockedIndices[-1]:
            openIndices.pop()
            unlockedIndices.pop()
        if not openIndices and unlockedIndices: return len(unlockedIndices) % 2 == 0
        return not openIndices