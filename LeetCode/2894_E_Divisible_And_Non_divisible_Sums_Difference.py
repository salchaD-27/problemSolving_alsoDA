class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1,num2=0,0
        for i in range(1, n+1):
            if i%m==0: num2+=i
            else: num1+=i
        return num1-num2
    
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num2 = 0
        multiple = 0
        while multiple + m <= n:
            multiple += m
            num2 += multiple
        range_sum = (n*(n+1)) // 2
        num1 = range_sum - num2
        return num1 - num2