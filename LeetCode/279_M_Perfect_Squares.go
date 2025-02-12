// func isPerfectSquare(n int) bool {
//     sqrtN := int(math.Sqrt(float64(n)))
//     return sqrtN*sqrtN == n
// }
// func numSquares(n int) int {
//     count:= 0
//     for n > 0 {
//         i := int(math.Sqrt(float64(n)))
//         largestPS := i * i
//         n -= largestPS
//         count++
//     }
//     return count
// }

func numSquares(n int) int {
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = i
	}
	for i := 1; i <= n; i++ {
		for j := 1; j*j <= i; j++ {
			dp[i] = min(dp[i], dp[i-j*j]+1)
		}
	}
	return dp[n]
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}