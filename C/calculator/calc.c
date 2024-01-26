#include <math.h>
#include <stdio.h>
int main(int argc, char *argv[]) {
  printf("Welcome to the calculator program!\n");
  int num1;
  int num2;
  char operator;
  char option;

  while (1) {
    printf("Please input a number, an operator, and another number\n");
    // no space between inputs
    scanf("%d", &num1);
    scanf("%c", &operator);
    scanf("%d", &num2);
    if (operator== '+') {
      printf("%d\n", num1 + num2);
    } else if (operator== '-') {
      printf("%d\n", num1 - num2);
    } else if (operator== '*') {
      printf("%d\n", num1 * num2);
    } else if (operator== '/') {
      printf("%f\n", (double)num1 / num2);
    } else if (operator== '^') {
      printf("%f\n", pow(num1, num2));
    }
    printf(
        "Calculation completed, would you like to make another calculation?\n");
    // After pressing enter in the previous scanf, the linebreak will transfer
    // to this scanf. Must put space before %c to prevent this scanf from being
    // skipped
    scanf(" %c", &option);
    if (option == 'y') {
      continue;
    } else {
      break;
    }
  }
  return 0;
}
