import java.util.HashMap;

public class Structure {

  Vertex root;
  HashMap<Integer, Vertex> vertices = new HashMap<>();
  int size;

  public Structure() {
    this.root = null;
    this.size = 0;
  }

  public void insert(int value) {
    Vertex newNode = new Vertex(value);
    if (this.size == 0) {
      this.root = newNode;
    }
    this.size++;
    this.vertices.put(value, newNode);
  }

  public void connect(int first, int second) {
    if (!(this.vertices.containsKey(first))) {
      this.insert(first);
    }
    if (!(this.vertices.containsKey(second))) {
      this.insert(second);
    }
    this.vertices.get(first).addNeighbour(this.vertices.get(second));
    this.vertices.get(second).addNeighbour(this.vertices.get(first));
  }

  public int[] dfs() {
    if (this.size == 0) {
      return null;
    }
    Vertex vertex = this.root;
    int output[] = new int[this.size];
    Vertex neighbours[] = new Vertex[vertex.getNeighbours().size()];
  }
}
