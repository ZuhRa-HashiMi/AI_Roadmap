import math


def derivative(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


tests = [
    ("x^2", lambda x: x ** 2, lambda x: 2 * x, 3),
    ("x^3", lambda x: x ** 3, lambda x: 3 * x ** 2, 2),
    ("e^x", math.exp, math.exp, 2)
]

hs = [
    1e-1, 1e-2, 1e-3, 1e-4,
    1e-5, 1e-6, 1e-7, 1e-8,
    1e-9, 1e-10, 1e-11, 1e-12
]

for name, f, exact_derivative, x in tests:

    print("\n", name)

    exact = exact_derivative(x)

    for h in hs:
        numerical = derivative(f, x, h)
        error = abs(numerical - exact)

        print(
            f"h={h:.0e}, "
            f"numerical={numerical:.12f}, "
            f"error={error:.3e}"
        )