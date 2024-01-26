/** Queue */
public class Queue {

  private int size = 0;
  private QueueNode tail = null;
  private QueueNode head = null;

  public void push(int value) {
    QueueNode newNode = new QueueNode(value);
    if (this.size == 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.head.setPrev(newNode);
      newNode.setNext(this.head);
      this.head = newNode;
    }
    this.size++;
  }

  public int pop() {
    QueueNode output = this.tail;
    if (this.size == 0) {
      throw new IndexOutOfBoundsException("Queue is already 0!!");
    } else if (this.size == 1) {
      this.size--;
      this.tail = null;
      this.head = null;
      return output.getValue();
    } else {
      this.size--;
      this.tail = this.tail.getPrev();
      this.tail.setNext(null);
      return output.getValue();
    }
  }

  public int getSize() {
    return this.size;
  }
}
