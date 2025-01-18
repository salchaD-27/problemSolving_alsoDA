#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode* next;
};
int countNodes(struct ListNode* head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->next;
    }
    return count;
}
int* originalList(struct ListNode* head, int n) {
    int* origList = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        origList[i] = head->val;
        head = head->next;
    }
    return origList;
}
struct ListNode* createList(int* arr, int size) {
    if (size == 0) return NULL;
    struct ListNode* head = malloc(sizeof(struct ListNode));
    head->val = arr[0];
    head->next = NULL;
    struct ListNode* current = head;
    for (int i = 1; i < size; i++) {
        current->next = malloc(sizeof(struct ListNode));
        current = current->next;
        current->val = arr[i];
        current->next = NULL;
    }
    return head;
}
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    int n = countNodes(head);
    if (k <= 1 || n < k) return head; 
    int* origList = originalList(head, n); 
    int* ansList = malloc(n * sizeof(int));
    int ansIndex = 0, finalIndex = 0;
    for (int i = k - 1; i < n; i += k) {
        int iter = k;
        int val = i;
        while (iter > 0) {
            ansList[ansIndex++] = origList[val--];
            iter--;
            finalIndex++;
        }
    }
    for (int i = finalIndex; i < n; i++){ansList[ansIndex++] = origList[i];}
    free(origList); 
    head = createList(ansList, n); 
    free(ansList); 
    return head;
}