# from typing import List
# class Solution:
#     def removeComments(self, source: List[str]) -> List[str]:
#         in_block = False
#         res = []
#         new_line = []
#         for line in source:
#             i = 0
#             while i < len(line):
#                 if not in_block:
#                     if line[i:i+2] == "//": break
#                     elif line[i:i+2] == "/*":
#                         in_block = True
#                         i += 2
#                     else:
#                         new_line.append(line[i])
#                         i += 1
#                 else:
#                     if line[i:i+2] == "*/":
#                         in_block = False
#                         i += 2
#                     else: i += 1
#             if new_line and not in_block:
#                 res.append("".join(new_line))
#                 new_line = []
#         return res

from typing import List
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        current = []
        inBlockComment = False
        for line in source:
            i = 0
            while i < len(line):
                if inBlockComment:
                    if i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                        inBlockComment = False
                        i += 1
                else:
                    if i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                        inBlockComment = True
                        i += 1
                    elif i + 1 < len(line) and line[i] == '/' and line[i+1] == '/': break
                    else: current.append(line[i])
                i += 1
            if not inBlockComment and current:
                result.append("".join(current))
                current = []
        return result