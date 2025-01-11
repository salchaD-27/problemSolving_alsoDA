#include <stdio.h>

int shortestSubarray(int* nums, int numsSize, int k) {
    for(int i=0; i<numsSize; i++){
        int len=0;
        while(len!=numsSize){
            int prev=i-1, next=i+1;
            int sum=nums[i];
            len++;
            if(sum==k){return len;}
            if(prev>=0){
                sum+=nums[prev];
                prev--;
                len++;
                if(sum==k){return len;}
            }
            if(next<numsSize){
                sum+=nums[next];
                next++;
                len++;
                if(sum==k){return len;}
            }
        }
    }
    return -1;
}