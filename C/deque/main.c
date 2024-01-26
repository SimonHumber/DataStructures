#include <stdio.h>
#include <stdlib.h>

#define MAX 10

struct deque {
  int items[MAX];
  int size;
};

typedef struct deque dq;

void createDeque(dq *deque) { deque->size = 0; }

void append(dq *deque, int item) {
  if (deque->size == MAX) {
    printf("Deque full!\n");
  } else {
    deque->items[deque->size] = item;
    deque->size++;
  }
}

void prepend(dq *deque, int item) {
  if (deque->size == MAX) {
    printf("Deque full!\n");
  } else {
    int currentItem = deque->size;
    int prevItem = deque->size - 1;
    for (int i = 0; i < deque->size; i++) {
      deque->items[currentItem] = deque->items[prevItem];
      currentItem--;
      prevItem--;
    }
    deque->items[0] = item;
    deque->size++;
  }
}

void removeLast(dq *deque) {
  if (deque->size == 0) {
    printf("Deque empty!\n");
  } else {
    printf("Removed item is: %d\n", deque->items[deque->size - 1]);
    deque->size--;
  }
}
void removeFirst(dq *deque) {
  if (deque->size == 0) {
    printf("Deque empty!\n");
  } else {
    printf("Removed item is: %d\n", deque->items[0]);
    for (int i = 1; i < deque->size; i++) {
      deque->items[i - 1] = deque->items[i];
    }
    deque->size--;
  }
}

void printDeque(dq *deque) {
  for (int i = 0; i < deque->size; i++) {
    printf("%d ", deque->items[i]);
  }
  printf("\n");
}

int main(int argc, char *argv[]) {
  dq *deque = (dq *)malloc(sizeof(dq));
  prepend(deque, 5);
  printDeque(deque);
  append(deque, 6);
  printDeque(deque);
  prepend(deque, 4);
  printDeque(deque);
  removeLast(deque);
  removeFirst(deque);
  printDeque(deque);
  append(deque, 100);
  printDeque(deque);

  return EXIT_SUCCESS;
}
