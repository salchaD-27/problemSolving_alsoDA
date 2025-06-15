class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        max_val = float('-inf')
        min_val = float('inf')
        for x in '0123456789':
            for y in '0123456789':
                if x == y: continue
                replaced = s.replace(x, y)
                if replaced[0] == '0': continue
                val = int(replaced)
                max_val = max(max_val, val)
                min_val = min(min_val, val)
        return max_val - min_val