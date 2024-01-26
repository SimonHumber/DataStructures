import java.util.HashMap;

public class Vertex {

  int value;
  HashMap<Integer, Vertex> neighbours = new HashMap<>();

  public Vertex(int value) {
    this.value = value;
  }

  public int getValue() {
    return this.value;
  }

  public HashMap<Integer, Vertex> getNeighbours() {
    return this.neighbours;
  }

  public void addNeighbour(Vertex node) {
    this.neighbours.put(node.getValue(), node);
  }
}
