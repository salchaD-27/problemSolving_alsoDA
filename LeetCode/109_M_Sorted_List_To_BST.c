#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct ListNode* findMiddle(struct ListNode* head) {
    struct ListNode *slow = head, *fast = head;
    struct ListNode *prev = NULL;    
    while (fast != NULL && fast->next != NULL) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }
    if (prev != NULL){prev->next = NULL;}
    return slow;
}
struct TreeNode* sortedListToBST(struct ListNode* head) {
    if (head == NULL){return NULL;}
    struct ListNode* mid = findMiddle(head);
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = mid->val;
    node->left = NULL;
    node->right = NULL;
    if (head == mid){return node;}
    node->left = sortedListToBST(head);
    node->right = sortedListToBST(mid->next);
    return node;
}