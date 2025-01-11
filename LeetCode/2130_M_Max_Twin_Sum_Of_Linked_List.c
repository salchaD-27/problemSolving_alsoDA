// #include <stdio.h>
// #include <stdlib.h>
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };
// int countNodes(struct ListNode* head) {
//     int count = 0;
//     while (head != NULL) {
//         count++;
//         head = head->next;
//     }
//     return count;
// }
// int twinVal(struct ListNode* head, int index, int totalNodes) {
//     for (int i = 0; i < totalNodes - index - 1; i++) {
//         head = head->next;
//     }
//     return head->val;
// }
// int pairSum(struct ListNode* head) {
//     int sum = 0;
//     int totalNodes = countNodes(head);
//     for (int i = 0; i < totalNodes / 2; i++) {
//         int tempSum = head->val + twinVal(head, i, totalNodes);
//         head = head->next;
//         if (tempSum > sum){sum = tempSum;}
//     }
//     return sum;
// }


#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};
int countNodes(struct ListNode* head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->next;
    }
    return count;
}
int pairSum(struct ListNode* head) {
    int n = countNodes(head), arr[n], index = 0;
    struct ListNode* current = head;
    while (current != NULL) {
        arr[index++] = current->val;
        current = current->next;
    }
    int L = 0, R = n - 1, sum = 0;
    while (L < R) {
        int tempSum = arr[L] + arr[R];
        if (tempSum > sum){sum = tempSum;}
        L++;
        R--;
    }
    return sum;
}