class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # operands
        operands = ["+", "-", "*", "/"]

        # loop through the list
        for tok in tokens:
            # if operator, pop 2 number from stack and operate
            if tok in operands:
                # the first popped is second number
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if tok == "+":
                    res = num1 + num2
                if tok == "-":
                    res = num1 - num2
                if tok == "*":
                    res = num1 * num2
                if tok == "/":
                    res = num1 / num2
                
                stack.append(res)
            
            # if encounter number, push to stack
            else:
                stack.append(tok)

        return int(stack[0])