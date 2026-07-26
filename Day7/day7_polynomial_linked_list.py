class TermNode:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coefficient, power):
        if coefficient == 0:
            return

        new_node = TermNode(coefficient, power)

        if self.head is None or power > self.head.power:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        while current.next is not None and current.next.power > power:
            current = current.next

        if current.power == power:
            current.coefficient += coefficient
            return

        if current.next is not None and current.next.power == power:
            current.next.coefficient += coefficient
            return

        new_node.next = current.next
        current.next = new_node

    def display(self):
        if self.head is None:
            print("0")
            return

        current = self.head
        terms = []

        while current is not None:
            coef = current.coefficient
            power = current.power

            if power == 0:
                terms.append(str(coef))
            elif power == 1:
                terms.append(f"{coef}x")
            else:
                terms.append(f"{coef}x^{power}")

            current = current.next

        print(" + ".join(terms))

    def add(self, other):
        result = Polynomial()

        p1 = self.head
        p2 = other.head

        while p1 is not None and p2 is not None:
            if p1.power == p2.power:
                result.insert_term(p1.coefficient + p2.coefficient, p1.power)
                p1 = p1.next
                p2 = p2.next

            elif p1.power > p2.power:
                result.insert_term(p1.coefficient, p1.power)
                p1 = p1.next

            else:
                result.insert_term(p2.coefficient, p2.power)
                p2 = p2.next

        while p1 is not None:
            result.insert_term(p1.coefficient, p1.power)
            p1 = p1.next

        while p2 is not None:
            result.insert_term(p2.coefficient, p2.power)
            p2 = p2.next

        return result


p1 = Polynomial()
p1.insert_term(3, 2)
p1.insert_term(5, 1)
p1.insert_term(7, 0)

p2 = Polynomial()
p2.insert_term(2, 2)
p2.insert_term(4, 1)
p2.insert_term(1, 0)

print("P1:")
p1.display()

print("P2:")
p2.display()

result = p1.add(p2)

print("P1 + P2:")
result.display()