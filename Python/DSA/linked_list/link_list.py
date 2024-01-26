class Node:
    def __init__(self, value):
        self.value = value
        self._next = None

    @property
    def node_value(self):
        return self.value

    @node_value.setter
    def node_value(self, new_value):
        self.value = new_value

    @property
    def next_node(self):
        return self._next

    @next_node.setter
    def next_node(self, new_next):
        self._next = new_next


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head, new_node.next_node = new_node, self.head
        self.size += 1

    def append(self, value):
        new_node = Node(value)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
        else:
            prev_node = self.head
            current_node = prev_node.next_node
            while index > 1:
                if current_node is None:
                    raise IndexError("Index out of range!")
                else:
                    prev_node, current_node = current_node, current_node.next_node
                    index -= 1
            if current_node is None:
                self.append(value)
            else:
                prev_node.next_node = new_node
                new_node.next_node = current_node
                self.size += 1

    def delete(self, index):
        current_node = self.head
        if index == 0:
            output = self.head.node_value
            self.head = self.head.next_node
            self.size -= 1
            return output
        elif index >= self.size:
            raise IndexError("Index out of range!")
        else:
            while index > 1:
                current_node = current_node.next_node
                index -= 1
            prev_node = current_node
            current_node = current_node.next_node
            prev_node.next_node = current_node.next_node
            if current_node == self.tail:
                self.tail = prev_node
            self.size -= 1
            return current_node.node_value

    def get_index(self, index):
        if index == 0:
            return self.head.node_value
        elif index == self.size-1:
            return self.tail.node_value
        elif index >= self.size:
            raise IndexError("Index out of range!")
        else:
            current_node = self.head
            while index > 0:
                current_node = current_node.next_node
                index -= 1
            return current_node.node_value

    def set_index(self, index, value):
        if index > self.size-1:
            raise IndexError("Index out of range!")
        current_node = self.head
        while index > 0:
            current_node = current_node.next_node
            index -= 1
        current_node.node_value = value

    def __repr__(self):
        array = []
        current_node = self.head
        if self.size == 0:
            return str(array)
        elif self.size == 2:
            array.append(current_node.node_value)
        elif self.size > 2:
            next_node = current_node.next_node
            while next_node is not None:
                array.append(current_node.node_value)
                current_node = next_node
                next_node = current_node.next_node
        array.append(self.tail.node_value)
        return str(array)

    def reverse(self):
        if self.size <= 1:
            pass
        elif self.size == 2:
            self.head, self.tail = self.tail, self.head
        else:
            prev_node = self.head
            current_node = prev_node.next_node
            next_node = current_node.next_node
            self.tail = self.head
            self.tail.next_node = None
            while next_node is not None:
                current_node.next_node = prev_node
                prev_node = current_node
                current_node = next_node
                next_node = next_node.next_node
            current_node.next_node = prev_node
            self.head = current_node


object = Linked_list()
object.prepend(4)
object.prepend(3)
object.append(5)
object.append(6)
object.insert(4, 7)
print(object)
object.reverse()
print(object)
