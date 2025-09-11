class Solution:
    def baseNeg2(self, x):
        # def base2(self, x):
        #     res = []
        #     while x:
        #         res.append(x & 1)
        #         x = x >> 1
        #     return "".join(map(str, res[::-1] or [0]))
        res = []
        while x:
            res.append(x & 1)
            x = -(x >> 1)
        return "".join(map(str, res[::-1] or [0]))