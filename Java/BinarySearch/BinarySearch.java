public class BinarySearch {
  public static void main(String[] args) {
    int[] array = {-1, 1, 2, 3, 4, 5, 6, 7, 8, 10};
    int target = -1;
    System.out.println(binarySearch(array, target));
  }

  public static int binarySearch(int[] array, int target) {
    int targetIndex = array.length / 2;

    while (array[targetIndex] > target) {
      targetIndex /= 2;
    }

    while (array[targetIndex] < target) {
      targetIndex += (array.length - targetIndex) / 2;
    }

    return targetIndex;
  }
}
