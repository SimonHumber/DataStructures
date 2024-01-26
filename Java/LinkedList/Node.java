public class Node {
  private int value;
  Node nextNode;

  public Node(int input) {
    value = input;
    nextNode = null;
  }

  public Integer getNode() {
    return value;
  }

  public void setNode(int newValue) {
    value = newValue;
  }

  public Node getNext() {
    return nextNode;
  }

  public void setNext(Node value) {
    nextNode = value;
  }
}
