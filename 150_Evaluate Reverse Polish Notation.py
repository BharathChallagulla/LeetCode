import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []

        for i in tokens:
            oper = None
            if i in "+-*/":
                first, second = stack.pop(), stack.pop()
            if i == '+':
                oper = second + first
            elif i == '-':
                oper = second - first
            elif i == '*':
                oper = second * first
            elif i == '/':
                oper = float(second) / float(first)
                if oper < 0:
                    oper = math.ceil(oper)
                else:
                    oper = math.floor(oper)
            else:
                stack.append(int(i))
            
            if oper is not None:
                stack.append(oper)

        return int(stack[0])