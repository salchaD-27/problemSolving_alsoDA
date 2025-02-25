import (
	"sort"
)

func topKFrequent(nums []int, k int) []int {
	count := make(map[int]int)
	for _, num := range nums {
		count[num]++
	}
	keys := make([]int, 0, len(count))
	for num := range count {
		keys = append(keys, num)
	}
	sort.Slice(keys, func(i, j int) bool {
		return count[keys[i]] > count[keys[j]]
	})
	return keys[:k]
}