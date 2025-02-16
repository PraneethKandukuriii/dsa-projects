def stack_calculator(expression):

    stack = []
    operators = {'+','-','*','/'}

    for token in expression.split():
        if token not in operators:
            stack.append(float(token))
        else:
            if len(stack) < 2:
                return "Error: Invalid expression!"


            b = stack.pop()
            a = stack.pop()



            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '/':
                stack.append(a/b)
            elif token == '*':
                if b == 0:
                    return "Error: Division by zero!"
                stack.append(a*b)
    return stack.pop()


expression = input("Enter The Expression: ")

result = stack_calculator(expression)
print("Result:",result)
