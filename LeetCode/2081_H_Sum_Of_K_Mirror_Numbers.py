# class Solution:
#     def kMirror(self, k: int, n: int) -> int:
#         def is_palindrome(s: str) -> bool: return s == s[::-1]
#         def to_base(num: int, base: int) -> str:
#             if num == 0: return "0"
#             digits = []
#             while num:
#                 digits.append(str(num % base))
#                 num //= base
#             return ''.join(reversed(digits))

#         res, count, i = 0, 0, 1
#         while count < n:
#             if is_palindrome(str(i)) and is_palindrome(to_base(i, k)):
#                 res += i
#                 count += 1
#             i += 1
#         return res

class Solution:
    def createPalindrome(self, num: int, odd: bool) -> int:
        x = num
        if odd: x //= 10
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num
    def isPalindrome(self, num: int, base: int) -> bool:
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]
    def kMirror(self, k: int, n: int) -> int:
        total = 0
        length = 1
        while n > 0:
            for i in range(length, length * 10):
                if n <= 0: break
                p = self.createPalindrome(i, True)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            for i in range(length, length * 10):
                if n <= 0: break
                p = self.createPalindrome(i, False)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            length *= 10
        return total