class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, first, second, value):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += value
                else: stack.append(char)
            return ''.join(stack), score
        if x > y: # ab then ba
            remaining, score1 = remove_substring(s, 'a', 'b', x)
            _, score2 = remove_substring(remaining, 'b', 'a', y)
        else: # ba then ab
            remaining, score1 = remove_substring(s, 'b', 'a', y)
            _, score2 = remove_substring(remaining, 'a', 'b', x)
        return score1 + score2