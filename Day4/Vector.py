import math


class Vector:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return str(self.values)

    def __add__(self, other):
        result = []

        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])

        return Vector(result)

    def __sub__(self, other):
        result = []

        for i in range(len(self.values)):
            result.append(self.values[i] - other.values[i])

        return Vector(result)

    def __mul__(self, scalar):
        result = []

        for value in self.values:
            result.append(value * scalar)

        return Vector(result)

    def dot(self, other):
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
        return self.dot(other) / (self.norm() * other.norm())


v1 = Vector([2, 3])
v2 = Vector([-1, 4])

print("v1:", v1)
print("v2:", v2)
print("v1 + v2:", v1 + v2)
print("v1 - v2:", v1 - v2)
print("v1 * 3:", v1 * 3)
print("dot product:", v1.dot(v2))
print("norm of v1:", v1.norm())
print("norm of v2:", v2.norm())
print("cosine similarity:", v1.cosine_similarity(v2))