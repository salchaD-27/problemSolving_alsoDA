// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// char* tree2str(struct TreeNode* root) {
//     if (!root) return "";
//     char* res = (char*)malloc(10000);
//     char* leftStr;
//     char* rightStr;
//     sprintf(res, "%d", root->val);
//     if (root->left || root->right) {
//         leftStr = tree2str(root->left);
//         strcat(res, "(");
//         strcat(res, leftStr);
//         strcat(res, ")");
//         if (root->left) free(leftStr);
//     }
//     if (root->right) {
//         rightStr = tree2str(root->right);
//         strcat(res, "(");
//         strcat(res, rightStr);
//         strcat(res, ")");
//         free(rightStr);
//     }
//     return res;
// }

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
char* tree2str(struct TreeNode* root) {
    if (!root) return strdup("");
    char valBuf[12];
    sprintf(valBuf, "%d", root->val);
    char *leftStr = NULL, *rightStr = NULL;
    if (root->left) leftStr = tree2str(root->left);
    if (root->right) rightStr = tree2str(root->right);
    int totalLen = strlen(valBuf) + 1;
    if (root->left || root->right) totalLen += 2 + (leftStr ? strlen(leftStr) : 0); // (left)
    if (root->right) totalLen += 2 + strlen(rightStr);  // (right)
    char* res = (char*)malloc(totalLen + 1);
    strcpy(res, valBuf);
    if (root->left || root->right) {
        strcat(res, "(");
        if (leftStr) strcat(res, leftStr);
        strcat(res, ")");
    }
    if (root->right) {
        strcat(res, "(");
        strcat(res, rightStr);
        strcat(res, ")");
    }
    if (leftStr) free(leftStr);
    if (rightStr) free(rightStr);
    return res;
}