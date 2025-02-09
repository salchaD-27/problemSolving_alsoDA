# #include <stdio.h>
# #include <stdlib.h>
# #include <ctype.h>
# #include <string.h>
# #define MAX 100
# int operandStack[MAX];
# int operandTop = -1;
# char operatorStack[MAX];
# int operatorTop = -1;
# void pushOperand(int value) {operandStack[++operandTop] = value;}
# int popOperand() {
#     if (operandTop == -1) return 0;
#     return operandStack[operandTop--];
# }
# void pushOperator(char op) {operatorStack[++operatorTop] = op;}
# char popOperator() {
#     if (operatorTop == -1) return 0;
#     return operatorStack[operatorTop--];
# }
# int precedence(char op) {
#     if (op == '+' || op == '-') return 1;
#     return 0;
# }
# int applyOperation(int a, int b, char op) {
#     if (op == '+') return a + b;
#     if (op == '-') return a - b;
#     return 0;
# }
# int calculate(char* expression) {
#     int i, n = strlen(expression);
#     for (i = 0; i < n; i++) {
#         if (expression[i] == ' ') continue;
#         if (isdigit(expression[i]) || 
#             (expression[i] == '-' && (i == 0 || expression[i - 1] == '('))) {
#             int num = 0, sign = 1;
#             if (expression[i] == '-') {
#                 sign = -1;
#                 i++;
#             }
#             while (i < n && isdigit(expression[i])) {
#                 num = num * 10 + (expression[i] - '0');
#                 i++;
#             }
#             i--;
#             pushOperand(sign * num);
#         }
#         else if (expression[i] == '(') {
#             pushOperator(expression[i]);
#         }
#         else if (expression[i] == ')') {
#             while (operatorTop != -1 && operatorStack[operatorTop] != '(') {
#                 int b = popOperand();
#                 int a = popOperand();
#                 char op = popOperator();
#                 pushOperand(applyOperation(a, b, op));
#             }
#             popOperator(); 
#         }
#         else {  
#             while (operatorTop != -1 && precedence(operatorStack[operatorTop]) >= precedence(expression[i])) {
#                 int b = popOperand();
#                 int a = popOperand();
#                 char op = popOperator();
#                 pushOperand(applyOperation(a, b, op));
#             }
#             pushOperator(expression[i]);
#         }
#     }
#     while (operatorTop != -1) {
#         int b = popOperand();
#         int a = popOperand();
#         char op = popOperator();
#         pushOperand(applyOperation(a, b, op));
#     }
#     return popOperand();
# }

# class Solution:
#     def calculate(self, s: str) -> int:
#         def op(char): return (char=='+' or char=='-' or char=='(' or char==')')
#         exp=[]
#         for i in range(len(s)):
#             if(i==0 and s[i]=='-'):
#                 num=''
#                 i+=1
#                 while(not op(s[i])): 
#                     if(s[i]==' '): 
#                         i+=1
#                         continue
#                     num+=s[i]
#                     i+=1
#                 exp.append(-int(num))
#             elif(s[i]=='(' or s[i]==')'): continue
#             elif(op(s[i]) and s[i+1]=='-'):
#                 exp.append(s[i])
#                 num=''
#                 i+=2
#                 while(not op(s[i])): 
#                     if(s[i]==' '): 
#                         i+=1
#                         continue
#                     num+=s[i]
#                     i+=1
#                 exp.append(-int(num))
#             elif(not op(s[i])): exp.append(int(s[i]))
#             else: exp.append(s[i])

class Solution:
  def calculate(self, s: str) -> int:
    ans = 0
    num = 0
    sign = 1
    stack = [sign] 
    for c in s:
      if c.isdigit(): num = num * 10 + int(c)
      elif c == '(': stack.append(sign)
      elif c == ')': stack.pop()
      elif c == '+' or c == '-':
        ans += sign * num
        sign = (1 if c == '+' else -1) * stack[-1]
        num = 0
    return ans + sign * num