class Deque:
    def __init__(self, array=[]):
        self.array = array

    def addFront(self, value):
        self.array.insert(0, value)

    def addRear(self, value):
        self.array.append(value)

    def removeFront(self):
        return self.array.pop(0)

    def removeRear(self):
        return self.array.pop()

    def getArray(self):
        return self.array

    def getIndex(self, index):
        return self.array[index]


def palindrome(input):
    palin = Deque(input)
    print(palin.getArray())
    while len(palin.getArray()) > 1:
        if palin.removeFront() == palin.removeRear():
            continue
        else:
            return False

    return True


print(palindrome([1, 2, 1]))
