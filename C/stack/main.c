#include <stdio.h>
#include <stdlib.h>

#define MAX 10
struct stack {
  int items[MAX];
  int size;
};
typedef struct stack st;

void createStack(st *stack) { stack->size = 0; }

void push(st *stack, int item) {
  if (stack->size == 10) {
    printf("Stack full!\n");
  } else {
    stack->items[stack->size] = item;
    stack->size++;
  }
}
void pop(st *stack) {
  if (stack->size == 0) {
    printf("Stack empty!\n");
  } else {
    printf("Popped item: %d\n", stack->items[stack->size - 1]);
    stack->size--;
  }
}
void printStack(st *stack) {
  for (int i = 0; i < stack->size; i++) {
    printf("%d ", stack->items[i]);
  }
  printf("\n");
}

int main(int argc, char *argv[]) {
  st *stack = (st *)malloc(sizeof(st));
  createStack(stack);
  push(stack, 3);
  push(stack, 4);
  pop(stack);
  printStack(stack);

  return EXIT_SUCCESS;
}
