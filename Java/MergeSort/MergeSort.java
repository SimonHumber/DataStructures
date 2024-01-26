public class MergeSort {
  public static void main(String[] args) {
    int[] array = {5, 2, 0, 8, 1, 6, -1};
    int[] newArray = mergeSort(array);
    for (int i = 0; i < array.length; i++) {
      System.out.println(newArray[i]);
    }
  }

  public static int[] mergeSort(int[] unsortedArray) {
    int midpoint = unsortedArray.length / 2;
    int[] leftHalf = new int[midpoint];
    int[] rightHalf = new int[unsortedArray.length - midpoint];

    for (int i = 0; i < midpoint; i++) {
      leftHalf[i] = unsortedArray[i];
    }
    for (int i = midpoint, index = 0; i < unsortedArray.length; i++, index++) {
      rightHalf[index] = unsortedArray[i];
    }

    if (leftHalf.length > 1) {
      leftHalf = mergeSort(leftHalf);
    }
    if (rightHalf.length > 1) {
      rightHalf = mergeSort(rightHalf);
    }

    int leftIndex = 0;
    int rightIndex = 0;
    int[] sortedArray = new int[unsortedArray.length];
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
}
