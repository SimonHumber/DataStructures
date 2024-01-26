#include <stdio.h>
#include <stdlib.h>

#define MAX 10

struct queue {
  int items[MAX];
  int size;
};
typedef struct queue q;

void createQueue(q *queue) { queue->size = 0; }
void push(q *queue, int item) {
  if (queue->size == MAX) {
    printf("Queue full!\n");
  } else {
    int currentIndex = queue->size;
    int prevIndex = queue->size - 1;
    while (prevIndex >= 0) {
      queue->items[currentIndex] = queue->items[prevIndex];
      currentIndex--;
      prevIndex--;
    }
    queue->items[0] = item;
    queue->size++;
  }
}
void pop(q *queue) {
  if (queue->size == 0) {
    printf("Queue empty!\n");
  } else {
    printf("Popped item: %d\n", queue->items[queue->size - 1]);
    queue->size--;
  }
}
void printQueue(q *queue) {
  for (int i = 0; i < queue->size; i++) {
    printf("%d ", queue->items[i]);
  }
  printf("\n");
}
int main(int argc, char *argv[]) {
  q *queue = (q *)malloc(sizeof(q));
  createQueue(queue);
  push(queue, 5);
  printQueue(queue);
  push(queue, 6);
  printQueue(queue);
  pop(queue);
  printQueue(queue);
  return EXIT_SUCCESS;
}
