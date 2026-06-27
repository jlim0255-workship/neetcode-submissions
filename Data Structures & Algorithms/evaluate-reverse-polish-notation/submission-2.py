class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # operands
        operands = ["+", "-", "*", "/"]

        # loop through the list
        for tok in tokens:
            if tok in operands:
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
            else:
                stack.append(tok)

        return int(stack[0])



        # if encounter number, push to stack


        # if operator, pop 2 number from stack and operate

