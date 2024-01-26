public class QueueNode {
  private int value;
  private QueueNode next;
  private QueueNode prev;

  public QueueNode(int value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }

  public int getValue() {
    return this.value;
  }

  public void setValue(int value) {
    this.value = value;
  }

  public QueueNode getNext() {
    return this.next;
  }

  public void setNext(QueueNode node) {
    this.next = node;
  }

  public QueueNode getPrev() {
    return this.prev;
  }

  public void setPrev(QueueNode node) {
    this.prev = node;
  }
}
