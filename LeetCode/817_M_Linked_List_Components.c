// #include <stdio.h>
// #include <stdlib.h>
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };
// int getIndex(int* nums, int numsSize, int val){for(int i=0; i<numsSize; i++){if(nums[i]==val){return i;}} return -1;}
// int numComponents(struct ListNode* head, int* nums, int numsSize) {
//     int connected[numsSize];
//     for(int i=0; i<numsSize; i++){connected[i]=0;}
//     while(head->next->next!=NULL){
//         int idx=getIndex(nums, numsSize, head->val);
//         if(nums[idx+1]==head->next->val){
//             connected[idx]=1;
//             connected[idx+1]=1;
//         }
//         head=head->next;
//     }
//     int sum=0;
//     for(int i=0; i<numsSize; i++){sum+=connected[i];}
//     return sum;
// }

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
bool inSet[10001];
int numComponents(struct ListNode* head, int* nums, int numsSize) {
    for (int i = 0; i < 10001; i++) inSet[i] = false;
    for (int i = 0; i < numsSize; i++) {inSet[nums[i]] = true;}
    int count = 0;
    bool inComponent = false;
    while (head != NULL) {
        if (inSet[head->val]) {
            if (!inComponent) {
                count++;
                inComponent = true;
            }
        }
        else{inComponent = false;}
        head = head->next;
    }
    return count;
}