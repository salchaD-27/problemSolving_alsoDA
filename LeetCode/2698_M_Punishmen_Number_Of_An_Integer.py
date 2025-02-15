class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(s: str, target: int, index: int, current_sum: int) -> bool:
            if index == len(s): return current_sum == target
            for j in range(index, len(s)):
                num = int(s[index:j+1])
                if current_sum + num > target: break
                if canPartition(s, target, j+1, current_sum + num): return True
            return False

        punishment_sum = 0
        for i in range(1, n+1):
            square_str = str(i * i)
            if canPartition(square_str, i, 0, 0): punishment_sum += i * i
        return punishment_sum