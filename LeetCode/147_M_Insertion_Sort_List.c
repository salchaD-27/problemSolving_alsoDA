#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
int countNode(struct ListNode* head) {
    int count = 0;
    while (head) {
        count++;
        head = head->next;
    }
    return count;
}
int removeValInListFromIndex(struct ListNode** head, int index) {
    struct ListNode* temp = *head;
    if (index == 0) {
        *head = (*head)->next;
        int val = temp->val;
        free(temp);
        return val;
    }
    for (int i = 0; i < index - 1; i++){temp = temp->next;}
    struct ListNode* nodeToDelete = temp->next;
    temp->next = nodeToDelete->next;
    int val = nodeToDelete->val;
    free(nodeToDelete);
    return val;
}
struct ListNode* insertionSortInsert(struct ListNode* head, int val) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    if (head == NULL || head->val >= val) {
        newNode->next = head;
        return newNode;
    }
    struct ListNode* temp = head;
    while (temp->next != NULL && temp->next->val < val){temp = temp->next;}
    newNode->next = temp->next;
    temp->next = newNode;
    return head;
}
struct ListNode* insertionSortList(struct ListNode* head) {
    if (head == NULL) return NULL;
    struct ListNode* sorted = NULL;
    int n = countNode(head);
    for (int i = 0; i < n; i++) {
        int temp = removeValInListFromIndex(&head, 0);
        sorted = insertionSortInsert(sorted, temp);
    }
    return sorted;
}