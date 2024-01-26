def linearSearch(listInput, target):
    # returns index position of target if found, else return none

    # checking list size is a constant time operation
    # if this were naive implementation (we implement list ourselves), we incur linear cost
    for index in range(0, len(listInput)):
        if listInput[index] == target:
            return index
    return None


def verify(index):
    if index is not None:
        print("Target found at index ", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linearSearch(numbers, 12)

verify(result)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linearSearch(numbers, 8)

verify(result)
