class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def search(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                return True

            current = current.next

        return False

    def delete(self, target):
        if self.head is None:
            return

        if self.head.data == target:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.data == target:
                current.next = current.next.next
                return

            current = current.next

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        self.head = prev


linked_list = LinkedList()

linked_list.insert_end(10)
linked_list.insert_end(20)
linked_list.insert_end(30)

print("Original list:")
linked_list.traverse()

linked_list.insert_beginning(5)
print("After inserting 5 at beginning:")
linked_list.traverse()

linked_list.insert_end(40)
print("After inserting 40 at end:")
linked_list.traverse()

print("Search 30:")
print(linked_list.search(30))

print("Search 100:")
print(linked_list.search(100))

linked_list.delete(20)
print("After deleting 20:")
linked_list.traverse()

linked_list.reverse()
print("After reversing:")
linked_list.traverse()