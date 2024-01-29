import java.util.ArrayDeque;

public class Tree {

  private Node root;
  private int size = 0;

  public void insert(int value) {
    Node newNode = new Node(value);
    this.size++;
    if (this.root == null) {
      this.root = newNode;
    } else {
      Node parentNode = this.root;
      while (true) {
        if (newNode.getValue() < parentNode.getValue()) {
          if (parentNode.getLeft() != null) {
            parentNode = parentNode.getLeft();
          } else {
            parentNode.setLeft(newNode);
            newNode.setParent(parentNode);
            break;
          }
        } else {
          if (parentNode.getRight() != null) {
            parentNode = parentNode.getRight();
          } else {
            parentNode.setRight(newNode);
            newNode.setParent(parentNode);
            break;
          }
        }
      }
    }
  }

  public Node get(int value) {
    if (this.size == 0) {
      throw new ArrayIndexOutOfBoundsException("Cannot retrieve, array empty!!");
    }
    Node current_node = this.root;
    while (true) {
      if (current_node.getValue() == value) {
        return current_node;
      } else if (current_node.getValue() > value) {
        if (current_node.getLeft() == null) {
          throw new ArithmeticException("Value not in tree!!");
        } else {
          current_node = current_node.getLeft();
        }
      } else {
        if (current_node.getRight() == null) {
          throw new ArithmeticException("Value not in tree!!");
        } else {
          current_node = current_node.getRight();
        }
      }
    }
  }

  public Node delete(int value) {
    Node current_node = this.get(value);
    this.size--;
    if (current_node.getParent().getLeft() == current_node) {
      if (current_node.isLeaf()) {
        current_node.getParent().setLeft(null);
      } else if (current_node.getLeft() == null) {
        current_node.getParent().setLeft(current_node.getRight());
      } else if (current_node.getRight() == null) {
        current_node.getParent().setLeft(current_node.getLeft());
      }
    } else {
      if (current_node.isLeaf()) {
        current_node.getParent().setRight(null);
      } else if (current_node.getLeft() == null) {
        current_node.getParent().setRight(current_node.getRight());
      } else if (current_node.getRight() == null) {
        current_node.getParent().setRight(current_node.getLeft());
      }
    }
    return current_node;
  }

  public String dfs() {
    Node currentNode = this.root;
    String output = String.format("%d ", currentNode.getValue());
    if (currentNode.getLeft() != null) {
      output += dfs(currentNode.getLeft());
    }
    if (currentNode.getRight() != null) {
      output += dfs(currentNode.getRight());
    }
    return output;
  }

  public String dfs(Node node) {
    Node currentNode = node;
    String output = String.format("%d ", currentNode.getValue());
    if (currentNode.getLeft() != null) {
      output += dfs(currentNode.getLeft());
    }
    if (currentNode.getRight() != null) {
      output += dfs(currentNode.getRight());
    }
    return output;
  }

  public String bfs() {
    Node currentNode;
    String output = "";
    ArrayDeque<Node> queue = new ArrayDeque<>();
    queue.push(this.root);
    while (queue.size() > 0) {
      currentNode = queue.poll();
      if (currentNode.getLeft() != null) {
        queue.offer(currentNode.getLeft());
      }
      if (currentNode.getRight() != null) {
        queue.offer(currentNode.getRight());
      }
      output += String.format("%d ", currentNode.getValue());
    }
    return output;
  }
}
