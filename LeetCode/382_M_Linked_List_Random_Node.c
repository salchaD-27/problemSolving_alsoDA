#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
typedef struct {
    int *values; 
    int size;    
} Solution;
Solution* solutionCreate(struct ListNode* head) {
    Solution* obj = (Solution*)malloc(sizeof(Solution));
    int count = 0;
    struct ListNode* temp = head;
    while (temp) {
        count++;
        temp = temp->next;
    }
    obj->values = (int*)malloc(count * sizeof(int));
    obj->size = count;
    temp = head;
    for (int i = 0; i < count; i++) {
        obj->values[i] = temp->val;
        temp = temp->next;
    }
    return obj;
}
int solutionGetRandom(Solution* obj) {
    if (obj->size == 0) return -1;
    int randomIndex = rand() % obj->size;
    return obj->values[randomIndex];
}
void solutionFree(Solution* obj) {
    free(obj->values);
    free(obj);
}