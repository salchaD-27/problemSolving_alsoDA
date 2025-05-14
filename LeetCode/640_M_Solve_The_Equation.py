# class Solution:
#     def solveEquation(self, equation: str) -> str:
#         def getXCoeff(eq):
#             eqXidx=0
#             for i in range(len(eq)):
#                 if eq[i]=='x': eqXidx=i
#             eqXCoeff=0
#             for i in range(eqXidx-1, -1, -1):
#                 if(eq[i]!='-' and eq[i]!='+'):
#                     if(eqXCoeff==0): eqXCoeff+=int(eq[i])
#                     else: eqXCoeff+=int(eq[i])*10
#                 else: break
#             if eqXCoeff==0: eqXCoeff=1
#             return eqXCoeff
        
#         LHS,RHS=equation.split('=')
#         lhsXCoeff,rhsXCoeff=getXCoeff(LHS),getXCoeff(RHS)
#         LHStotal,RHStotal=0,0
        
#         pos=LHS.split('+')
#         neg=[]
#         for i in range(len(pos)):
#             if('-' not in pos[i] and 'x' not in pos[i]): LHStotal+=int(pos[i])
#             else: neg.append(pos[i])
#         for i in range(len(neg)):
#             tempLHS=neg[i].split('-')
#             if('x' not in tempLHS[0]): LHStotal-=int(tempLHS[i])
#         pos=RHS.split('+')
#         neg=[]
#         for i in range(len(pos)):
#             if('-' not in pos[i] and 'x' not in pos[i]): RHStotal+=int(pos[i])
#             else: neg.append(pos[i])
#         for i in range(len(neg)):
#             tempRHS=neg[i].split('-')
#             if('x' not in tempRHS[0]): RHStotal-=int(tempRHS[i])
#         # lhsXCoeff*x + LHStotal = rhsXCoeff*x + RHStotal
#         finalEq=[]
#         if(lhsXCoeff>=rhsXCoeff): finalEq=[lhsXCoeff-rhsXCoeff, 'x=', RHStotal-=LHStotal]
#         else: finalEq=[rhsXCoeff-lhsXCoeff, 'x=', LHStotal-=RHStotal]

#         if finalEq[0]==0: return 'Infinite solutions'
#         elif finalEq[1]=='x=' and finalEq[2]==0: return 'No solution'
#         else: return str(finalEq[0]) + finalEq[1] + str(finalEq)

class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr):
            coeff = 0
            const = 0
            i = 0
            sign = 1
            while i < len(expr):
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1
                else:
                    num = 0
                    valid = False
                    while i < len(expr) and expr[i].isdigit():
                        num = num * 10 + int(expr[i])
                        i += 1
                        valid = True
                    if i < len(expr) and expr[i] == 'x':
                        if valid: coeff += sign * num
                        else: coeff += sign
                        i += 1
                    else: const += sign * num
            return coeff, const
        
        lhs, rhs = equation.split('=')
        lhs_coeff, lhs_const = parse(lhs)
        rhs_coeff, rhs_const = parse(rhs)
        x_coeff = lhs_coeff - rhs_coeff
        total_const = rhs_const - lhs_const
        if x_coeff == 0:
            if total_const == 0: return "Infinite solutions"
            else: return "No solution"
        return f"x={total_const // x_coeff}"