#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int getHeight(struct TreeNode* root) {
    if (!root) return -1;
    int left = getHeight(root->left);
    int right = getHeight(root->right);
    return 1 + (left > right ? left : right);
}
void fillMatrix(char*** res, struct TreeNode* root, int row, int col, int height, int offset) {
    if (!root) return;
    char* valStr = (char*)malloc(12);
    sprintf(valStr, "%d", root->val);
    res[row][col] = valStr;
    int nextOffset = 0;
    if (height - row - 1 >= 0) nextOffset = 1 << (height - row - 1);
    if (root->left) fillMatrix(res, root->left, row + 1, col - nextOffset, height, offset);
    if (root->right) fillMatrix(res, root->right, row + 1, col + nextOffset, height, offset);
}
char*** printTree(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    int height = getHeight(root);
    int rows = height + 1;
    int cols = (1 << (height + 1)) - 1;
    char*** res = (char***)malloc(rows * sizeof(char**));
    *returnColumnSizes = (int*)malloc(rows * sizeof(int));
    for (int i = 0; i < rows; i++) {
        res[i] = (char**)malloc(cols * sizeof(char*));
        for (int j = 0; j < cols; j++) {res[i][j] = strdup("");}
        (*returnColumnSizes)[i] = cols;
    }
    fillMatrix(res, root, 0, (cols - 1) / 2, height, cols / 2);
    *returnSize = rows;
    return res;
}