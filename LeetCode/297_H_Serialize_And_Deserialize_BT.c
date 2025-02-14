#include <stdio.h>
#include <stdlib.h>
#define MAX_NODES 10000
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct Queue {
    struct TreeNode *data[MAX_NODES];
    int front, rear;
};
void initQueue(struct Queue *q){q->front = q->rear = 0;}
int isEmpty(struct Queue *q){return q->front == q->rear;}
void enqueue(struct Queue *q, struct TreeNode *node){if (q->rear < MAX_NODES){q->data[q->rear++] = node;}}
struct TreeNode *dequeue(struct Queue *q) {
    if (!isEmpty(q)){return q->data[q->front++];}
    return NULL;
}
char* serialize(struct TreeNode* root){
    if (!root) return "_";
    struct Queue q;
    initQueue(&q);
    enqueue(&q, root);
    char *result = (char *)malloc(MAX_NODES * 5);
    result[0] = '\0';
    while (!isEmpty(&q)) {
        struct TreeNode *node = dequeue(&q);
        if (node) {
            char buffer[12];
            sprintf(buffer, "%d,", node->val);
            strcat(result, buffer);
            enqueue(&q, node->left);
            enqueue(&q, node->right);
        }else{strcat(result, "_,");}
    }
    int len = strlen(result);
    if (len > 0 && result[len - 1] == ','){result[len - 1] = '\0';}
    return result;
}
struct TreeNode *newNode(int val) {
    struct TreeNode *node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}
struct TreeNode* deserialize(char* data) {
    if (!data || strcmp(data, "_") == 0) return NULL;
    char *token = strtok(data, ",");
    if (!token) return NULL;
    struct TreeNode *root = newNode(atoi(token));
    struct Queue q;
    initQueue(&q);
    enqueue(&q, root);
    while (!isEmpty(&q)) {
        struct TreeNode *parent = dequeue(&q);
        token = strtok(NULL, ",");
        if (token) {
            if (strcmp(token, "_") != 0) {
                parent->left = newNode(atoi(token));
                enqueue(&q, parent->left);
            }
        }
        token = strtok(NULL, ",");
        if (token) {
            if (strcmp(token, "_") != 0) {
                parent->right = newNode(atoi(token));
                enqueue(&q, parent->right);
            }
        }
    }
    return root;
}