#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
int getDecimalValue(struct ListNode* head) {
    int num = 0;
    while (head != NULL) {
        num = num * 2 + head->val;
        head = head->next;
    }
    return num;
}