// from typing import List
// class Solution:
//     def singleNumber(self, nums: List[int]) -> List[int]:
//         a=[]
//         b=[]
//         lastRand=0
//         for num in nums:
//             if(num in a): b.append(num)
//             elif(num in b): a.append(num)
//             elif(num not in a and num not in b):
//                 if(lastRand): a.append(num)
//                 else: 
//                     b.append(num)
//                     lastRand+=1
//         xor_result1, xor_result2 = 0,0
//         for num in a:
//             xor_result1 ^= num
//         for num in b:
//             xor_result2 ^= num
//         return [xor_result1, xor_result2]
            
function singleNumber(nums: number[]): number[] {
    let xor_result:number=0
    for(let i=0; i<nums.length; i++){xor_result ^= nums[i]}
    let diff = xor_result & -xor_result
    let num1=0, num2=0
    for(let i=0; i<nums.length; i++){
        if(nums[i]&diff){num1 ^= nums[i]}
        else{num2 ^= nums[i]}
    }
    return [num1, num2]
};