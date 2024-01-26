function mergeSort(array: Array<number>) {
  const MIDPOINT = array.length / 2;
  var leftHalf = array.slice(0, MIDPOINT);
  var rightHalf = array.slice(MIDPOINT);
  if (leftHalf.length > 1) {
    leftHalf = mergeSort(leftHalf);
  }
  if (rightHalf.length > 1) {
    rightHalf = mergeSort(rightHalf);
  }
  var leftIndex = 0;
  var rightIndex = 0;
  var sortedArray: Array<number> = [];

  while (leftIndex < leftHalf.length && rightIndex < rightHalf.length) {
    if (leftHalf[leftIndex] < rightHalf[rightIndex]) {
      sortedArray[leftIndex + rightIndex] = leftHalf[leftIndex];
      leftIndex++;
    } else {
      sortedArray[leftIndex + rightIndex] = rightHalf[rightIndex];
      rightIndex++;
    }
  }
  while (leftIndex < leftHalf.length) {
    sortedArray[leftIndex + rightIndex] = leftHalf[leftIndex];
    leftIndex++;
  }
  while (rightIndex < rightHalf.length) {
    sortedArray[leftIndex + rightIndex] = rightHalf[rightIndex];
    rightIndex++;
  }
  return sortedArray;
}
var array: Array<number> = [2, 8, 3, 0, -1];
console.log(mergeSort(array));
