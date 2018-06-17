import unittest

class Stack:
    def __init__(self, size):
        self.size = size - 1
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, element):
        if len(self.data) > self.size:
            print("stack overflow")
            return

        self.data.append(element)

    def pop(self):
        if self.isEmpty():
            print("stack underflow")
            return

        temp = self.data[-1]
        del self.data[-1]

        return temp

    def top(self):
        return self.data[-1]

    def traverse(self):
        if self.isEmpty():
            print("stack is empty.")

        for e in self.data:
            print(e)

    def getSize(self):
        return len(self.data)

class MyTest(unittest.TestCase):
    def test_push(self):
        s = Stack(3)
        s.push(1)
        s.push(2)
        self.assertEqual(s.getSize() == 2, True)

    def test_pop(self):
        s = Stack(3)
        s.push(1)
        s.push(2)
        x = s.pop()
        x = s.pop()
        self.assertEqual(s.getSize() == 0, True)
        self.assertEqual(x == 1, True)

    def test_overflow(self):
        s = Stack(3)
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        self.assertEqual(s.getSize() > s.size, True)

    def test_underflow(self):
        s = Stack(3)
        s.pop()
        self.assertEqual(s.getSize() == 0, True)

if __name__ == '__main__':
    unittest.main()