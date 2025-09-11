# class Solution:
#     def queryString(self, S, N):
#         return all(bin(i)[2:] in S for i in range(N, N / 2, -1))

class Solution:
    def queryString(self, s, n):
        if n > 1000: n = 1000
        for x in range(1, n + 1):
            if bin(x)[2:] not in s: return False
        return True