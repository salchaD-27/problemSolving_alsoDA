func productExceptSelf(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	ans[0] = 1
	for i := 1; i < n; i++ {
		ans[i] = ans[i-1] * nums[i-1]
	}
	suffix := 1
	for i := n - 1; i >= 0; i-- {
		ans[i] *= suffix
		suffix *= nums[i]
	}
	return ans
}