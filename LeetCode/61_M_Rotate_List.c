#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
int deleteEnd(struct ListNode* head){
    if (head == NULL || head->next == NULL){ 
        int val = head ? head->val : -1;      
        free(head);                           
        return val;
    }
    struct ListNode* temp=head;
    while(temp->next->next!=NULL){temp=temp->next;}
    int val=temp->next->val;
    free(temp->next);
    temp->next=NULL;
    return val;
}
struct ListNode* insertFront(struct ListNode* head, int val){
    struct ListNode* temp=(struct ListNode*)malloc(sizeof(struct ListNode));
    temp->val=val;
    temp->next=head;
    head=temp;
    return head;
}
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head == NULL || head->next == NULL || k == 0){return head;}
    int length = 0;
    struct ListNode* temp = head;
    while (temp != NULL) {
        length++;
        temp = temp->next;
    }
    k = k % length;
    if (k == 0){return head;}
    for(int i=0; i<k; i++){
        int temp=deleteEnd(head);
        head=insertFront(head, temp);
    }
    return head;
}