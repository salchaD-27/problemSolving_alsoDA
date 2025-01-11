#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MAX_ROWS 30
#define MAX_COLS 30
#define MAX_STATE (1 << 6)

typedef struct {
    int row, col;
} Position;

typedef struct {
    Position pos;
    int keys;
} State;

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

int shortestPathAllKeys(char** grid, int gridSize) {
    int rows=gridSize, cols=strlen(grid[0]);
    Position start;
    int totalKeys = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '@') {
                start.row = i;
                start.col = j;
            }
            if (grid[i][j] >= 'a' && grid[i][j] <= 'f') {
                totalKeys++;
            }
        }
    }
    State queue[MAX_ROWS * MAX_COLS * MAX_STATE];
    int front = 0, rear = 0;
    int visited[MAX_ROWS][MAX_COLS][MAX_STATE] = {{{0}}};
    queue[rear++] = (State){start, 0};
    visited[start.row][start.col][0] = 1;
    
    int steps = 0;
    
    while (front < rear) {
        int size = rear - front;
        for (int i = 0; i < size; i++) {
            State current = queue[front++];
            Position currPos = current.pos;
            int currKeys = current.keys;
            if (currKeys == (1 << totalKeys) - 1) {
                return steps;
            }
            for (int d = 0; d < 4; d++) {
                int newRow = currPos.row + dx[d];
                int newCol = currPos.col + dy[d];
                if (newRow < 0 || newRow >= rows || newCol < 0 || newCol >= cols || grid[newRow][newCol] == '#') {
                    continue;
                }
                char cell = grid[newRow][newCol];
                int newKeys = currKeys;
                if (cell >= 'a' && cell <= 'f') {
                    newKeys |= (1 << (cell - 'a'));
                }
                if (cell >= 'A' && cell <= 'F' && !(currKeys & (1 << (cell - 'A')))) {
                    continue;
                }
                if (!visited[newRow][newCol][newKeys]) {
                    visited[newRow][newCol][newKeys] = 1;
                    queue[rear++] = (State){{newRow, newCol}, newKeys};
                }
            }
        }
        steps++;
    }
    return -1;
}

int main() {
    char* grid[] = {"@.a..","###.#","b.A.B"};
    int gridSize = 3;
    int result = shortestPathAllKeys(grid, gridSize);
    printf("Result: %d\n", result);
    return 0;
}
