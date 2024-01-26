/** Node */
public class Node {

  private int value;
  private Node leftNode;
  private Node rightNode;
  private Node parentNode;

  public Node(int value) {
    this.value = value;
    this.leftNode = null;
    this.rightNode = null;
    this.parentNode = null;
  }

  public int getValue() {
    return this.value;
  }

  public Node getLeft() {
    return this.leftNode;
  }

  public Node getRight() {
    return this.rightNode;
  }

  public Node getParent() {
    return this.parentNode;
  }

  public void setValue(int value) {
    this.value = value;
  }

  public void setLeft(Node node) {
    this.leftNode = node;
  }

  public void setRight(Node node) {
    this.rightNode = node;
  }

  public void setParent(Node node) {
    this.parentNode = node;
  }

  public boolean isLeaf() {
    if (this.leftNode == null && this.rightNode == null) {
      return true;
    } else {
      return false;
    }
  }
}
