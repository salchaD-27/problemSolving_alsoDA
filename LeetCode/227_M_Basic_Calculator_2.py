class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operator = '+'
        n = len(s)
        for i in range(n):
            char = s[i]
            if char.isdigit(): current_number = current_number * 10 + int(char)
            if (not char.isdigit() and char != ' ') or i == n - 1:
                if operator == '+': stack.append(current_number)
                elif operator == '-': stack.append(-current_number)
                elif operator == '*': stack.append(stack.pop() * current_number)
                elif operator == '/':
                    top = stack.pop()
                    if top // current_number < 0 and top % current_number != 0: stack.append(top // current_number + 1)
                    else: stack.append(top // current_number)
                operator = char
                current_number = 0
        return sum(stack)