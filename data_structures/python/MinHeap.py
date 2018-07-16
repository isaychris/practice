from math import floor

class MinHeap:
    def __init__(self):
        self.data = []

    def swap(self, idx1, idx2):
        temp = self.data[idx1]
        self.data[idx1] = self.data[idx2]
        self.data[idx2] = temp

    def heapifyUp(self):
        idx = len(self.data) - 1
        while self.hasParent(idx) and self.data[self.getParent(idx)] > self.data[idx]:
            self.swap(idx, self.getParent(idx))
            idx = self.getParent(idx)

    def heapifyDown(self):
        idx = 0
        while self.hasLeftChild(idx):
            small_idx = self.getLeftChild(idx)
            if self.hasRightChild(idx) and self.data[self.getRightChild(idx)] < self.data[self.getLeftChild(idx)]:
                small_idx = self.getRightChild(idx)
            if self.data[idx] < self.data[small_idx]:
                break
            else:
                self.swap(idx, small_idx)
            idx = small_idx

    def insert(self, item):
        self.data.append(item)
        self.heapifyUp()

    def extract(self):
        if self.isEmpty():
            return

        min_val = self.data[0]
        self.data[0] = self.data[len(self.data) - 1]
        self.data.pop()
        self.heapifyDown()

        return min_val

    def peek(self):
        if self.isEmpty():
            return

        return self.data[0]

    def traverse(self):
        print(self.data)

    def isEmpty(self):
        if len(self.data) == 0:
            print("Heap is empty")
            return True

    def getLeftChild(self, idx):
        return (2 * idx) + 1

    def getRightChild(self, idx):
        return (2 * idx) + 2

    def getParent(self, idx):
        return floor((idx-1) / 2)

    def hasLeftChild(self, idx):
        return self.getLeftChild(idx) < len(self.data)

    def hasRightChild(self, idx):
        return self.getRightChild(idx) < len(self.data)

    def hasParent(self, idx):
        return self.getParent(idx) >= 0


my_heap = MinHeap()
my_heap.insert(23)
my_heap.insert(1)
my_heap.insert(6)
my_heap.insert(19)
my_heap.insert(14)
my_heap.insert(18)
my_heap.insert(8)
my_heap.insert(24)
my_heap.insert(15)
my_heap.traverse()

while not my_heap.isEmpty():
    print(my_heap.extract())
