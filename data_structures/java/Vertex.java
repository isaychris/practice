import java.util.HashMap;

public class Vertex {
    public char name;
    public HashMap<Character, Integer> neighbors;

    public Vertex(char name) {
        this.name = name;
        this.neighbors = new HashMap<>();
    }


    public void add_neighbor(char v, int weight) {
        if (!neighbors.containsKey(v)) {
            neighbors.put(v, weight);
        }
    }
}

