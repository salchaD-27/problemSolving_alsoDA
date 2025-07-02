# from collections import deque
# class Solution:
#     def possibleStringCount(self, word: str, k: int) -> int:
#         n=len(word)
#         queue=deque()
#         queue.append([word[0], 0])
#         res=0
#         while queue:
#             currWord,lastAddedIdx=queue.popleft()
#             if lastAddedIdx==n-1 and len(currWord)<k: continue
#             elif lastAddedIdx==n-1 and len(currWord)>=k: res+=1
#             else:
#                 if len(currWord)>=k: res+=1
#                 lastAddedChar=currWord[-1]
#                 if word[lastAddedIdx+1]==lastAddedChar: queue.append([currWord,lastAddedIdx+1])
#                 queue.append([currWord+word[lastAddedIdx+1],lastAddedIdx+1])
#         return res

# from collections import deque
# class Solution:
#     def possibleStringCount(self, word: str, k: int) -> int:
#         n = len(word)
#         queue = deque()
#         queue.append((word[0], 0))
#         seen = set()
#         while queue:
#             currWord, lastIdx = queue.popleft()
#             if len(currWord) >= k: seen.add(currWord)
#             if lastIdx == n - 1: continue
#             next_char = word[lastIdx + 1]
#             last_char = currWord[-1]
#             if next_char == last_char: queue.append((currWord, lastIdx + 1))
#             queue.append((currWord + next_char, lastIdx + 1))
#         return len(seen)

class Solution:
    MOD = 10**9 + 7
    def possibleStringCount(self, word: str, k: int) -> int:
        if not word: return 0
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]: count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)
        total = 1
        for num in groups:
            total = (total * num) % self.MOD
        if k <= len(groups): return total
        dp = [0] * k
        dp[0] = 1
        for num in groups:
            new_dp = [0] * k
            sum_val = 0
            for s in range(k):
                if s > 0: sum_val = (sum_val + dp[s - 1]) % self.MOD
                if s > num: sum_val = (sum_val - dp[s - num - 1] + self.MOD) % self.MOD
                new_dp[s] = sum_val
            dp = new_dp
        invalid = sum(dp[len(groups):k]) % self.MOD
        return (total - invalid + self.MOD) % self.MOD