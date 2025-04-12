# import math
# from collections import Counter
# class Solution:
#     def countGoodIntegers(self, n: int, k: int) -> int:
#         def possPalindrome(num):
#             freq=Counter(str(num))
#             temp=1
#             for val in freq.values():
#                 if val%2!=0 and temp!=0: temp-=1
#                 elif val%2!=0 and temp==0: return False
#                 else: continue
#             return True
#         count=0
#         start= 10**(n-1)
#         end= 10**n
#         for i in range(start, end):
#             if(i%k==0 and possPalindrome(i)): count+=1
#         return count

# from collections import Counter
# from itertools import permutations
# class Solution:
#     def countGoodIntegers(self, n: int, k: int) -> int:
#         def can_form_palindrome(counter):
#             odd = sum(1 for v in counter.values() if v % 2 == 1)
#             return odd <= 1
#         def generate_palindromic_permutations(s):
#             counter = Counter(s)
#             if not can_form_palindrome(counter): return set()
#             half = []
#             mid = ''
#             for digit, count in counter.items():
#                 if count % 2 == 1: mid = digit
#                 half.extend([digit] * (count // 2))
#             if not half and not mid: return set()
#             half_perms = set(permutations(half))
#             palindromes = set()
#             for perm in half_perms:
#                 if not perm or perm[0] == '0': continue
#                 half_str = ''.join(perm)
#                 pal = half_str + mid + half_str[::-1]
#                 palindromes.add(int(pal))
#             return palindromes
#         count = 0
#         if n == 1:
#             for i in range(1, 10):
#                 if i % k == 0: count += 1
#             return count
#         for num in range(10**(n - 1), 10**n):
#             s = str(num)
#             palindromes = generate_palindromic_permutations(s)
#             if any(p % k == 0 for p in palindromes): count += 1
#         return count

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        dictionary = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            palindromicInteger = int(s)
            if palindromicInteger % k == 0:
                sorted_s = "".join(sorted(s))
                dictionary.add(sorted_s)
        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in dictionary:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            tot = (n - cnt[0]) * fac[n - 1]
            for x in cnt:
                tot //= fac[x]
            ans += tot
        return ans