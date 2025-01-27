// #include <stdio.h>
// #include <stdlib.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// struct TreeNode* createTreeNode(int val) {
//     struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
//     newNode->val = val;
//     newNode->left = NULL;
//     newNode->right = NULL;
//     return newNode;
// }
// int getSize(struct TreeNode* root) {
//     if (root == NULL) return 0;
//     return 1 + getSize(root->left) + getSize(root->right);
// }
// void preorderTraversalHelper(struct TreeNode* root, int* result, int* index) {
//     if (root == NULL) return;
//     result[*index] = root->val;
//     (*index)++;
//     preorderTraversalHelper(root->left, result, index);
//     preorderTraversalHelper(root->right, result, index);
// }
// int* preorderTraversal(struct TreeNode* root, int* returnSize) {
//     int size = getSize(root);
//     int* result = (int*)malloc(size * sizeof(int));
//     int index = 0;
//     preorderTraversalHelper(root, result, &index);
//     *returnSize = size;
//     return result;
// }
// struct ListNode* createListNode(int val) {
//     struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
//     newNode->val = val;
//     newNode->next = NULL;
//     return newNode;
// }
// void addNodeToList(struct ListNode** root, int val) {
//     struct ListNode* newNode = createListNode(val);
//     if (*root == NULL){*root = newNode;}
//     else{
//         struct ListNode* temp = *root;
//         while (temp->next != NULL){temp = temp->next;}
//         temp->next = newNode;
//     }
// }
// void flatten(struct TreeNode* root) {
//     int returnSize;
//     int* preorder = preorderTraversal(root, &returnSize);
//     struct ListNode* listHead = NULL;
//     for (int i = 0; i < returnSize; i++){addNodeToList(&listHead, preorder[i]);}
//     struct ListNode* temp = listHead;
//     while (temp != NULL) {
//         printf("%d -> ", temp->val);
//         temp = temp->next;
//     }
//     printf("NULL\n");
//     free(preorder);
//     temp = listHead;
//     while (temp != NULL) {
//         struct ListNode* toDelete = temp;
//         temp = temp->next;
//         free(toDelete);
//     }
// }

#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
void flatten(struct TreeNode* root) {
    if (root == NULL) return;
    struct TreeNode* current = root;
    while (current != NULL) {
        if (current->left != NULL) {
            struct TreeNode* rightmost = current->left;
            while (rightmost->right != NULL){rightmost = rightmost->right;}
            rightmost->right = current->right; 
            current->right = current->left;    
            current->left = NULL;              
        }
        current = current->right;
    }
}