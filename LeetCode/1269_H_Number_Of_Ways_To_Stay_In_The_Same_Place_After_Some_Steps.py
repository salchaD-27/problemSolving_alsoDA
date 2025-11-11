class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_position = min(steps // 2 + 1, arrLen)
        cur_ways = [0] * (max_position + 2)
        next_ways = [0] * (max_position + 2)
        cur_ways[1] = 1
        mod = 10 ** 9 + 7
        while steps > 0:
            for pos in range(1, max_position + 1):
                next_ways[pos] = (cur_ways[pos] + cur_ways[pos - 1] + cur_ways[pos + 1]) % mod
            cur_ways, next_ways = next_ways, cur_ways
            steps -= 1
        return cur_ways[1]        