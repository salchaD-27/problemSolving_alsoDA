from typing import List
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        score = 0
        max_score = 0
        left = 0
        right = n - 1
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else: break
        return max_score

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        start, end = 0, len(tokens) - 1
        score = 0
        max_score = 0

        while start <= end:
            if power >= tokens[start]:
                power -= tokens[start]
                score += 1
                max_score = max(max_score, score)
                start += 1
            elif score > 0:
                power += tokens[end]
                score -= 1
                end -= 1
            else: return max_score
        return max_score