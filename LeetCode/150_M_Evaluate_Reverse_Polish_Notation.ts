function oper(str: string): boolean {return (str === '+' || str === '-' || str === '*' || str === '/');}
function evaluate(op1: string, opr: string, op2: string): string {
    switch (opr) {
        case '+': return (Number(op1) + Number(op2)).toString();
        case '-': return (Number(op1) - Number(op2)).toString();
        case '*': return (Number(op1) * Number(op2)).toString();
        case '/': return Math.trunc(Number(op1) / Number(op2)).toString();
    }
    return '';
}
function evalRPN(tokens: string[]): number {
    let stack: string[] = [];
    for (let token of tokens) {
        if (oper(token)) {
            let op2 = stack.pop()!;
            let op1 = stack.pop()!;
            let result = evaluate(op1, token, op2);
            stack.push(result);
        } else {
            stack.push(token);
        }
    }
    return Number(stack.pop());
}