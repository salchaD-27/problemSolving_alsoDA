# 588878843
# 5 8 88788 4 3
# 58,85,43,34,55,88,33,44
# 58,85,43,34

# class Solution:
#     def nearestPalindromic(self, n: str) -> str:
#         if len(n)<2: return str(int(n)-1)
#         modifyIdx=0
#         for i in range(len(n)//2+1):
#             if(n[i]!=n[-i-1]): modifyIdx+=1
#         baseNum=n[modifyIdx:len(n)-modifyIdx]
#         possFront=n[:modifyIdx]
#         possBack=n[len(n)-modifyIdx:]
#         str1=str(possFront+baseNum+possFront[::-1])
#         str2=str(possBack+baseNum+possBack[::-1])
#         return str1 if abs(int(str1)-int(n))<abs(int(str2)-int(n)) else str2

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1: return str(int(n)-1)
        candidates = set()
        half_len = len(n) // 2
        prefix = n[:half_len + (len(n) % 2)] 
        palindrome = prefix + prefix[::-1][len(n) % 2:]
        candidates.add(palindrome)
        smaller_prefix = str(int(prefix) - 1)
        larger_prefix = str(int(prefix) + 1)
        candidates.add(smaller_prefix + smaller_prefix[::-1][len(n) % 2:])
        candidates.add(larger_prefix + larger_prefix[::-1][len(n) % 2:])
        candidates.add('9' * (len(n) - 1)) 
        candidates.add('1' + '0' * (len(n) - 1) + '1') 
        min_diff = float('inf')
        nearest_palindrome = None
        for candidate in candidates:
            if candidate != n: 
                diff = abs(int(candidate) - int(n))
                if diff < min_diff or (diff == min_diff and int(candidate) < int(nearest_palindrome)):
                    min_diff = diff
                    nearest_palindrome = candidate
        return nearest_palindrome