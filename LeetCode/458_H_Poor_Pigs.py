class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        count = 0
        Btest = 1
        while Btest < buckets:
            count += 1
            Btest *= (minutesToTest // minutesToDie) + 1
        return count