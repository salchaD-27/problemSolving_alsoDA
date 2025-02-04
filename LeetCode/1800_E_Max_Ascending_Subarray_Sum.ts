function maxAscendingSum(nums: number[]): number {
    let ans = 0, temp = nums[0];  
    for (let i = 1; i < nums.length; i++) {
        if (nums[i - 1] < nums[i]) {temp += nums[i];} 
        else {
            ans=(ans>temp)?ans:temp
            temp = nums[i];  
        }
    }
    return (ans>temp)?ans:temp
}