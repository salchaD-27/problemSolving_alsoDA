#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
int countNodes(struct ListNode* root) {
    int count = 0;
    while (root) {
        count++;
        root = root->next;
    }
    return count;
}
struct ListNode** splitListToParts(struct ListNode* head, int k, int* returnSize) {
    *returnSize = k;
    struct ListNode** result = (struct ListNode**)malloc(sizeof(struct ListNode*) * k);
    int total = countNodes(head);
    int minPartSize = total / k;
    int extraNodes = total % k;
    for (int i = 0; i < k; i++) {
        result[i] = head;
        int partSize = minPartSize + (i < extraNodes ? 1 : 0);
        for (int j = 0; j < partSize - 1; j++) {if (head) head = head->next;}
        if (head) {
            struct ListNode* next = head->next;
            head->next = NULL;
            head = next;
        }
    }
    return result;
}