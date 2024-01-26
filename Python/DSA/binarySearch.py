def binarySearch(listInput, target):
    first = 0
    last = len(listInput) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if listInput[midpoint] == target:
            return midpoint

        elif listInput[midpoint] < target:
            first = midpoint + 1

        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index ", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binarySearch(numbers, 12)

verify(result)

verify(binarySearch(numbers, 7))
