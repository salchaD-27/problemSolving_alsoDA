class Solution:
    def addNegabinary(self, A, B):
        res = []
        carry = 0
        while A or B or carry:
            carry += (A or [0]).pop() + (B or [0]).pop()
            res.append(carry & 1)
            carry = -(carry >> 1)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]

class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry != 0:
            x = arr1[i] if i >= 0 else 0
            y = arr2[j] if j >= 0 else 0
            total = x + y + carry
            res.append(total & 1)  # total % 2
            carry = -(total >> 1)  # -(total // 2)
            i -= 1
            j -= 1
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]