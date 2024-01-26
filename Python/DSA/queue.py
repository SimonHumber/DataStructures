class Queue:
    def __init__(self, array=[]):
        self.array = array

    def enqueue(self, value):
        self.array.insert(0, value)

    def dequeue(self):
        return self.array.pop()

    def peek(self):
        if len(self.array) == 0:
            return None
        else:
            return self.array[-1]

    def getArray(self):
        return self.array


def hotPotato(array, num):
    potato = Queue(array)
    print(potato.getArray())
    x = 0
    while len(potato.getArray()) > 1:
        x += 1
        if x < num:
            potato.enqueue(potato.dequeue())
        else:
            print(potato.getArray())
            potato.dequeue()
            x = 0
    return potato.getArray()


print(hotPotato(["Brad", "Kent", "Jane", "Susan", "David", "Bill"], 5))
