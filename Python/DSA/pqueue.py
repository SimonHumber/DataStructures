class Pqueue:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)
        if len(self.array) > 1:
            self.sortup()

    def sortup(self):
        child = len(self.array)-1
        while child > 0:
            if (child-1) % 2 == 1:
                parent = (child-2)//2
            else:
                parent = (child-1)//2
            if self.array[child] < self.array[parent]:
                self.array[child], self.array[parent] = self.array[parent], self.array[child]
                child = parent
            else:
                break

    def poll(self):
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        self.sortdown()
        return self.array.pop()

    def sortdown(self):
        parent = 0

        while parent < len(self.array)-1:
            if self.array[parent] > self.array[parent*2+1]:
                self.array[parent], self.array[parent*2 +
                                               1] = self.array[parent*2+1], self.array[parent]
                parent = parent*2+1
            elif self.array[parent] > self.array[parent*2+2]:
                self.array[parent], self.array[parent*2 +
                                               2] = self.array[parent*2+2], self.array[parent]
                parent = parent*2+2
            else:
                break

    def getArray(self):
        return self.array


test = Pqueue()

test.insert(5)
test.insert(6)
test.insert(2)
test.insert(10)
test.insert(8)
test.insert(4)
test.insert(-1)
print(test.getArray())
