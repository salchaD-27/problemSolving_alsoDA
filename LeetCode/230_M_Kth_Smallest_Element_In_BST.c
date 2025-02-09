// #include <stdio.h>
// #include <stdlib.h>
// #include <limits.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// void sortedInsert(int* smalls, int k, int val) {
//     if(val < smalls[k-1]) {return;}
//     int i = k - 1;
//     while(i > 0 && smalls[i-1] > val) {
//         smalls[i] = smalls[i-1];
//         i--;
//     }
//     smalls[i] = val;
// }
// void traverseAndFind(struct TreeNode* root, int* smalls, int k) {
//     if (root == NULL) {return;}
//     sortedInsert(smalls, k, root->val);
//     if (root->left != NULL) {traverseAndFind(root->left, smalls, k);}
//     if (root->right != NULL) {traverseAndFind(root->right, smalls, k);}
// }
// int kthSmallest(struct TreeNode* root, int k) {
//     int* smalls = (int*)malloc(k * sizeof(int));
//     for (int i = 0; i < k; i++) {smalls[i] = INT_MAX;}
//     traverseAndFind(root, smalls, k);
//     int result = smalls[k - 1];
//     free(smalls);
//     return result;
// }

#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
void inOrderTraversal(struct TreeNode* root, int* count, int k, int* result) {
    if (root == NULL || *count >= k) {return;}
    inOrderTraversal(root->left, count, k, result);
    (*count)++;
    if (*count == k) {
        *result = root->val;
        return;
    }
    inOrderTraversal(root->right, count, k, result);
}
int kthSmallest(struct TreeNode* root, int k) {
    int count = 0; 
    int result = 0;
    inOrderTraversal(root, &count, k, &result);
    return result;
}