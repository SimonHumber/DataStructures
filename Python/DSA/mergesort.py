def mergeSort(array):
    # sort given list in ascending order
    # divide: find midpoint of list and divide into sublists
    # conquer: recursively sort sublists created in previous step
    # combine: merge sorted sublists created in previous step
    # runtime should be O(n log n)
    # space is O(n)
    if len(array) <= 1:
        return array
    left_half, right_half = split(array)
    left = mergeSort(left_half)
    right = mergeSort(right_half)

    return merge(left, right)


def split(array):
    # divide unsorted list at midpoint into sublists
    # returns 2 sublists, left and right
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return left, right


def merge(left, right):
    # merges 2 lists, sorting them in the process and returns new list

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verifySort(array):
    n = len(array)

    if n == 0 or n == 1:
        return True

    return array[0] < array[1] and verifySort(array[1:])


with open("1m.txt") as f:
    numbers = [int(i) for i in f]

print(mergeSort(numbers))
