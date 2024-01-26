class Node {
  constructor(value) {
    this.value = value;
    this.nextNode = null;
  }

  getValue() {
    return this.value;
  }

  setValue(value) {
    this.value = value;
  }

  getNext() {
    return this.nextNode;
  }

  setNext(nextNode) {
    this.nextNode = nextNode;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  append(value) {
    const newNode = new Node(value);
    this.length++;
    if (this.tail == null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.setNext(newNode);
      this.tail = newNode;
    }
  }
  prepend(value) {
    this.length++;
    const newNode = new Node(value);
    if (this.head == null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.setNext(this.head);
      this.head = newNode;
    }
  }

  insert(index, value) {
    if (index > this.length || index < 0) {
      throw "Index out of range";
    } else if (index == 0) {
      this.prepend(value);
    } else if (index == this.length) {
      this.append(value);
    } else {
      this.length++;
      const newNode = new Node(value);
      var prevNode = this.head;
      var currentNode = this.head.getNext();

      for (var i = 0; i < index - 1; i++) {
        prevNode = currentNode;
        currentNode = currentNode.getNext();
      }
      prevNode.setNext(newNode);
      newNode.setNext(currentNode);
    }
  }

  delete(index) {
    if (index > this.length || index < 0) {
      throw "Index out of range";
    }
    var delNode;
    this.length--;
    if (index == 0) {
      delNode = this.head;
      this.head = this.head.getNext();
      return delNode;
    } else {
      var prevNode = this.head;
      var currentNode = this.head.getNext();
      for (var i = 0; i < index - 1; i++) {
        prevNode = currentNode;
        currentNode = currentNode.getNext();
      }
      delNode = currentNode;
      prevNode.setNext(currentNode.getNext());
      return delNode;
    }
  }
  getList() {
    if (this.length == 0) {
      return [];
    } else {
      var currentNode = this.head;
      var nextNode = this.head.getNext();
      var list = [];
      for (var i = 0; i < this.length - 1; i++) {
        list.push(currentNode.getValue());
        currentNode = nextNode;
        nextNode = nextNode.getNext();
      }
      list.push(currentNode.getValue());
      return list;
    }
  }

  reverse() {
    const oldTail = this.tail;
    const oldHead = this.head;
    if (this.length <= 1) {
    } else if (this.length == 2) {
      this.head = oldTail;
      this.tail = oldHead;
    } else {
      var prevNode = this.head;
      var currentNode = this.head.getNext();
      var nextNode = currentNode.getNext();
      for (var i = 0; i < this.length - 2; i++) {
        currentNode.setNext(prevNode);
        prevNode = currentNode;
        currentNode = nextNode;
        nextNode = nextNode.getNext();
      }
      currentNode.setNext(prevNode);
      this.head = oldTail;
      this.tail = oldHead;
    }
    return this.getList();
  }
}

var newList = new LinkedList();

newList.append(4);
newList.append(5);
newList.prepend(3);
newList.insert(2, 2);
console.log(newList.getList());
console.log(newList.reverse());
