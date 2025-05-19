# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         if s[0]==')': return False
#         parenCount,starCount=0,0
#         for i in range(len(s)):
#             if s[i]=='(': parenCount+=1
#             if s[i]==')': parenCount-=1
#             if s[i]=='*': starCount+=1
#         if abs(parenCount)==starCount: return True
#         if not parenCount and starCount: return True
#         return False

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0  # min no of open paren
        high = 0  # max no of open paren
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            elif char == '*':
                low -= 1
                high += 1
            if high < 0: return False
            low = max(low, 0)
        return low==0