# split list into 2 halves recursively until you reach single elements
# sort the single elements, move back up tree, keep sorting
# return the two halves and pivot element
# space and time complexity worst case O(n^2)
# worst case is when pivot is largest or smallest number for EVERY recursion
# aka worst case is when list is already sorted
# space and time complexity average case O(n log n)
def quicksort(array):
    if len(array) > 1:
        pivot = [array[0]]
        beforePivot = []
        afterPivot = []
        for index in range(1, len(array)):
            if array[index] < pivot[0]:
                beforePivot.append(array[index])
            elif array[index] > pivot[0]:
                afterPivot.append(array[index])
            else:
                pivot.append(array[index])
        sortedBefore = quicksort(beforePivot)
        sortedAfter = quicksort(afterPivot)
    else:
        return array
    return sortedBefore + pivot + sortedAfter


with open("1m.txt") as f:
    numbers = [int(i) for i in f]

# print(quicksort(numbers))

array = [5]
print(array[-1])
