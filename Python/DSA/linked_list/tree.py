class Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None
        self._parent = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    def is_leaf(self):
        return self._left is None and self._right is None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        self.size += 1
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if new_node.value < current_node.value:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        new_node.parent = current_node
                        break
                else:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        new_node.parent = current_node
                        break

    def dfs(self, value, current_node=None):
        if self.root is None:
            raise IndexError("Value not found!")

        if current_node is None:
            current_node = self.root

        if current_node.value == value:
            return current_node
        elif value < current_node.value:
            if current_node.left:
                current_node = self.dfs(value, current_node.left)
            else:
                raise IndexError("Value not found!")
        else:
            if current_node.right:
                current_node = self.dfs(value, current_node.right)
            else:
                raise IndexError("Value not found!")

        return current_node

    def dfs_str(self, current_node=None):
        if self.root is None:
            return ""

        if current_node is None:
            current_node = self.root
        output = str(current_node.value)+" "
        if current_node.left:
            output += str(self.dfs_str(current_node.left))
        if current_node.right:
            output += str(self.dfs_str(current_node.right))
        return output

    def bfs(self, value):
        if self.root is None:
            raise IndexError("value not found!")

        queue = Deque()
        queue.push(self.root)

        while True:
            current_node = queue.pop()
            if current_node.value == value:
                return current_node
            else:
                if queue.size == 0:
                    raise IndexError

                if current_node.left:
                    queue.push(current_node.left)
                if current_node.right:
                    queue.push(current_node.right)

    def delete(self, value):
        current_node = self.dfs(value)
        if current_node.left and current_node.right:
            replacement_node = current_node.right
            while True:
                if replacement_node.left:
                    replacement_node = replacement_node.left
                else:
                    if current_node.parent:
                        if current_node.parent.left == current_node:
                            current_node.parent.left = replacement_node
                        else:
                            current_node.parent.right = replacement_node
                    replacement_node.left = current_node.left
                    current_node.left.parent = replacement_node
                    replacement_node.parent.left = None
                    replacement_node.parent = current_node.parent
                    if current_node.right != replacement_node:
                        replacement_node.right = current_node.right

                    break
        elif current_node.left:
            replacement_node = current_node.left
            replacement_node.left, replacement_node.right, replacement_node.parent = current_node.left, current_node.right, current_node.parent
        elif current_node.right:
            replacement_node = current_node.right
            replacement_node.left, replacement_node.right, replacement_node.parent = current_node.left, current_node.right, current_node.parent
        current_node.parent = None
        current_node.left = None
        current_node.right = None

        return current_node

    def __str__(self):
        if self.root is None:
            return ""
        queue = Deque()
        queue.push(self.root)
        output = ""

        while True:
            current_node = queue.pop()
            output += str(current_node.value)+" "

            if current_node.left:
                queue.push(current_node.left)
            if current_node.right:
                queue.push(current_node.right)
            if queue.size == 0:
                return output


class QNode:
    def __init__(self, node):
        self._node = node
        self.next_node = None
        self.prev_node = None

    @property
    def next(self):
        return self.next_node

    @next.setter
    def next(self, node):
        self.next_node = node

    @property
    def prev(self):
        return self.prev_node

    @prev.setter
    def prev(self, node):
        self.prev_node = node

    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, node):
        self._node = node


class Deque:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push(self, node):
        self.size += 1
        new_node = QNode(node)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop(self):
        if self.tail is None:
            raise IndexError
        else:
            self.size -= 1
            output = self.tail
            if self.tail.prev:
                self.tail = self.tail.prev
                output.prev = None
            else:
                self.tail = None
                self.head = None
            return output.node

    def dequeue(self):
        if self.head is None:
            raise IndexError
        else:
            output = self.head
            if self.head.next:
                self.head = self.head.next
                output.next = None
            else:
                self.head = None
                self.tail = None
            return output.node


tree = BinaryTree()
tree.add(4)
tree.add(2)
tree.add(8)
tree.add(1)
tree.add(3)
tree.add(5)
tree.add(7)
tree.add(9)
tree.add(8.5)
print(tree)
print(tree.dfs_str())
tree.delete(8)
print(tree)

# 1
# 0 2
# -1   3
# 2.5 4
