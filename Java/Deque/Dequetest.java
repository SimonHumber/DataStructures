import java.util.ArrayDeque;
import java.util.Arrays;

public class Dequetest {
  public static void main(String[] args) {
    int[] numbers = {121};
    System.out.println(palindrome(numbers));
  }

  public static boolean palindrome(int[] numbers) {
    ArrayDeque deque = new ArrayDeque<>();
    deque.addAll(Arrays.asList(numbers));
    while (deque.size() > 1) {
      if (deque.removeFirst() == deque.removeLast()) {
        continue;
      } else {
        return false;
      }
    }
    return true;
  }
}
