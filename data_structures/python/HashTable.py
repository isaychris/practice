class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for x in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash(key)
        self.table[idx].append((key, value))

    def retrieve(self, key):
        idx = self.hash(key)

        for item in self.table[idx]:
            if item[0] == key:
                return item[1]

        return None

    def delete(self, key):
        idx = self.hash(key)

        for i, item in enumerate(self.table[idx]):
            if item[0] == key:
                self.table[idx].pop(i)

    def display(self):
        print(str(self.table))

my_hash = HashTable(10)
my_hash.insert(key=2, value='chris')
my_hash.insert(key=115, value='billy')
my_hash.insert(key=15, value='kevin')
my_hash.display()

# billy and kevin in same slot
print(my_hash.retrieve(key=115))
print(my_hash.retrieve(key=15))
print(my_hash.retrieve(key=2))

my_hash.delete(key=15)
my_hash.display()

