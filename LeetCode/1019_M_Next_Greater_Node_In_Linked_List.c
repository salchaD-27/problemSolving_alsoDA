#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* reverseList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {return head;}
    struct ListNode* newHead = reverseList(head->next);
    head->next->next = head;
    head->next = NULL;
    return newHead;
}
int countNodes(struct ListNode* head) {
    struct ListNode* temp = head;
    int count = 0;
    while (temp != NULL) {
        temp = temp->next;
        count++;
    }
    return count;
}
int* nextLargerNodes(struct ListNode* head, int* returnSize) {
    head = reverseList(head);
    int n = countNodes(head);
    int stack[n];
    int top = -1;
    int* ans = (int*)malloc(sizeof(int) * n);
    int idx = n - 1;
    struct ListNode* temp = head;
    while (temp != NULL) {
        while (top != -1 && stack[top] <= temp->val) {top--;}
        ans[idx--] = top == -1 ? 0 : stack[top];
        stack[++top] = temp->val;
        temp = temp->next;
    }
    *returnSize = n;
    return ans;
}