# 1. If enc a number, push two units to stack, marking that we need to check for its 2 children (either 2 nums, or 1 num and 1 #, or 2 #).
# (Also pop one unit from stack marking we marked one node that might have been child of some parent node previously, except for the root node)
# 2. If enc a #, pop one unit from stack, marking that we need have checked for its one null child.
# 3. At end, return if stack is empty, since empty stack represents all nodes have been visited correctly

# class Solution:
#     def isValidSerialization(self, preorder: str) -> bool:
#         stack = []
#         nodes = preorder.split(",")
#         for i, node in enumerate(nodes):
#             if node != "#":
#                 if stack:
#                     stack[-1] -= 1
#                     if stack[-1] == 0: stack.pop()
#                 stack.append(2)
#             else:
#                 if not stack: return False
#                 stack[-1] -= 1
#                 if stack[-1] == 0: stack.pop()
#         return not stack

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        nodes = preorder.split(",")
        for node in nodes:
            slots -= 1
            if slots < 0: return False
            if node != "#": slots += 2
        return slots == 0