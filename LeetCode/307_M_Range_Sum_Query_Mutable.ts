class NumArray {
    private numArr: number[];
    constructor(nums: number[]) {
        this.numArr = new Array(nums.length); 
        this.numArr[0] = nums[0]; 
        for (let i = 1; i < nums.length; i++){this.numArr[i] = this.numArr[i - 1] + nums[i];}
    }
    update(index: number, val: number): void {
        let originalNum: number = index === 0 ? this.numArr[0] : this.numArr[index] - this.numArr[index - 1];
        let change: number = val - originalNum;
        for (let i = index; i < this.numArr.length; i++){this.numArr[i] += change;}
    }
    sumRange(left: number, right: number): number {return left === 0 ? this.numArr[right] : this.numArr[right] - this.numArr[left - 1];}
}