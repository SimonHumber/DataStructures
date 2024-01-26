#include <stdio.h>
int main(int argc, char *argv[]) {
  int num = 1;
  while (num <= 15) {
    if (num % 3 == 0 && num % 5 == 0) {
      printf("FizzBuzz\n");
    } else if (num % 3 == 0) {
      printf("Fizz\n");
    } else if (num % 5 == 0) {
      printf("Buzz\n");
    } else {
      printf("%d\n", num);
    }
    num += 1;
  }
}
