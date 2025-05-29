# class Solution:
#     def monotoneIncreasingDigits(self, n: int) -> int:
#         def ifMono(num):
#             num=str(num)
#             for i in range(len(num)-1):
#                 if int(num[i])>int(num[i+1]): return False
#             return True
#         while(True):
#             if ifMono(n): return n
#             n-=1

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        mark = len(digits)
        for i in range(len(digits)-1, 0, -1):
            if digits[i] < digits[i-1]:
                digits[i-1] = str(int(digits[i-1]) - 1)
                mark = i
        for i in range(mark, len(digits)):
            digits[i] = '9'
        return int("".join(digits))