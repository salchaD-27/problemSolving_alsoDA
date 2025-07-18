class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)
        count = 0
        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]
        for k in range(1, 100000):
            s = str(k)
            # odd len
            p = int(s + s[-2::-1])
            p2 = p * p
            if p2 > right: break
            if p2 >= left and is_palindrome(p2): count += 1
            # even len
            p = int(s + s[::-1])
            p2 = p * p
            if p2 > right: continue
            if p2 >= left and is_palindrome(p2): count += 1
        return count

import math
class Solution:
    ROOTS = [0, 1, 2, 3, 11, 22, 101 , 111, 121, 202, 212, 1001,
             1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211,
             20002, 20102, 100001, 101101, 110011, 111111, 200002,
             1000001 , 1001001 , 1002001 , 1010101 , 1011101 ,
             1012101 , 1100011 , 1101011 , 1102011 , 1110111 , 
             1111111 , 2000002 , 2001002 , 10000001, 10011001 , 
             10100101 , 10111101 , 11000011 , 11011011 , 11100111 , 
             11111111 , 20000002 , 100000001, 100010001, 100020001, 
             100101001, 100111001, 100121001, 101000101, 101010101, 
             101020101, 101101101, 101111101, 110000011, 110010011, 
             110020011, 110101011, 110111011, 111000111, 111010111, 
             111101111, 111111111, 200000002, 200010002]
    def superpalindromesInRange(self, left, right):
        result = 0
        left_small = int(math.ceil(math.sqrt(int(left))))
        right_small = int(math.floor(math.sqrt(int(right))))
        idx_left = 0
        while self.ROOTS[idx_left] < left_small: idx_left += 1
        idx_right = idx_left - 1
        while idx_right < len(self.ROOTS) and self.ROOTS[idx_right] <= right_small: idx_right += 1
        return 0 if idx_left > idx_right else idx_right - idx_left