//TODO: find out why output is undefined
class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
    this.parent = null;
  }
  getValue() {
    return this.value;
  }
  setValue(value) {
    this.value = value;
  }
  getLeft() {
    return this.left;
  }
  setLeft(node) {
    this.left = node;
  }
  getRight() {
    return this.right;
  }
  setRight(node) {
    this.right = node;
  }
  getParent() {
    return this.parent;
  }
  setParent(node) {
    this.parent = node;
  }
  isLeaf() {
    if (this.left == null && this.right == null) {
      return true;
    } else {
      return false;
    }
  }
}

class Tree {
  constructor() {
    this.root = null;
    this.size = 0;
  }
  insert(value) {
    var newNode = new Node(value);
    if (this.size == 0) {
      this.root = newNode;
    } else {
      var parentNode = this.root;
      while (true) {
        if (value < parentNode.getValue()) {
          if (parentNode.getLeft() == null) {
            parentNode.setLeft(newNode);
            newNode.setParent(parentNode);
            break;
          } else {
            parentNode = parentNode.getLeft();
          }
        } else {
          if (parentNode.getRight() == null) {
            parentNode.setRight(newNode);
            newNode.setParent(parentNode);
            break;
          } else {
            parentNode = parentNode.getRight();
          }
        }
      }
    }
    this.size++;
  }
  get(value) {
    if (this.size == 0) {
      throw "Cannot find because size is 0!!";
    }
    var parentNode = this.root;
    while (true) {
      if (value == parentNode.getValue()) {
        return parentNode;
      } else if (value < parentNode.getValue()) {
        if (parentNode.getLeft() == null) {
          throw "Cannot find value in tree!!";
        } else {
          parentNode = parentNode.getLeft();
        }
      } else {
        if (parentNode.getRight() == null) {
          throw "Cannot find value in tree!!";
        } else {
          parentNode = parentNode.getRight();
        }
      }
    }
  }
  delete(value) {
    var currentNode = this.get(value);
    var parentNode = self.root;
    if (currentNode.value < parentNode.value) {
      if (currentNode.isLeaf()) {
        parentNode.setLeft(null);
      } else if (currentNode.getRight() == null) {
        parentNode.setLeft(currentNode.getLeft());
      } else if (currentNode.getLeft() == null) {
        parentNode.setLeft(currentNode.getRight());
      } else {
        replacement = currentNode.getRight();
        while (replacement.getLeft() != null) {
          replacement = replacement.getLeft();
        }
        parentNode.setLeft(replacement);
      }
    } else {
      if (currentNode.isLeaf()) {
        parentNode.setRight(null);
      } else if (currentNode.getRight() == null) {
        parentNode.setRight(currentNode.getLeft());
      } else if (currentNode.getLeft() == null) {
        parentNode.setRight(currentNode.getLeft());
      } else {
        replacement = currentNode.getRight();
        while (replacement.getLeft() != null) {
          replacement = replacement.getLeft();
        }
        parentNode.setRight(replacement);
      }
    }
  }
  dfs(node = null) {
    if (this.size == 0) {
      return null;
    }
    if (node == null) {
      var currentNode = this.root;
    } else {
      var currentNode = node;
    }
    var output = currentNode.getValue() + " ";
    if (currentNode.getLeft() != null) {
      output += this.dfs(currentNode.getLeft());
    }
    if (currentNode.getRight() != null) {
      output += this.dfs(currentNode.getRight());
    }
    return output;
  }
  bfs() {
    if (this.size == 0) {
      return null;
    }
    var currentNode;
    var array = [];
    array[0] = this.root;
    var output = "";
    while (array.length > 0) {
      currentNode = array.pop();
      if (currentNode.getLeft() != null) {
        array.unshift(currentNode.getLeft());
      }
      if (currentNode.getRight() != null) {
        array.unshift(currentNode.getRight());
      }
      output += currentNode.getValue() + " ";
    }
    return output;
  }
}

tree = new Tree();
tree.insert(4);
tree.insert(2);
tree.insert(6);
tree.insert(3);
tree.insert(1);
console.log(tree.dfs());
console.log(tree.bfs());
