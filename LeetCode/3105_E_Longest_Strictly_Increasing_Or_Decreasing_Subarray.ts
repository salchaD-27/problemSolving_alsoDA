function longestMonotonicSubarray(nums: number[]): number {
    let L:number=0, R:number=0, longInc:number=0, longDec:number=0
    while (R < nums.length - 1) {
        if (nums[R + 1] > nums[R]){R++;} 
        else {
            longInc = (longInc<(R-L+1)?(R-L+1):longInc)
            L = R + 1;
            R = L;
        }
    }
    longInc = (longInc<(R-L+1)?(R-L+1):longInc)
    L = 0, R = 0;
    while (R < nums.length - 1) {
        if (nums[R + 1] < nums[R]){R++;} 
        else {
            longDec = (longDec<(R-L+1)?(R-L+1):longDec)
            L = R + 1;
            R = L;
        }
    }
    longDec = (longDec<(R-L+1)?(R-L+1):longDec)
    return longInc>longDec?longInc:longDec
}