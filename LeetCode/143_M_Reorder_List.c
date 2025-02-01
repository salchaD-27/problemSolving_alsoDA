#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* findMiddle(struct ListNode* head) {
    struct ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *prev = NULL, *curr = head, *next;
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
void reorderList(struct ListNode* head) {
    if (!head || !head->next) return;
    struct ListNode* mid = findMiddle(head);
    struct ListNode* secondHalf = mid->next;
    mid->next = NULL;
    secondHalf = reverseList(secondHalf);
    struct ListNode* firstHalf = head;
    while (firstHalf && secondHalf) {
        struct ListNode* temp1 = firstHalf->next;
        struct ListNode* temp2 = secondHalf->next;
        firstHalf->next = secondHalf;
        secondHalf->next = temp1;
        firstHalf = temp1;
        secondHalf = temp2;
    }
}