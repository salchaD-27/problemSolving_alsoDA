func calculateMinimumHP(dungeon [][]int) int {
	rows, cols := len(dungeon), len(dungeon[0])
	dp := make([]int, cols+1)
	for i := range dp {
		dp[i] = math.MaxInt32
	}
	dp[cols-1] = 1
	for i := rows - 1; i >= 0; i-- {
		for j := cols - 1; j >= 0; j-- {
			dp[j] = max(1, min(dp[j], dp[j+1])-dungeon[i][j])
		}
	}
	return dp[0]
}