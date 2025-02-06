# func prime(n int) bool {
#     if n < 2 {return false}
#     for i := 2; i <= int(math.Sqrt(float64(n))); i++ {if n%i == 0 {return false}}
#     return true
# }
# func countPrimes(n int) int {
#     if n <= 2 {return 0}
#     count := 0
#     for i := 2; i < n; i++ {if prime(i){count++}}
#     return count
# }

from typing import List
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return sum(is_prime)