// #include <stdlib.h>
// #include <stdbool.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// typedef struct QueueNode {
//     struct TreeNode* node;
//     struct QueueNode* next;
// } QueueNode;
// typedef struct Queue {
//     QueueNode* front;
//     QueueNode* rear;
// } Queue;
// Queue* createQueue() {
//     Queue* queue = (Queue*)malloc(sizeof(Queue));
//     queue->front = NULL;
//     queue->rear = NULL;
//     return queue;
// }
// void enqueue(Queue* queue, struct TreeNode* node) {
//     QueueNode* newNode = (QueueNode*)malloc(sizeof(QueueNode));
//     newNode->node = node;
//     newNode->next = NULL;
//     if (queue->rear){queue->rear->next = newNode;}
//     queue->rear = newNode;
//     if (!queue->front){queue->front = newNode;}
// }
// struct TreeNode* dequeue(Queue* queue) {
//     if (!queue->front){return NULL;}
//     QueueNode* temp = queue->front;
//     struct TreeNode* node = temp->node;
//     queue->front = queue->front->next;
//     if (!queue->front){queue->rear = NULL;}
//     free(temp);
//     return node;
// }
// bool isQueueEmpty(Queue* queue){return queue->front == NULL;}
// void freeQueue(Queue* queue) {
//     while (!isQueueEmpty(queue)){dequeue(queue);}
//     free(queue);
// }
// int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
//     if (!root) {
//         *returnSize = 0;
//         *returnColumnSizes = NULL;
//         return NULL;
//     }
//     int** result = (int**)malloc(1000 * sizeof(int*));  
//     *returnColumnSizes = (int*)malloc(1000 * sizeof(int));
//     *returnSize = 0;
//     Queue* queue = createQueue();
//     enqueue(queue, root);
//     while (!isQueueEmpty(queue)) {
//         int levelSize = 0;
//         QueueNode* temp = queue->front;
//         while (temp) {
//             levelSize++;
//             temp = temp->next;
//         }
//         result[*returnSize] = (int*)malloc(levelSize * sizeof(int));
//         (*returnColumnSizes)[*returnSize] = levelSize;
//         for (int i = 0; i < levelSize; i++) {
//             struct TreeNode* current = dequeue(queue);
//             result[*returnSize][i] = current->val;
//             if (current->left){enqueue(queue, current->left);}
//             if (current->right){enqueue(queue, current->right);}
//         }
//         (*returnSize)++;
//     }
//     freeQueue(queue);
//     return result;
// }

#include <stdlib.h>
#include <stdbool.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct QueueNode {
    struct TreeNode* node;
    struct QueueNode* next;
} QueueNode;
typedef struct Queue {
    QueueNode* front;
    QueueNode* rear;
} Queue;
Queue* createQueue() {
    Queue* queue = (Queue*)malloc(sizeof(Queue));
    queue->front = NULL;
    queue->rear = NULL;
    return queue;
}
void enqueue(Queue* queue, struct TreeNode* node) {
    QueueNode* newNode = (QueueNode*)malloc(sizeof(QueueNode));
    newNode->node = node;
    newNode->next = NULL;
    if (queue->rear){queue->rear->next = newNode;}
    queue->rear = newNode;
    if (!queue->front){queue->front = newNode;}
}
struct TreeNode* dequeue(Queue* queue) {
    if (!queue->front){return NULL;}
    QueueNode* temp = queue->front;
    struct TreeNode* node = temp->node;
    queue->front = queue->front->next;
    if (!queue->front){queue->rear = NULL;}
    free(temp);
    return node;
}
bool isQueueEmpty(Queue* queue){return queue->front == NULL;}
void freeQueue(Queue* queue) {
    while (!isQueueEmpty(queue)){dequeue(queue);}
    free(queue);
}
int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if (!root) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    int capacity = 10;
    int** result = (int**)malloc(capacity * sizeof(int*));
    *returnColumnSizes = (int*)malloc(capacity * sizeof(int));
    *returnSize = 0;
    Queue* queue = createQueue();
    enqueue(queue, root);
    while (!isQueueEmpty(queue)) {
        int levelSize = 0;
        QueueNode* temp = queue->front;
        while (temp) {
            levelSize++;
            temp = temp->next;
        }
        if (*returnSize >= capacity) {
            capacity *= 2;
            result = (int**)realloc(result, capacity * sizeof(int*));
            *returnColumnSizes = (int*)realloc(*returnColumnSizes, capacity * sizeof(int));
        }
        result[*returnSize] = (int*)malloc(levelSize * sizeof(int));
        (*returnColumnSizes)[*returnSize] = levelSize;
        for (int i = 0; i < levelSize; i++) {
            struct TreeNode* current = dequeue(queue);
            result[*returnSize][i] = current->val;
            if (current->left){enqueue(queue, current->left);}
            if (current->right){enqueue(queue, current->right);}
        }
        (*returnSize)++;
    }
    freeQueue(queue);
    return result;
}