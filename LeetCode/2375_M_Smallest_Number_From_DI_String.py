class Solution:
    def smallestNumber(self, pattern: str) -> str:
        if('I' not in pattern): return ''.join([str(i) for i in reversed(range(1, len(pattern)+2))])
        if('D' not in pattern): return ''.join([str(i) for i in range(1, len(pattern)+2)])
        res, stack = [], []
        for i in range(len(pattern) + 1): 
            stack.append(i + 1)
            while stack and (i == len(pattern) or pattern[i]== "I"):
                res.append(str(stack.pop()))
        return ''.join(res)