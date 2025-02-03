package main
import "fmt"
func findMin(nums []int) int {
    if(nums[len(nums)-1]<=nums[0]){
		var i=len(nums)-1
		for i > 0 && nums[i] >= nums[i-1] {i--}
		return nums[i]
	}else{return nums[0]}
}