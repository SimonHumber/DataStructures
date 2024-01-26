# recursive binary search
def recursiveBinary(inputList, target):
    if len(inputList) == 0:
        return False
    else:
        midpoint = len(inputList) // 2

        if inputList[midpoint] == target:
            return True
        else:
            if inputList[midpoint] < target:
                return recursiveBinary(inputList[midpoint + 1:], target)
            else:
                return recursiveBinary(inputList[:midpoint], target)


def verify(index):
    print("Target found:", index)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
verify(recursiveBinary(numbers, 12))

verify(recursiveBinary(numbers, 8))
