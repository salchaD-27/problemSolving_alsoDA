# type MedianFinder struct{ dataStream []int }

# func Constructor() MedianFinder { return MedianFinder{dataStream: []int{}} }
# func (this *MedianFinder) AddNum(num int) {
# 	index := sort.SearchInts(this.dataStream, num)
# 	this.dataStream = append(this.dataStream[:index], append([]int{num}, this.dataStream[index:]...)...)
# }
# func (this *MedianFinder) FindMedian() float64 {
# 	n := len(this.dataStream)
# 	if n%2 == 1 {
# 		return float64(this.dataStream[n/2])
# 	}
# 	return (float64(this.dataStream[n/2-1]) + float64(this.dataStream[n/2])) / 2
# }

import heapq
class MedianFinder:
    def __init__(self):
        self.low = []
        self.high = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.low) < len(self.high): heapq.heappush(self.low, -heapq.heappop(self.high))
    def findMedian(self) -> float:
        if len(self.low) > len(self.high): return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2.0