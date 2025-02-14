// func lengthOfLIS(nums []int) int {
// 	L := 0
// 	R := 0
// 	ans := 0
// 	for R < len(nums) {
// 		if R + 1 < len(nums) && nums[R+1] > nums[R] {R++}else{
// 			temp := R - L + 1
// 			if temp > ans{ans = temp}
// 			L = R + 1
// 			R = L
// 		}
// 	}
// 	temp := R - L + 1
// 	if temp > ans {ans = temp}
// 	return ans
// }

// func lengthOfLIS(nums []int) int {
// 	dp:=make([]int, len(nums))
// 	dp[0]=1
// 	for i:=1; i<len(nums);i++{if(nums[i-1]<=nums[i]){dp[i]=1}else{dp[i]=dp[i-1]+1}}
// 	max := dp[0]
//     for _, num := range dp {if num > max {max = num}}
//     return max-1
// }

func lengthOfLIS(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	dp := make([]int, len(nums))
	for i := range dp {
		dp[i] = 1
	}
	for i := 1; i < len(nums); i++ {
		for j := 0; j < i; j++ {
			if nums[i] > nums[j] {
				dp[i] = max(dp[i], dp[j]+1)
			}
		}
	}
	max := dp[0]
	for _, length := range dp {
		if length > max {
			max = length
		}
	}
	return max
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}