#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
#pragma GCC optimize("O3, unroll-loops")
static struct ListNode* modifiedList(int* nums, int n, struct ListNode* head) {
    bool hasN[100001]={0};
    for(int i=0; i<n; i++) hasN[nums[i]]=1;
    struct ListNode dummy={0, head};
    struct ListNode* prev=&dummy;
    for(struct ListNode* curr=head; curr; curr=curr->next){
        if (hasN[curr->val]) prev->next=curr->next;
        else  prev=prev->next;
    }
    return dummy.next;
}