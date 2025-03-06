class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1 
        count = 9  
        start = 1
        while n > length * count:
            n -= length * count 
            length += 1         
            count *= 10         
            start *= 10         
        num = start + (n - 1) // length
        return int(str(num)[(n - 1) % length])