import "math"

func maxAbsoluteSum(nums []int) int {
	sum, minSum, maxSum := 0, 0, 0
	ans := 0
	for _, num := range nums {
		sum += num
		maxSum = max(maxSum, sum)
		minSum = min(minSum, sum)
		ans = max(ans, int(math.Abs(float64(maxSum-minSum))))
	}
	return ans
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}