# from typing import List
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         if(s=='' or len(s)==1): return 0
#         def oin(list):
#             count=0
#             for char in list:
#                 if char=='(': count+=1
#             return count
#         def cin(list):
#             count=0
#             for char in list:
#                 if char==')': count+=1
#             return count

#         pairs=[]
#         firstOpening=0
#         for i in range(len(s)):
#             if s[i]=='(' and cin(s[i+1:]):
#                 firstOpening=i
#                 break
#         pairs.append(s[firstOpening])

#         for j in range(i, len(s)):
#             if s[j]=='(' and cin(s[j+1:]): pairs.append(s[j])
#             if s[j]==')' and oin(pairs)>cin(pairs): pairs.append(s[j])
#         return len(pairs)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(': stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                else: max_len = max(max_len, i - stack[-1])
        return max_len