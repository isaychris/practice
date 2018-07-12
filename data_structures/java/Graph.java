import java.util.*;

public class Graph {
    private HashMap<Character, Vertex> vertices;

    private Graph() {
        this.vertices = new HashMap<>();
    }

    private void addVertex(char v) {
        if (!vertices.containsKey(v)) {
            vertices.put(v, new Vertex(v));
        }
    }

    private void addEdge(char u, char v, int weight) {
        if (vertices.containsKey(u) && vertices.containsKey(v)) {
            vertices.get(u).add_neighbor(v, weight);
            vertices.get(v).add_neighbor(u, weight);
        }
    }

    private void printGraph() {
        for (Map.Entry m : vertices.entrySet()) {
            Vertex v = (Vertex) m.getValue();

            System.out.println(m.getKey() + " " + v.neighbors);
        }
    }

    public static void main(String[] args) {
        Graph g = new Graph();
        g.addVertex('A');
        g.addVertex('B');
        g.addVertex('C');
        g.addEdge('A', 'B', 1);
        g.addEdge('A', 'C', 2);
        g.addEdge('C', 'B', 3);
        g.printGraph();
    }
}
