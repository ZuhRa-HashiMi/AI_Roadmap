import math


class Vector:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return f"Vector({self.values})"

    def __eq__(self, other):
        return self.values == other.values

    def check_dimension(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same dimension")

    def __add__(self, other):
        self.check_dimension(other)

        result = []

        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])

        return Vector(result)

    def __sub__(self, other):
        self.check_dimension(other)

        result = []

        for i in range(len(self.values)):
            result.append(self.values[i] - other.values[i])

        return Vector(result)

    def __mul__(self, scalar):
        result = []

        for value in self.values:
            result.append(value * scalar)

        return Vector(result)

    def __rmul__(self, scalar):
        return self * scalar

    def dot(self, other):
        self.check_dimension(other)

        result = 0

        for i in range(len(self.values)):
            result += self.values[i] * other.values[i]

        return result

    def norm(self):
        total = 0

        for value in self.values:
            total += value ** 2

        return math.sqrt(total)

    def cosine_similarity(self, other):
        self.check_dimension(other)

        if self.norm() == 0 or other.norm() == 0:
            raise ValueError("Cannot compute cosine similarity with zero vector")

        return self.dot(other) / (self.norm() * other.norm())


v1 = Vector([2, 3])
v2 = Vector([-1, 4])
v3 = Vector([2, 3])

print("v1:", v1)
print("v2:", v2)

print("v1 + v2:", v1 + v2)
print("v1 - v2:", v1 - v2)

print("v1 * 3:", v1 * 3)
print("3 * v1:", 3 * v1)

print("dot product:", v1.dot(v2))
print("norm of v1:", v1.norm())
print("norm of v2:", v2.norm())

print("cosine similarity:", v1.cosine_similarity(v2))

print("v1 == v2:", v1 == v2)
print("v1 == v3:", v1 == v3)

try:
    v4 = Vector([1, 2, 3])
    print(v1 + v4)
except ValueError as error:
    print(error)

