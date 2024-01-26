class Node:
    def __init__(self, value: int):
        self._value: int = value
        self._next_node = None
        self._prev_node = None

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, next_node):
        self._prev_node = next_node


class Linked_List:
    def __init__(self):
        self.size = 0
        self.head: Node
        self.tail: Node

    def append(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.head.prev_node = Node(value)
            new_node.next_node = self.head
            self.head = new_node
        self.size += 1

    def get(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")

        current_index = 0
        current_node = self.head
        while current_index < index:
            current_index += 1
            if current_node.next_node is not None:
                current_node = current_node.next_node
        return current_node.value

    def __str__(self):
        output = "+"
        output = ""
        current_node = self.head
        counter = 0
        while counter < self.size:
            counter += 1
            output += str(current_node.value)
            if current_node.next_node is not None:
                output += ", "
                current_node = current_node.next_node
        return output


link = Linked_List()
link.append(4)
link.append(5)
link.prepend(3)
print(link.get(2))
print(link)
