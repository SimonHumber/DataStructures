#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int value;
  struct node *leftNode;
  struct node *rightNode;
  struct node *parentNode;
  bool isLeaf;
} Node;

typedef struct {
  int size;
  Node *root;
} BinaryTree;

typedef struct q {
  int size;
  Node *nodes[];
} Queue;

Queue *createQ(int size) {
  // Need to allocate memory to Queue and flexible array
  Queue *queue = (Queue *)malloc(sizeof(Queue) + size * sizeof(Node));
  queue->size = 0;
  return queue;
}
void push(Queue *queue, Node *node) {
  int currentIndex = queue->size;
  int prevIndex = queue->size - 1;
  while (prevIndex >= 0) {
    queue->nodes[currentIndex] = queue->nodes[prevIndex];
    currentIndex--;
    prevIndex--;
  }
  queue->nodes[0] = node;
  queue->size++;
}
Node *pop(Queue *queue) {
  Node *output = queue->nodes[queue->size - 1];
  queue->size--;
  return output;
}

BinaryTree *newTree() {
  BinaryTree *tree = malloc(sizeof(BinaryTree));
  tree->root = NULL;
  tree->size = 0;
  return tree;
}

void add(BinaryTree *tree, int value) {
  Node *newNode = (Node *)malloc(sizeof(Node));
  newNode->value = value;
  newNode->isLeaf = true;
  newNode->leftNode = NULL;
  newNode->rightNode = NULL;
  newNode->parentNode = NULL;
  if (tree->size == 0) {
    tree->root = newNode;
  } else {
    Node *currentNode = tree->root;
    while (true) {
      if (value < currentNode->value) {
        if (currentNode->leftNode) {
          currentNode = currentNode->leftNode;
        } else {
          currentNode->leftNode = newNode;
          newNode->parentNode = currentNode;
          break;
        }
      } else {
        if (currentNode->rightNode) {
          currentNode = currentNode->rightNode;
        } else {
          currentNode->rightNode = newNode;
          newNode->parentNode = currentNode;
          break;
        }
      }
    }
  }
  tree->size++;
}

void printBFS(BinaryTree *tree) {
  Queue *queue = createQ(tree->size);
  push(queue, tree->root);
  while (queue->size > 0) {
    Node *currentNode = pop(queue);
    printf("%d ", currentNode->value);
    if (currentNode->leftNode) {
      push(queue, currentNode->leftNode);
    }
    if (currentNode->rightNode) {
      push(queue, currentNode->rightNode);
    }
  }
}

void printDFS(BinaryTree *tree, Node *node) {
  if (node == NULL) {
    node = tree->root;
  }
  printf("%d ", node->value);
  if (node->leftNode) {
    printDFS(tree, node->leftNode);
  }
  if (node->rightNode) {
    printDFS(tree, node->rightNode);
  }
}

int main(int argc, char *argv[]) {
  BinaryTree *tree = newTree();
  add(tree, 5);
  add(tree, 7);
  add(tree, 3);
  add(tree, 6);
  add(tree, 8);
  add(tree, 4);
  add(tree, 1);
  printBFS(tree);
  printf("\n");
  printDFS(tree, NULL);

  return EXIT_SUCCESS;
}
