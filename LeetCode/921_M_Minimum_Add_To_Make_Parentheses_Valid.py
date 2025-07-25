class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0  # unmatched (
        insertions = 0  # insertions needed
        for char in s:
            if char == '(': balance += 1
            else:
                if balance > 0: balance -= 1  # match with (
                else: insertions += 1  # need to insert ( before )
        return balance + insertions  # unmatched ( + )