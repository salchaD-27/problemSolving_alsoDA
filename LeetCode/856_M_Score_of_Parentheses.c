#include <stdio.h>

int scoreOfParentheses(char* s) {
    int stack[75]; 
    int top = -1; 
    
    while (*s != '\0') {
        if (*s == '(') {
            stack[++top] = 0;
        } else {
            int innerScore = stack[top--];
            int currentScore = (innerScore == 0) ? 1 : 2 * innerScore;
            if (top >= 0) {
                stack[top] += currentScore;
            } else {
                stack[++top] = currentScore;
            }
        }
        s++;
    }
    return stack[top];
}

int main() {
    char input[] = "(()(()))";
    printf("Score: %d\n", scoreOfParentheses(input)); // Output: 6
    return 0;
}
