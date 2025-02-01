function parity(num1:number, num2:number): boolean{
    if((num1%2==0 && num2%2==0) || (num1%2!=0 && num2%2!=0)){return false;}
    return true;
}
function isArraySpecial(nums: number[]): boolean {
    let i:number;
    for(i=0; i<nums.length-1; i++){if(!parity(nums[i], nums[i+1])){return false;}}
    return true;
};