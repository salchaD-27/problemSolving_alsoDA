#include <stdio.h>
#include <string.h>
int slidingWindow(char* str, int k, char target){
    int left = 0, right = 0;
    int changes = 0;
    int maxLen = 0;
    while (right < strlen(str)) {
        if (str[right] != target) {
            changes++;
        }
        while (changes > k) {
            if (str[left] != target) {
                changes--;
            }
            left++;
        }
        maxLen = (right - left + 1 > maxLen) ? right - left + 1 : maxLen;
        right++;
    }
    return maxLen;
}
int maxConsecutiveAnswers(char* answerKey, int k) {
    int maxWindow = 0;
    int maxForT = slidingWindow(answerKey, k, 'T');
    int maxForF = slidingWindow(answerKey, k, 'F');
    return (maxForT > maxForF) ? maxForT : maxForF;
}