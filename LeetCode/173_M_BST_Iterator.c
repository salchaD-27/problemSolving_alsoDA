#include <stdbool.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct {
    struct TreeNode** stack;
    int top;
    int capacity;
} BSTIterator;

void pushLeft(BSTIterator* obj, struct TreeNode* node) {
    while (node) {
        obj->stack[++obj->top] = node;
        node = node->left;
    }
}
BSTIterator* bSTIteratorCreate(struct TreeNode* root) {
    BSTIterator* obj = (BSTIterator*)malloc(sizeof(BSTIterator));
    obj->capacity = 100;
    obj->stack = (struct TreeNode**)malloc(sizeof(struct TreeNode*) * obj->capacity);
    obj->top = -1;
    pushLeft(obj, root);
    return obj;
}
int bSTIteratorNext(BSTIterator* obj) {
    struct TreeNode* node = obj->stack[obj->top--];
    int val = node->val;
    if (node->right){pushLeft(obj, node->right);}
    return val;
}
bool bSTIteratorHasNext(BSTIterator* obj){return obj->top >= 0;}
void bSTIteratorFree(BSTIterator* obj) {
    free(obj->stack);
    free(obj);
}