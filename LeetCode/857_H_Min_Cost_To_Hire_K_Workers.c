#include <stdio.h>

// calculate one standard
// calculate standardWages
// for all qualities with standardWages greater than minWages, they are accepted
// if accepted no of qualities greater than k, then sort them and add first k qualities
// answer = standard * sum
// else change the standard

void bubbleSort(double* arr, int n) {
    int i, j;
    double temp;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

double mincostToHireWorkers(int* quality, int qualitySize, int* wage, int wageSize, int k) {
    double cost = 999999999.99999;
    for (int i = 0; i < qualitySize; i++) {
        double standard = (double)wage[i] / quality[i]; 
        double acceptedQualities[qualitySize]; 
        int j = 0;

        for (int l = 0; l < qualitySize; l++) {
            if ((quality[l] * standard) >= wage[l]) {
                acceptedQualities[j] = quality[l];
                j++;
            }
        }

        if (j >= k) {
            bubbleSort(acceptedQualities, j); 
            double tempCost = 0;
            for (int a = 0; a < k; a++) {
                tempCost += acceptedQualities[a];
            }
            double tempAns = tempCost * standard;
            if (tempAns < cost) {
                cost = tempAns;
            }
        }
    }
    return cost;
}