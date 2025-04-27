#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
// [bottomLeftValue, depth]
int* traverse(struct TreeNode* root, int level) {
    int* result = (int*)malloc(2 * sizeof(int));  
    if (root->left == NULL && root->right == NULL) {
        result[0] = root->val;
        result[1] = level;
        return result;
    }
    int* leftResult = NULL;
    int* rightResult = NULL;
    if (root->left) leftResult = traverse(root->left, level + 1);
    if (root->right) rightResult = traverse(root->right, level + 1);
    if (leftResult && (!rightResult || leftResult[1] >= rightResult[1])) {
        free(rightResult);
        return leftResult;
    } else {
        free(leftResult);
        return rightResult;
    }
}
int findBottomLeftValue(struct TreeNode* root) {
    int* result = traverse(root, 0);
    int val = result[0];
    free(result);
    return val;
}

#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int max(int a, int b) {
    if (a > b) return a;
    else return b;
}
int heightOfTree(struct TreeNode* root) {
    if (!root) return 0;
    return 1 + max(heightOfTree(root->left), heightOfTree(root->right));
}
struct TreeNode* find (struct TreeNode* root, int height) {
    if (root == NULL) return NULL;
    if (height == 0) return root;
    struct TreeNode *leftResult = find(root->left, height - 1);
    if (leftResult != NULL) return leftResult;
    return find(root->right, height - 1);
}
int findBottomLeftValue(struct TreeNode* root) {return find(root, heightOfTree(root)-1)->val;}