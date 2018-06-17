import Stack as S

class Queue:
    def __init__(self, size):
        self.s1 = S.Stack(size)
        self.s2 = S.Stack(size)

    def enqueue(self, element):
        self.s1.push(element)

    def dequeue(self):
        if self.getSize() == 0:
            print('queue is empty')
            return

        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if self.getSize() == 0:
            print('queue is empty')
            return

        return self.s2.top()

    def getSize(self):
        return self.s1.getSize() + self.s2.getSize()

    def traverse(self):
        self.s2.traverse()

my_queue = Queue(5)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.traverse()
