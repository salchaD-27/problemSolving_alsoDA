// n=6
// 1 2 3 4 5 6
// 1 1 1 1 1 1 (1)
// 1 0 1 0 1 0 (2)
// 1 0 0 0 1 1 (3)
// 1 0 0 1 1 1 (4)
// 1 0 0 1 0 1 (5)
// 1 0 0 1 0 0 (6)
// 1     4     (2)
import "math"

func bulbSwitch(n int) int { return int(math.Sqrt(float64(n))) }