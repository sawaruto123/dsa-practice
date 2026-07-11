"""
Singly Linked List — built from scratch (no built-in list/deque).

Why build this instead of just using a Python list?
A Python list is actually a dynamic array under the hood - O(1) random
access but O(n) insert/delete at the front. A linked list flips that:
O(n) random access but O(1) insert/delete at the front. Building it by
hand is the only way to really feel *why* that tradeoff exists.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def delete(self, value):
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def reverse(self):
        """
        The classic "everyone gets stuck on this once" problem.
        Idea: walk the list, and at each node, flip its `next` pointer
        to point backward instead of forward. Need three pointers
        (prev, current, next_node) because once you overwrite
        current.next, you'd lose the rest of the list otherwise.
        """
        prev = None
        current = self.head

        while current:
            next_node = current.next   # save before we overwrite it
            current.next = prev        # flip the pointer
            prev = current              # move prev forward
            current = next_node         # move current forward

        self.head = prev

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_end(1)
    ll.insert_end(2)
    ll.insert_end(3)
    print("Built:", ll.to_list())        # [1, 2, 3]

    ll.reverse()
    print("Reversed:", ll.to_list())     # [3, 2, 1]

    ll.delete(2)
    print("After delete(2):", ll.to_list())  # [3, 1]
