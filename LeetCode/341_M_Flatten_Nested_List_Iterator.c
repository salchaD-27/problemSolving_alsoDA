#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
bool NestedIntegerIsInteger(struct NestedInteger *ni);
int NestedIntegerGetInteger(struct NestedInteger *ni);
struct NestedInteger **NestedIntegerGetList(struct NestedInteger *ni);
int NestedIntegerGetListSize(struct NestedInteger *ni);
struct NestedIterator {
    int *flatList; 
    int size;      
    int index;     
};
int countIntegers(struct NestedInteger **nestedList, int nestedListSize) {
    int count = 0;
    for (int i = 0; i < nestedListSize; i++) {
        if (NestedIntegerIsInteger(nestedList[i])) {count++;}
        else {count += countIntegers(NestedIntegerGetList(nestedList[i]), NestedIntegerGetListSize(nestedList[i]));}
    }
    return count;
}
void flattenList(struct NestedInteger **nestedList, int nestedListSize, int *flatList, int *index) {
    for (int i = 0; i < nestedListSize; i++) {
        if (NestedIntegerIsInteger(nestedList[i])) {flatList[(*index)++] = NestedIntegerGetInteger(nestedList[i]);}
        else {flattenList(NestedIntegerGetList(nestedList[i]), NestedIntegerGetListSize(nestedList[i]), flatList, index);}
    }
}
struct NestedIterator *nestedIterCreate(struct NestedInteger **nestedList, int nestedListSize) {
    struct NestedIterator *iter = (struct NestedIterator *)malloc(sizeof(struct NestedIterator));
    iter->size = countIntegers(nestedList, nestedListSize);
    iter->flatList = (int *)malloc(iter->size * sizeof(int));
    iter->index = 0;
    int idx = 0;
    flattenList(nestedList, nestedListSize, iter->flatList, &idx);
    return iter;
}
bool nestedIterHasNext(struct NestedIterator *iter) {return iter->index < iter->size;}
int nestedIterNext(struct NestedIterator *iter) {return iter->flatList[iter->index++];}
void nestedIterFree(struct NestedIterator *iter) {
    free(iter->flatList);
    free(iter);
}