class Solution:
    def rand10(self) -> int:
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col  # Generates 1 to 49
            if idx <= 40: return 1 + (idx - 1) % 10