import unittest
import copy

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            print('[error] list is empty')
            return True
        return False

    def addFront(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def addBack(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def deleteFront(self):
        if self.isEmpty():
            return

        temp = self.head
        self.head = temp.next

    def deleteBack(self):
        if self.isEmpty():
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def hasLoop(self):
        slow = self.head
        fast = self.head

        while slow.next is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("loop detected")
                return True

        return False


class MyTest(unittest.TestCase):
    def test_addFront(self):
        ll = LinkedList()
        ll.addFront(5)

        temp = ll.head
        self.assertEqual(temp.data == 5, True)

    def test_addBack(self):
        ll = LinkedList()
        ll.addFront(5)
        ll.addBack(6)

        temp = ll.head
        while temp.next is not None:
            temp = temp.next

        self.assertEqual(temp.data == 6, True)

    def test_deleteBack(self):
        ll = LinkedList()
        ll.addFront(5)
        ll.addBack(6)
        ll.deleteBack()

        temp = ll.head
        while temp.next is not None:
            temp = temp.next

        self.assertEqual(temp.data == 6, False)

    def test_deleteFront(self):
        ll = LinkedList()
        ll.addFront(5)
        ll.addBack(6)
        ll.deleteFront()

        temp = ll.head
        self.assertEqual(temp.data == 6, True)

    def test_reverse(self):
        ll = LinkedList()
        ll.addFront(5)
        ll.addBack(6)
        ll.addBack(7)
        forwards = []

        temp = ll.head
        while temp.next is not None:
            forwards.append(temp.data)
            temp = temp.next

        ll_r = LinkedList()
        ll_r.addFront(5)
        ll_r.addBack(6)
        ll_r.addBack(7)
        backwords = []

        temp = ll_r.head
        while temp.next is not None:
            backwords.append(temp.data)
            temp = temp.next

        for a, b in zip(forwards, backwords):
            self.assertEqual(a == b, True)

if __name__ == '__main__':
    unittest.main()