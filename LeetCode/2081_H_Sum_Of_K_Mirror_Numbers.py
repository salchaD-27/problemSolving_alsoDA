class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool: return s == s[::-1]
        def to_base(num: int, base: int) -> str:
            if num == 0: return "0"
            digits = []
            while num:
                digits.append(str(num % base))
                num //= base
            return ''.join(reversed(digits))

        res, count, i = 0, 0, 1
        while count < n:
            if is_palindrome(str(i)) and is_palindrome(to_base(i, k)):
                res += i
                count += 1
            i += 1
        return res