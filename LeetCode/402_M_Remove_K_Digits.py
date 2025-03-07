# 3
# 1 4 3 2 2 1 9
# 1       2 1 9
# 3-1=2-1=2-1=0
# 9
# 1
# 2
# 1

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        stack = stack[:len(stack) - k]  
        result = "".join(stack).lstrip("0")
        return result if result else "0"