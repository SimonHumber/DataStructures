#include <stdio.h>
#include <stdlib.h>

void mergeSort(int array[], int length) {
  int midpoint = length / 2;
  int leftHalf[midpoint];
  int rightHalf[length - midpoint];
  int leftLength = sizeof(leftHalf) / sizeof(leftHalf[0]);
  int rightLength = sizeof(rightHalf) / sizeof(rightHalf[0]);
  for (int i = 0; i < leftLength; i++) {
    leftHalf[i] = array[i];
  }
  for (int i = 0, index = midpoint; i < rightLength; i++, index++) {
    rightHalf[i] = array[index];
  }

  if (leftLength > 1) {
    mergeSort(leftHalf, leftLength);
  }
  if (rightLength > 1) {
    mergeSort(rightHalf, rightLength);
  }

  int leftIndex = 0;
  int rightIndex = 0;
  while (leftIndex < leftLength && rightIndex < rightLength) {
    if (rightHalf[rightIndex] > leftHalf[leftIndex]) {
      array[leftIndex + rightIndex] = leftHalf[leftIndex];
      leftIndex++;
    } else {
      array[leftIndex + rightIndex] = rightHalf[rightIndex];
      rightIndex++;
    }
  }
  while (leftIndex < leftLength) {
    array[leftIndex + rightIndex] = leftHalf[leftIndex];
    leftIndex++;
  }
  while (rightIndex < rightLength) {
    array[leftIndex + rightIndex] = rightHalf[rightIndex];
    rightIndex++;
  }
}
int main() {
  int arr[] = {5, 1, 2, 40, 9, 8};
  int arrayLength = sizeof(arr) / sizeof(arr[0]);
  mergeSort(arr, arrayLength);

  for (int i = 0; i < arrayLength; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");

  return 0;
}
