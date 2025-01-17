class Solution:
    def intToRoman(self, num: int) -> str:
        def digits(num):
            digits = 0
            while num != 0:
                num = num // 10
                digits += 1
            return digits
        def ithNum(num, i):
            temp = 0
            power = -1
            for j in range(i):
                temp = num % 10
                num = num // 10
                power += 1
            return temp * (10 ** power)
        def romanRange(num):
            if 1 <= num < 4: return 'I' * num
            if num == 4: return 'IV'
            if 5 <= num < 9: return 'V' + ('I' * (num - 5))
            if num == 9: return 'IX'
            if 10 <= num < 40: return 'X' * (num // 10)
            if 40 <= num < 50: return 'XL'
            if 50 <= num < 90: return 'L' + ('X' * ((num - 50) // 10))
            if 90 <= num < 100: return 'XC'
            if 100 <= num < 400: return 'C' * (num // 100)
            if 400 <= num < 500: return 'CD'
            if 500 <= num < 900: return 'D' + ('C' * ((num - 500) // 100))
            if 900 <= num < 1000: return 'CM'
            if 1000 <= num: return 'M' * (num // 1000)
            return ''
        ans = ''
        for i in range(digits(num), 0, -1):
            ans += romanRange(ithNum(num, i))
        return ans