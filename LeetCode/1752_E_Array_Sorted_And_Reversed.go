package main
import "fmt"
func check(nums []int) bool {
	rotation := 1
	for i := 0; i < len(nums)-1; i++ {  
		if nums[i] > nums[i+1] {
			if rotation == 0 {return false}
			rotation--
		}
	}
	if len(nums) > 1 && nums[len(nums)-1] > nums[0] && rotation == 0 {return false}
	return true
}