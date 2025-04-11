# class Solution:
#     def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
#         count=0
#         for i in range(limit+1):
#             newS=str(i)+s
#             if start<=int(newS)<=finish: count+=1
#         return count

# limit=7
# start=1829505
# nextToStart=2011223
# end=1255574165
# prevToEnd=1255611223
# nums=12556-20+1=12537

# class Solution:
#     def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
#         suffix_len = len(s)
#         step = 10 ** suffix_len

#         def is_valid(x): return str(x).endswith(s) and all(int(d) <= limit for d in str(x))
#         def next_valid(x):
#             mod = int(s)
#             base = (x + step - 1) // step * step + mod - (int(str(x + step - 1).zfill(suffix_len)[-suffix_len:]) if len(str(x)) >= suffix_len else 0)
#             while base <= finish:
#                 if base >= start and is_valid(base): return base
#                 base += step
#             return None
#         def prev_valid(x):
#             mod = int(s)
#             base = (x // step) * step + mod
#             if base > x: base -= step
#             while base >= start:
#                 if base <= finish and is_valid(base): return base
#                 base -= step
#             return None

#         low = next_valid(start)
#         high = prev_valid(finish)
#         if low is None or high is None or low > high: return 0
#         return ((high - low) // step) + 1
    
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suffix: str) -> int:
        def count_powerful_up_to(num: int) -> int:
            num_str = str(num)
            suffix_len = len(suffix)
            prefix_len = len(num_str) - suffix_len
            if prefix_len < 0: return 0
            dp = [[0] * 2 for _ in range(prefix_len + 1)]
            dp[prefix_len][0] = 1
            suffix_from_num = num_str[prefix_len:]
            dp[prefix_len][1] = int(suffix_from_num) >= int(suffix)
            for i in range(prefix_len - 1, -1, -1):
                digit = int(num_str[i])
                dp[i][0] = (limit + 1) * dp[i + 1][0]
                if digit <= limit: dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]
                else: dp[i][1] = (limit + 1) * dp[i + 1][0]
            return dp[0][1]
        return count_powerful_up_to(finish) - count_powerful_up_to(start - 1)