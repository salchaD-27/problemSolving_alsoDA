from collections import defaultdict
class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        pattern_count = defaultdict(int)
        for row in matrix:
            temp = "".join('1' if x == row[0] else '0' for x in row)
            pattern_count[temp] += 1
        maxi = max(pattern_count.values())
        return maxi