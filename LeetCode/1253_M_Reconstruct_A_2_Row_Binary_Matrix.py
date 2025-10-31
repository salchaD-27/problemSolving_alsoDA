class Solution:
    def reconstructMatrix(self, upper, lower, colsum):
        n = len(colsum)
        top = [0] * n
        bottom = [0] * n
        for i in range(n):
            if colsum[i] == 2:
                top[i] = 1
                bottom[i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if upper > lower:
                    top[i] = 1
                    upper -= 1
                else:
                    bottom[i] = 1
                    lower -= 1
        if upper == 0 and lower == 0: return [top, bottom]
        return []