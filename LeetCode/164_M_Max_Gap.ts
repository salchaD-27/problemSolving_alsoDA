function maximumGap(nums: number[]): number {
    if(nums.length<2){return 0}
    let max:number=0
    nums.sort((a, b) => a - b)
    for(let i=0; i<nums.length-1; i++){max=(max>(nums[i+1]-nums[i])?max:(nums[i+1]-nums[i]))}
    return max
};