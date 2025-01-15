#include <stdio.h>
#include <stdbool.h>
bool has1(int* arr, int size) {
    for (int i = 0; i < size; i++){if (arr[i] == 1){return true;}}
    return false;
}
int minimumArea(int** grid, int gridSize, int* gridColSize) {
    int u = -1, b = -1, l = -1, r = -1;
    for (int i = 0; i < gridSize; i++) {
        if (has1(grid[i], gridColSize[i])) {
            u = i;
            break;
        }
    }
    for (int i = gridSize - 1; i >= 0; i--) {
        if (has1(grid[i], gridColSize[i])) {
            b = i;
            break;
        }
    }
    for (int j = 0; j < gridColSize[0]; j++) {
        for (int i = 0; i < gridSize; i++) {
            if (grid[i][j] == 1) {
                l = j;
                break;
            }
        }
        if (l != -1) break;
    }
    for (int j = gridColSize[0] - 1; j >= 0; j--) {
        for (int i = 0; i < gridSize; i++) {
            if (grid[i][j] == 1) {
                r = j;
                break;
            }
        }
        if (r != -1) break;
    }
    if (u == -1 || b == -1 || l == -1 || r == -1){return 0;}
    return (b - u + 1) * (r - l + 1);
}