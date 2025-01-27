# #include <stdlib.h>
# #include <stdbool.h>
# struct TreeNode {
#     int val;
#     struct TreeNode *left;
#     struct TreeNode *right;
# };
# typedef struct QueueNode {
#     struct TreeNode* node;
#     struct QueueNode* next;
# } QueueNode;
# typedef struct Queue {
#     QueueNode* front;
#     QueueNode* rear;
# } Queue;
# Queue* createQueue() {
#     Queue* queue = (Queue*)malloc(sizeof(Queue));
#     queue->front = NULL;
#     queue->rear = NULL;
#     return queue;
# }
# void enqueue(Queue* queue, struct TreeNode* node) {
#     QueueNode* newNode = (QueueNode*)malloc(sizeof(QueueNode));
#     newNode->node = node;
#     newNode->next = NULL;
#     if (queue->rear){queue->rear->next = newNode;}
#     queue->rear = newNode;
#     if (!queue->front){queue->front = newNode;}
# }
# struct TreeNode* dequeue(Queue* queue) {
#     if (!queue->front){return NULL;}
#     QueueNode* temp = queue->front;
#     struct TreeNode* node = temp->node;
#     queue->front = queue->front->next;
#     if (!queue->front){queue->rear = NULL;}
#     free(temp);
#     return node;
# }
# bool isQueueEmpty(Queue* queue){return queue->front == NULL;}
# void freeQueue(Queue* queue) {
#     while (!isQueueEmpty(queue)){dequeue(queue);}
#     free(queue);
# }
# int** levelOrderBottom(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
#     if (!root) {
#         *returnSize = 0;
#         *returnColumnSizes = NULL;
#         return NULL;
#     }
#     int capacity = 10;
#     int** result = (int**)malloc(capacity * sizeof(int*));
#     *returnColumnSizes = (int*)malloc(capacity * sizeof(int));
#     *returnSize = 0;
#     Queue* queue = createQueue();
#     enqueue(queue, root);
#     while (!isQueueEmpty(queue)) {
#         int levelSize = 0;
#         QueueNode* temp = queue->front;
#         while (temp) {
#             levelSize++;
#             temp = temp->next;
#         }
#         if (*returnSize >= capacity) {
#             capacity *= 2;
#             result = (int**)realloc(result, capacity * sizeof(int*));
#             *returnColumnSizes = (int*)realloc(*returnColumnSizes, capacity * sizeof(int));
#         }
#         result[*returnSize] = (int*)malloc(levelSize * sizeof(int));
#         (*returnColumnSizes)[*returnSize] = levelSize;
#         for (int i = 0; i < levelSize; i++) {
#             struct TreeNode* current = dequeue(queue);
#             result[*returnSize][i] = current->val;
#             if (current->left){enqueue(queue, current->left);}
#             if (current->right){enqueue(queue, current->right);}
#         }
#         (*returnSize)++;
#     }
#     freeQueue(queue);

#     int start = 0;
#     int end = *returnSize - 1;
#     while (start < end) {
#         int* temp = result[start];
#         result[start] = result[end];
#         result[end] = temp;
#         start++;
#         end--;
#     }
#     return result;
# }

from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        result = []
        queue = deque([root])
        while queue:
            level_values = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft() 
                level_values.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level_values)
        return result[::-1]