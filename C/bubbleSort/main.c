#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int array[], int length) {
  int temp;
  for (int i = 0; i < length; i++) {
    for (int j = 0; j < length; j++) {
      if (array[j] > array[i]) {
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }
}
int main(int argc, char *argv[]) {

  int array[] = {3, 6, 2, 0, 9};
  int length = sizeof(array) / sizeof(array[0]);

  bubbleSort(array, length);
  for (int i = 0; i < length; i++) {
    printf("%d ", array[i]);
  }

  return EXIT_SUCCESS;
}
