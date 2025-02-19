class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(curr):
            nonlocal count, result
            if len(curr) == n:
                count += 1
                if count == k: result = curr
                return
            for char in "abc":
                if not curr or curr[-1] != char:
                    backtrack(curr + char)
                    if result: return

        count = 0
        result = ""
        backtrack("")
        return result if result else ""