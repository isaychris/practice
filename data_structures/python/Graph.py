class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = {}

    def add_neighbor(self, v, weight):
        if v not in self.neighbors:
            self.neighbors[v] = weight

class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertex(v)

    def addEdge(self, u, v, weight=0):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v, weight)
            self.vertices[v].add_neighbor(u, weight)

    def printGraph(self):
        for key, value in self.vertices.items():
            print('{}: {}'.format(key, value.neighbors))


g = Graph()
g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addEdge('A', 'B', 1)
g.addEdge('A', 'C', 2)
g.addEdge('C', 'B', 3)
g.printGraph()