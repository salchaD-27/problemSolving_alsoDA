#include <stdio.h>
#include <stdlib.h>
typedef struct MyLinkedList {
    int val;
    struct MyLinkedList* next;
} MyLinkedList;
MyLinkedList* myLinkedListCreate() {
    MyLinkedList* obj = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    obj->val = 0;
    obj->next = NULL;
    return obj;
}
int myLinkedListGet(MyLinkedList* obj, int index) {
    obj = obj->next;
    while (index > 0 && obj != NULL) {
        obj = obj->next;
        index--;
    }
    return (obj != NULL) ? obj->val : -1;
}
void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    MyLinkedList* newNode = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    newNode->val = val;
    newNode->next = obj->next;
    obj->next = newNode;
}
void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    while (obj->next != NULL) {obj = obj->next;}
    MyLinkedList* newNode = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    newNode->val = val;
    newNode->next = NULL;
    obj->next = newNode;
}
void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    while (index > 0 && obj != NULL) {
        obj = obj->next;
        index--;
    }
    if (obj == NULL) return;
    MyLinkedList* newNode = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    newNode->val = val;
    newNode->next = obj->next;
    obj->next = newNode;
}
void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    while (index > 0 && obj != NULL) {
        obj = obj->next;
        index--;
    }
    if (obj == NULL || obj->next == NULL) return;
    MyLinkedList* toDelete = obj->next;
    obj->next = toDelete->next;
    free(toDelete);
}
void myLinkedListFree(MyLinkedList* obj) {
    MyLinkedList* current = obj;
    while (current != NULL) {
        MyLinkedList* temp = current;
        current = current->next;
        free(temp);
    }
}