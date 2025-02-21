#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct {struct TreeNode* root;} FindElements;
void recoverTree(struct TreeNode* node, int val) {
    if (!node) return;
    node->val = val;
    recoverTree(node->left, 2 * val + 1);
    recoverTree(node->right, 2 * val + 2);
}
FindElements* findElementsCreate(struct TreeNode* root) {
    if (root) {recoverTree(root, 0);}
    FindElements* obj = (FindElements*)malloc(sizeof(FindElements));
    obj->root = root;
    return obj;
}
bool dfs(struct TreeNode* node, int target) {
    if (!node) return false;
    if (node->val == target) return true;
    return dfs(node->left, target) || dfs(node->right, target);
}
bool findElementsFind(FindElements* obj, int target) {return dfs(obj->root, target);}
void findElementsFree(FindElements* obj) {free(obj);}