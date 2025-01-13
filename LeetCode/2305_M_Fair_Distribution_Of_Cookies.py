from typing import List
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.min_unfairness = float('inf')
        distribution = [0] * k
        
        def backtrack(index):
            if index == len(cookies):
                self.min_unfairness = min(self.min_unfairness, max(distribution))
                return
            for i in range(k):
                distribution[i] += cookies[index]
                if max(distribution) < self.min_unfairness: backtrack(index + 1)
                distribution[i] -= cookies[index]
                if distribution[i] == 0: break
        cookies.sort(reverse=True)
        backtrack(0)
        return self.min_unfairness