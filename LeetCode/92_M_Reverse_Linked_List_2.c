#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    if (head == NULL || left == right) return head;
    struct ListNode dummy; 
    dummy.next = head;
    struct ListNode *prev = &dummy;
    for (int i = 1; i < left; i++){prev = prev->next;}

    struct ListNode *curr = prev->next;
    struct ListNode *tail = curr;      
    struct ListNode *next = NULL;
    for (int i = 0; i < right - left + 1; i++) {
        next = curr->next;
        curr->next = prev->next;
        prev->next = curr;
        curr = next;
    }
    tail->next = curr;
    return dummy.next;
}