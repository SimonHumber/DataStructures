public class BinaryHeap {
  private LinkedList heap = new LinkedList();

  public void insert(int value) {
    heap.append(value);
    if (heap.getSize() > 1) {
      sortup();
    }
  }

  public void sortup() {
    int child = heap.getSize() - 1;
    int parent;
    while (child > 0) {
      if ((child - 1) % 2 == 0) {
        parent = (child - 1) / 2;
      } else {
        parent = (child - 2) / 2;
      }
      if (heap.getIndex(child) < heap.getIndex(parent)) {
        int temp = heap.getIndex(parent);
        heap.replace(parent, heap.getIndex(child));
        heap.replace(child, temp);
      } else {
        break;
      }
    }
  }

  public int poll() {
    int first = heap.getIndex(0);
    int last = heap.getIndex(heap.getSize() - 1);
    if (heap.getSize() > 1) {
      sortdown();
    }
    return heap.delete(heap.getSize() - 1);
  }

  public void sortdown() {
    int parent = 0;
    while (parent < heap.getSize()) {
      if (heap.getIndex(parent) > heap.getIndex(parent * 2 + 1)) {
        int temp = heap.getIndex(parent);
        heap.replace(parent, heap.getIndex(parent * 2 - 1));
        heap.replace(parent * 2 + 1, temp);
      } else if (heap.getIndex(parent) > heap.getIndex(parent * 2 + 1)) {
        int temp = heap.getIndex(parent);
        heap.replace(parent, heap.getIndex(parent * 2 + 2));
        heap.replace(parent * 2 + 2, temp);
      } else {
        break;
      }
    }
  }

  public String getArray() {
    return heap.getList();
  }
}
