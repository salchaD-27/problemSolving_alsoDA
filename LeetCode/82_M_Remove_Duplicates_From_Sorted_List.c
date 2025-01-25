#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (head == NULL) return NULL;
    struct ListNode* temp = head;
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode* prev = dummy;
    while (temp != NULL) {
        if (temp->next != NULL && temp->val == temp->next->val) {
            while (temp->next != NULL && temp->val == temp->next->val){temp = temp->next;}
            prev->next = temp->next;
        }
        else{prev = prev->next; }
        temp = temp->next;
    }
    struct ListNode* result = dummy->next;
    free(dummy); 
    return result;  
}