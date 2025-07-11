# from typing import List
# from collections import deque
# class Solution:
#     def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
#         queue=deque()
#         queue.append(str(digits[0]))
#         count=0
#         while queue:
#             currNum=queue.popleft()
#             if int(currNum)<=n: count+=1
#             else: continue
#             for i in range(len(digits)):
#                 queue.append(currNum+str(digits[i]))
#         return count

from typing import List
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        num_digits = len(s)
        digits_len = len(digits)
        count = 0
        for i in range(1, num_digits):
            count += digits_len ** i
        for i in range(num_digits):
            has_same_digit = False
            for d in digits:
                if d < s[i]: count += digits_len ** (num_digits - i - 1)
                elif d == s[i]:
                    has_same_digit = True
                    break
            if not has_same_digit: return count
        return count + 1