class Solution:
    def maximum69Number (self, num: int) -> int:
        num=[i for i in str(num)]
        for i in range(len(num)):
            if num[i]=='6':
                num[i]='9'
                break
        return int(''.join(num))

class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))