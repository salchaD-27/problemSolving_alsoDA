#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode* next;
};
int countNodes(struct ListNode* head) {
    int count = 0;
    while (head != NULL) {
        head = head->next;
        count++;
    }
    return count;
}
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int targetIndex = countNodes(head) - n;
    if (targetIndex == 0) {
        struct ListNode* temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    struct ListNode* prev = head;
    for (int i = 0; i < targetIndex - 1; i++) {prev = prev->next;}
    struct ListNode* target = prev->next;
    prev->next = target->next;
    free(target);
    return head;
}