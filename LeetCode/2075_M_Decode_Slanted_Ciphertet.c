#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* decodeCiphertext(char* encodedText, int rows) {
    int n = strlen(encodedText);
    int cols = n / rows;
    char** grid = (char**)malloc(rows * sizeof(char*));
    for (int i = 0; i < rows; i++){grid[i] = (char*)malloc(cols * sizeof(char));}
    int k = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            grid[i][j] = encodedText[k++];
        }
    }
    char* expr = (char*)malloc((n + 1) * sizeof(char));
    int z = 0;
    for (int j = 0; j < cols; j++) {
        for (int i = 0; i < rows && (i + j) < cols; i++) {
            expr[z++] = grid[i][i + j];
        }
    }
    expr[z] = '\0';
    for (int i = 0; i < rows; i++){free(grid[i]);}
    free(grid);
    int end = z - 1;
    while (end >= 0 && expr[end] == ' '){end--;}
    expr[end + 1] = '\0';
    return expr;
}