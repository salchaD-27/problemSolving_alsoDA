# from typing import List
# class Solution:
#     def maxChunksToSorted(self, arr: List[int]) -> int:
#         count=1
#         stack=[]
#         for num in arr:
#             if not stack: stack.append(num)
#             else:
#                 stackTop=stack[0]
#                 if stackTop<=num: 
#                     stack=[num]
#                     count+=1
#                 else: stack.append(num)
#         return count

from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            if not stack or num >= stack[-1]: stack.append(num)
            else:
                max_in_chunk = stack.pop()
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(max_in_chunk)
        return len(stack)