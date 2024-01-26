class QueueNode:
    def __init__(self, value):
        self._value = value
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
    def q_value(self):
        return self._value

    @q_value.setter
    def q_value(self, value):
        self._value = value


class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def add(self, value):
        new_node = QueueNode(value)
        if self.size == 0:
            self.tail = new_node
            self.head = new_node
        elif self.size == 1:
            self.head = new_node
            self.tail.prev = new_node
            self.head.next = self.tail
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def pop(self):
        output = self.tail
        if self.size == 0:
            return None
        elif self.size == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return output

    def __len__(self):
        return self.size


class Node:
    def __init__(self, value: int):
        self._value: int = value
        self.left_node = None
        self.right_node = None
        self.parent_node = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self.left_node

    @left.setter
    def left(self, node):
        self.left_node = node

    @property
    def right(self):
        return self.right_node

    @right.setter
    def right(self, node):
        self.right_node = node

    @property
    def parent(self):
        return self.parent_node

    @parent.setter
    def parent(self, parent_node):
        self.parent_node = parent_node

    def is_leaf(self):
        if self.left_node is None and self.right_node is None:
            return True
        else:
            return False


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert_node(self, value):
        new_node = Node(value)
        self.size += 1
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if new_node.value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        new_node.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        new_node.parent = current_node
                        break
                    else:
                        current_node = current_node.right

    def get_node(self, value):
        if self.root is None:
            raise KeyError("Element not in tree!!")
        else:
            parent = self.root
            while True:
                if parent.value == value:
                    return parent
                elif parent.value > value:
                    if parent.left is None:
                        raise KeyError("Element not in tree!!")
                    else:
                        parent = parent.left
                else:
                    if parent.right is None:
                        raise KeyError("Element not in tree!!")
                    else:
                        parent = parent.right

    def delete(self, value):
        current_node = self.get_node(value)
        self.size -= 1
        parent_node = current_node.parent
        if current_node.is_leaf():
            if parent_node is None:
                self.root = None
                return current_node
            elif parent_node.left == current_node:
                parent_node.left = None
                return current_node
            else:
                parent_node.right = None
                return current_node
        elif current_node.left is None:
            if parent_node is None:
                self.root = current_node.right
            elif parent_node.left == current_node:
                parent_node.left = current_node.right
            else:
                parent_node.right = current_node.right
        elif current_node.right is None:
            if parent_node is None:
                self.root = current_node.left
            elif parent_node.left == current_node:
                parent_node.left = current_node.left
            else:
                parent_node.right = current_node.left
        else:
            smallest_larger_node = current_node.right
            while smallest_larger_node.left:
                smallest_larger_node = smallest_larger_node.left
            self.delete(smallest_larger_node.value)
            smallest_larger_node.left = current_node.left
            smallest_larger_node.right = current_node.right
            if parent_node is None:
                self.root = smallest_larger_node
                smallest_larger_node.parent = None
            elif parent_node.left == current_node:
                parent_node.left = smallest_larger_node
                smallest_larger_node.parent = parent_node
            else:
                parent_node.right = smallest_larger_node
                smallest_larger_node.parent = parent_node

    def bfs(self):
        if self.root is None:
            return None
        else:
            queue = Queue()
            queue.add(self.root)
            output = ""
            while len(queue) > 0:
                current_node = queue.tail
                if current_node.q_value.left:
                    queue.add(current_node.q_value.left)
                if current_node.q_value.right:
                    queue.add(current_node.q_value.right)

                output += str(queue.pop().q_value.value)+" "
        return output

    def dfs(self, node=None):
        if self.root is None:
            return None
        elif node is None:
            node = self.root

        output = str(node.value)+" "

        if node.left:
            output += str(self.dfs(node.left))
        if node.right:
            output += str(self.dfs(node.right))

        return output

    def dfs2(self, node=None, array=[]) -> list[int] | None:
        if self.root is None:
            return None
        if node is None:
            node = self.root
        array.append(node.value)
        if node.left:
            array = self.dfs2(node.left, array)
        if node.right:
            array = self.dfs2(node.right, array)
        return array

    # dfs post order left to right
    def postorder(self, node=None, array=[]):
        if self.root is None:
            return None
        if node is None:
            node = self.root
        if node.left:
            array = self.postorder(node.left, array)
        if node.right:
            array = self.postorder(node.right, array)
        array.append(node.value)
        return array


bst = Tree()
bst.insert_node(5)
bst.insert_node(3)
bst.insert_node(2)
bst.insert_node(1)
bst.insert_node(6)
bst.insert_node(4)
bst.insert_node(7)
bst.insert_node(5)
bst.insert_node(2)
bst.insert_node(3)
bst.insert_node(4)
print(bst.bfs())
print(bst.dfs())
print(bst.dfs2())
print(bst.postorder())
