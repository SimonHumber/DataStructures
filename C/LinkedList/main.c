#include <stdio.h>
#include <stdlib.h>

struct node {
  int value;
  struct node *nextNode;
};

struct LinkedList {
  struct node *head;
  struct node *tail;
  int size;
};

void createList(struct LinkedList *list) { list->size = 0; }

void prepend(struct LinkedList *list, int value) {
  struct node *newNode = (struct node *)malloc(sizeof(struct node));
  newNode->value = value;
  if (list->size > 0) {
    newNode->nextNode = list->head;
    list->head = newNode;
  } else {
    list->head = newNode;
    list->tail = newNode;
  }
  list->size++;
}

void append(struct LinkedList *list, int value) {
  struct node *newNode = (struct node *)malloc(sizeof(struct node));
  newNode->value = value;
  if (list->size > 0) {
    list->tail->nextNode = newNode;
    list->tail = newNode;
  } else {
    list->tail = newNode;
    list->head = newNode;
  }
  list->size++;
}

struct node *find(struct LinkedList *list, int index) {
  if (index >= list->size) {
    printf("Index out of range!\n");
    return NULL;
  }
  struct node *node = list->head;
  for (int i = 0; i < index; i++) {
    node = node->nextNode;
  }
  return node;
}

// complete this
void delete(struct LinkedList *list, int index) {
  if (index > list->size) {
    printf("Index out of range!\n");
  } else {
    struct node *currentNode = find(list, index);
    if (currentNode == list->head) {
      list->head = list->head->nextNode;
    } else {
      struct node *prevNode = find(list, index - 1);
      prevNode->nextNode = currentNode->nextNode;
      if (currentNode == list->tail) {
        list->tail = prevNode;
      }
    }
    free(currentNode);
    list->size--;
  }
}

void printList(struct LinkedList *list) {
  struct node *currentNode = list->head;
  for (int i = 0; i < list->size; i++) {
    printf("%d ", currentNode->value);
    if (i < list->size - 1) {
      currentNode = currentNode->nextNode;
    }
  }
  printf("\n");
}

int main(int argc, char *argv[]) {
  struct LinkedList *list =
      (struct LinkedList *)malloc(sizeof(struct LinkedList));
  createList(list);
  prepend(list, 5);
  append(list, 6);
  find(list, 0);
  printList(list);
  delete (list, 0);
  append(list, 4);
  printList(list);
  printf("%d\n", find(list, 2)->value);

  return EXIT_SUCCESS;
}
