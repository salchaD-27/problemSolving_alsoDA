#include <stdio.h>
#include <stdlib.h>
#define MAX_QUEUE 10000
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct {
    struct TreeNode* node;
    unsigned long long index;
} QueueNode;
QueueNode queue[MAX_QUEUE];
int front = 0, rear = 0;
void enqueue(struct TreeNode* node, unsigned long long index) {queue[rear++] = (QueueNode){node, index};}
QueueNode dequeue() {return queue[front++];}
int isEmpty() {return front == rear;}
int widthOfBinaryTree(struct TreeNode* root) {
    if (!root) return 0;
    front = rear = 0;
    enqueue(root, 0);
    int maxWidth = 0;
    while (!isEmpty()) {
        int levelSize = rear - front;
        unsigned long long start = queue[front].index;
        unsigned long long end = start;
        for (int i = 0; i < levelSize; ++i) {
            QueueNode curr = dequeue();
            unsigned long long idx = curr.index - start;
            if (i == levelSize - 1) end = curr.index;
            if (curr.node->left) enqueue(curr.node->left, 2 * idx);
            if (curr.node->right) enqueue(curr.node->right, 2 * idx + 1);
        }
        int width = (int)(end - start + 1);
        if (width > maxWidth) maxWidth = width;
    }
    return maxWidth;
}