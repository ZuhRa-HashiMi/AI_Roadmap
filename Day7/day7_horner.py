def horner_eval(coefficients, x):
    result = coefficients[0]

    print("Start:", result)

    for i in range(1, len(coefficients)):
        print(f"Step {i}: {result} * {x} + {coefficients[i]}")
        result = result * x + coefficients[i]
        print("Result:", result)

    return result


coefficients = [2, -6, 2, -1]
x = 3

answer = horner_eval(coefficients, x)

print("Final answer:")
print(answer)