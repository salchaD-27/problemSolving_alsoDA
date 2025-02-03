package main
import "fmt"
func findPeakElement(nums []int) int {
    n := len(nums)
    for i := 0; i < n; i++ {
        if i == 0 {
            if n == 1 || nums[i] > nums[i+1] {return i}
        } else if i == n-1 {
            if nums[i] > nums[i-1] {return i}
        } else {
            if nums[i] > nums[i-1] && nums[i] > nums[i+1] {return i}
        }
    }
    return -1
}