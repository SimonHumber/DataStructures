class Vertex:
    def __init__(self, value):
        self._value = value
        self._neighbours = {}

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get_neighbours(self):
        return self._neighbours

    def delete_neighbours(self):
        self._neighbours = []

    def add_neighbour(self, vertex):
        self._neighbours[vertex.value] = vertex

    def neighbour(self, value):
        return self._neighbours[value]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.size = 0
        self.root = None

    def add(self, value):
        if value in self.vertices:
            raise KeyError("Value already exists in graph!!")
        else:
            new_vertex = Vertex(value)
            self.vertices[value] = new_vertex
            if self.size == 0:
                self.root = new_vertex
        self.size += 1

    def connect(self, first, second):
        if first not in self.vertices:
            first_vertex = Vertex(first)
            self.vertices[first] = first_vertex
            if self.root is None:
                self.root = first_vertex
            self.size += 1
        else:
            first_vertex = self.vertices[first]
        if second not in self.vertices:
            second_vertex = Vertex(second)
            self.vertices[second] = second_vertex
            self.size += 1
        else:
            second_vertex = self.vertices[second]

        first_vertex.add_neighbour(second_vertex)
        second_vertex.add_neighbour(first_vertex)

    def delete(self, value):
        if value not in self.vertices:
            raise KeyError("Value does not exist in graph!!")
        else:
            vertex = self.vertices[value]
            for neighbour in vertex.get_neighbours():
                neighbour.get_neighbours().pop(value)
            vertex.delete_neighbours()

    # TODO complete this breadth first search create queue algorithm
    def bfs(self, value=None):
        if self.root is None:
            return None
        elif value is None:
            value = self.root.value
        elif value not in self.vertices:
            raise KeyError("Value does not exist in graph!!")
        queue = Queue()
        queue.add(value)
        output = []
        while queue.size > 0:
            value = queue.pop()
            current_vertex = self.vertices[value]
            output.append(value)
            for neighbour in current_vertex.get_neighbours():
                if neighbour not in output:
                    queue.add(neighbour)
        return output

    def dfs(self, value=None, searched=[]):
        if self.root is None:
            return None
        elif value is None:
            value = self.root.value
        elif value not in self.vertices:
            raise KeyError(str(value)+" does not exist in graph!!")

        current_vertex = self.vertices[value]
        searched.append(current_vertex.value)
        for neighbour in current_vertex.get_neighbours():
            if neighbour not in searched:
                searched = self.dfs(neighbour, searched)

        return searched

    def get_vertex(self, value):
        return self.vertices[value]


class Node:
    def __init__(self, value):
        self._value = value
        self.prev_node = None
        self.next_node = None

    @property
    def prev(self):
        return self.prev_node

    @prev.setter
    def prev(self, value):
        self.prev_node = value

    @property
    def next(self):
        return self.next_node

    @next.setter
    def next(self, value):
        self.next_node = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
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
        if self.size > 1:
            self.tail = self.tail.prev
            self.tail.next = None
        elif self.size == 1:
            self.tail = None
            self.head = None
        else:
            return None
        self.size -= 1
        return output.value


graph = Graph()
graph.add(5)
graph.add(2)
graph.connect(5, 2)
graph.connect(5, 1)
graph.connect(2, 3)
graph.connect(2, 6)
graph.connect(3, 4)
print(graph.dfs())
print(graph.bfs())
