# create empty array, find smallest number in input array
# append that number to empty array and delete it from input array
# repeat until input array is empty
# time and space complexity: O(n^2)
def selectSort(array):
    sorted = []
    if len(array) > 1:
        while 0 < len(array):
            numcheck = array[0]
            indexcheck = 0
            for y in range(len(array)):
                if array[y] < numcheck:
                    numcheck = array[y]
                    indexcheck = y
            sorted.append(numcheck)
            del array[indexcheck]
    else:
        return array

    return sorted


with open("10000.txt") as f:
    numbers = [int(i) for i in f]

print(selectSort(numbers))
