#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAX_LEN 10001
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct QueueNode {
    struct TreeNode* treeNode;
    struct QueueNode* next;
} QueueNode;
typedef struct Queue {
    QueueNode *front, *rear;
} Queue;
Queue* createQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = NULL;
    return q;
}
void enqueue(Queue* q, struct TreeNode* node) {
    QueueNode* temp = (QueueNode*)malloc(sizeof(QueueNode));
    temp->treeNode = node;
    temp->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = temp;
        return;
    }
    q->rear->next = temp;
    q->rear = temp;
}
struct TreeNode* dequeue(Queue* q) {
    if (q->front == NULL) return NULL;
    QueueNode* temp = q->front;
    struct TreeNode* node = temp->treeNode;
    q->front = q->front->next;
    if (q->front == NULL) q->rear = NULL;
    free(temp);
    return node;
}
int isEmpty(Queue* q) {return q->front == NULL;}
char* serialize(struct TreeNode* root) {
    if (!root) {
        char* empty = (char*)malloc(2);
        strcpy(empty, "");
        return empty;
    }
    int capacity = 1024;
    char* result = (char*)malloc(capacity);
    result[0] = '\0';
    int len = 0;
    Queue* q = createQueue();
    enqueue(q, root);
    while (!isEmpty(q)) {
        struct TreeNode* node = dequeue(q);
        char buffer[32];
        int written = snprintf(buffer, sizeof(buffer), "%d ", node->val);
        if (len + written + 1 >= capacity) {
            capacity *= 2;
            result = realloc(result, capacity);
            if (!result) {
                fprintf(stderr, "Memory allocation failed\n");
                exit(EXIT_FAILURE);
            }
        }
        strcat(result, buffer);
        len += written;
        if (node->left) enqueue(q, node->left);
        if (node->right) enqueue(q, node->right);
    }
    if (len > 0 && result[len - 1] == ' ') result[len - 1] = '\0';
    return result;
}
struct TreeNode* createNode(int val) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = node->right = NULL;
    return node;
}
struct TreeNode* insertBST(struct TreeNode* root, int val) {
    if (!root) return createNode(val);
    if (val < root->val) root->left = insertBST(root->left, val);
    else root->right = insertBST(root->right, val);
    return root;
}
struct TreeNode* deserialize(char* str) {
    struct TreeNode* root = NULL;
    int num = 0;
    int i = 0;
    int len = strlen(str);
    char buffer[20];
    int bufIndex = 0;
    while (i <= len) {
        if (isdigit(str[i]) || str[i] == '-') {
            buffer[bufIndex++] = str[i];
        } else if ((str[i] == ' ' || str[i] == '\0') && bufIndex > 0) {
            buffer[bufIndex] = '\0';
            int val = atoi(buffer);
            root = insertBST(root, val);
            bufIndex = 0;
        }
        i++;
    }
    return root;
}

// char* serialize(struct TreeNode* root) {return (char*) root;}
// struct TreeNode* deserialize(char* data) {return (struct TreeNode*) data;}