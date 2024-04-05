# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9


from typing import List
from operator import add, sub, mul


class Solution:
    op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(i))
        
        return stack.pop()
        
    #     op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}
    
    # def evalRPN(self, tokens: List[str]) -> int:
    #     stack = []
    #     for token in tokens:
    #         if token not in {'+', '-', '*', '/'}:
    #             stack.append(int(token))
    #         else:
    #             op2 = stack.pop()
    #             op1 = stack.pop()
    #             stack.append(self.op_map[token](op1, op2))  # 第一个出来的在运算符后面
    #     return stack.pop()


if __name__ == '__main__':
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))