// func rangeBitwiseAnd(left int, right int) int {
//     temp:=left
// 	for i:=left+1; i<=right; i++ {temp=temp&i}
// 	return temp
// }

func rangeBitwiseAnd(left int, right int) int {
	for left < right {
		right &= right - 1
	}
	return left & right
}