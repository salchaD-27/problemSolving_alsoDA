# class Solution:
#     def largestPalindrome(self, n: int) -> int:
#         pal = [0, 9, 987, 123, 597, 677, 1218, 877, 475]
#         return pal[n]

class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        upper = 10**n - 1
        lower = 10**(n - 1)
        for x in range(upper, lower - 1, -1):
            left = str(x)
            pal = int(left + left[::-1])
            for y in range(upper, lower - 1, -1):
                if pal // y > upper: break
                if pal % y == 0: return pal % 1337
        return 0