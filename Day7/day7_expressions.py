def is_valid_parentheses(text):
    stack = []

    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in text:
        if char in "({[":
            stack.append(char)

        elif char in ")}]":
            if len(stack) == 0:
                return False

            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0


def infix_to_postfix(expression):
    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    }

    stack = []
    output = []

    tokens = expression.split()

    for token in tokens:
        if token.isalnum():
            output.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            stack.pop()

        else:
            while (
                stack
                and stack[-1] != "("
                and precedence[stack[-1]] >= precedence[token]
            ):
                output.append(stack.pop())

            stack.append(token)

    while stack:
        output.append(stack.pop())

    return " ".join(output)


def evaluate_postfix(expression):
    stack = []

    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))

        else:
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(left / right)

    return stack.pop()


print("Valid parentheses:")
print(is_valid_parentheses("({[]})"))
print(is_valid_parentheses("([)]"))

print("\nInfix to postfix:")
print(infix_to_postfix("A + B * C"))
print(infix_to_postfix("( A + B ) * C"))

print("\nPostfix evaluation:")
print(evaluate_postfix("2 3 4 * +"))
print(evaluate_postfix("2 3 + 4 *"))