// #include <stdio.h>
// #include <stdbool.h>
// void swap(int* xp, int* yp) {
//     int temp = *xp;
//     *xp = *yp;
//     *yp = temp;
// }
// void bubbleSort(int arr[], int n) {
//     for (int i = 0; i < n - 1; i++) {
//         for (int j = 0; j < n - i - 1; j++) {
//             if (arr[j] > arr[j + 1]) {
//                 swap(&arr[j], &arr[j + 1]);
//             }
//         }
//     }
// }
// int maximumGroups(int* grades, int gradesSize) {
//     bubbleSort(grades, gradesSize);
//     int currentSize = 1, ans = 0, i = 0;           
//     while (i < gradesSize) {
//         if (gradesSize - i >= currentSize){
//             i += currentSize;
//             currentSize++;
//             ans++;
//         }else{break;}
//     }
//     return ans;
// }

#include <stdio.h>
int maximumGroups(int* grades, int gradesSize) {
    int i=1, ans=0;
    while(gradesSize>=i){
        gradesSize-=i;
        i++;
        ans++;
    }
    return ans;
}