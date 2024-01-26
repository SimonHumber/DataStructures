import java.util.Arrays;

public class LinkedList {
  private Node head = null;
  private Node tail = null;
  private int size = 0;

  public void prepend(int value) {
    size++;
    Node newNode = new Node(value);
    if (head == null) {
      head = newNode;
      tail = newNode;
    } else {
      newNode.setNext(head);
      head = newNode;
    }
  }

  public void append(int value) {
    size++;
    Node newNode = new Node(value);
    if (tail == null) {
      head = newNode;
      tail = newNode;
    } else {
      tail.setNext(newNode);
      tail = newNode;
      tail.setNext(null);
    }
  }

  public void insert(int index, int value) {
    size++;
    Node newNode = new Node(value);
    if (index == 0) {
      prepend(value);
    } else if (index > size) {
      throw new ArrayIndexOutOfBoundsException("Out of range!");
    } else {
      int i = 0;
      Node prevNode = head;
      while (i < index - 1) {
        prevNode = prevNode.getNext();
        i++;
      }
      if (prevNode.getNext() == null) {
        append(value);
      }
      newNode.setNext((prevNode.getNext()));
      prevNode.setNext(newNode);
    }
  }

  public void replace(int index, int value) {
    int i = 0;
    Node newNode = head;
    while (i < index) {
      newNode = newNode.getNext();
      i++;
    }
    newNode.setNode(value);
  }

  public int delete(int index) {
    size--;
    if (index == 0) {
      Node output = head;
      head = head.getNext();
      return output.getNode();
    } else if (index > size) {
      throw new ArrayIndexOutOfBoundsException("Out of range!");
    } else {
      Node prevNode = head;
      int i = 0;
      while (i < index - 1) {
        prevNode = head.getNext();
        i++;
      }
      Node currentNode = prevNode.getNext();
      if (currentNode.getNext() == null) {
        prevNode.setNext(null);
        return currentNode.getNode();
      } else {
        Node deleteNode = currentNode.getNext();
        prevNode.setNext(deleteNode);
        Node output = currentNode.getNext();
        return output.getNode();
      }
    }
  }

  public int getIndex(int index) {
    if (index == 0) {
      return head.getNode();
    } else {
      int i = 0;
      Node currentNode = head;
      while (i != index) {
        currentNode = currentNode.getNext();
        i++;
      }
      return currentNode.getNode();
    }
  }

  public String getList() {
    int[] output = new int[size];
    int i = 0;
    Node currentNode = head;
    while (i < size) {
      output[i] = currentNode.getNode();
      currentNode = currentNode.getNext();
      i++;
    }
    return Arrays.toString(output);
  }

  public int getSize() {
    return size;
  }

  public String reverse() {
    Node prev_node = head;
    head = tail;
    tail = prev_node;
    if (size > 2) {
      Node current_node = prev_node.getNext();
      Node next_node = current_node.getNext();
      while (next_node != null) {
        current_node.setNext(prev_node);
        prev_node = current_node;
        current_node = next_node;
        next_node = next_node.getNext();
      }
      tail.setNext(null);
    }
    head.setNext(prev_node);
    return getList();
  }
}
