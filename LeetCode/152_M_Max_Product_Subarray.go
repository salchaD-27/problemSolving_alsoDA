// package main
// import (
//     "fmt"
//     "math"
// )
// func maxProduct(nums []int) int {
//     var sum = 0
//     var ans = math.MinInt
//     for i=0; i<len(nums); i++ {
//         sum*=nums[i];
//         if(sum>ans){ans=sum;}
//         if(sum<1){sum=0;}
//     }
//     return ans;
// }

package main
import (
    "fmt"
    "math"
)
func maxProduct(nums []int) int {
    if len(nums) == 0 {return 0}
    maxProd := nums[0]
    minProd := nums[0]
    ans := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] < 0 {maxProd, minProd = minProd, maxProd}
        maxProd = int(math.Max(float64(nums[i]), float64(maxProd*nums[i])))
        minProd = int(math.Min(float64(nums[i]), float64(minProd*nums[i])))
        ans = int(math.Max(float64(ans), float64(maxProd)))
    }
    return ans
}