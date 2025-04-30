class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        nums1=num1.split('+')
        if(nums1[0][0]=='-'): a1=-int(nums1[0][1:])
        else: a1=int(nums1[0])
        if(nums1[-1][0]=='-'): i1=-int(nums1[-1][1:-1])
        else: i1=int(nums1[-1][:-1])
        nums2=num2.split('+')
        if(nums2[0][0]=='-'): a2=-int(nums2[0][1:])
        else: a2=int(nums2[0])
        if(nums2[-1][0]=='-'): i2=-int(nums2[-1][1:-1])
        else: i2=int(nums2[-1][:-1])
        a3=(a1*a2)-(i1*i2)
        i3=(a1*i2)+(a2*i1)
        return str(a3)+'+'+str(i3)+'i'