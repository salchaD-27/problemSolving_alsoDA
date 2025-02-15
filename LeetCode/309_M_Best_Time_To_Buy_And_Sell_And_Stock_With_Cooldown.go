func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func maxProfit(prices []int) int {
	if len(prices) < 2 {
		return 0
	}
	n := len(prices)
	buy := make([]int, n)
	sell := make([]int, n)
	cooldown := make([]int, n)

	buy[0] = -prices[0]
	sell[0] = 0
	cooldown[0] = 0
	for i := 1; i < n; i++ {
		buy[i] = max(buy[i-1], cooldown[i-1]-prices[i])
		sell[i] = buy[i-1] + prices[i]
		cooldown[i] = max(cooldown[i-1], sell[i-1])
	}
	return max(sell[n-1], cooldown[n-1])
}