// #include <stdio.h>
// int sumWith(int** questions, int questionsSize, int anchorIndex){
//     int sum=questions[anchorIndex][0];
//     for(int k=questions[anchorIndex][1]+1; k<questionsSize; k++){
//         sum+=questions[k][0];
//         k+=questions[k][1];
//     }
//     return sum;
// }
// long long mostPoints(int** questions, int questionsSize, int* questionsColSize) {
//     int sum=0;
//     for(int i=0; i<questionsSize; i++){
//         int tempSum=sumWith(questions, questionsSize, i);
//         if(tempSum>sum){sum=tempSum;}
//     }
//     return sum;
// }

#include <stdio.h>

long long mostPoints(int** questions, int questionsSize, int* questionsColSize) {
    long long dp[questionsSize];
    dp[questionsSize - 1] = questions[questionsSize - 1][0];

    for (int i = questionsSize - 2; i >= 0; i--) {
        long long pointsIfSolved = questions[i][0];
        int nextQuestionIndex = i + questions[i][1] + 1;
        if (nextQuestionIndex < questionsSize){pointsIfSolved += dp[nextQuestionIndex];}
        dp[i] = (pointsIfSolved > dp[i + 1]) ? pointsIfSolved : dp[i + 1];
    }
    return dp[0];
}