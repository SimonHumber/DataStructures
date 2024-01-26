import java.util.ArrayDeque;

// bracket checker program
class Main {
  public static void main(String[] args) {
    System.out.println(checker("()]}"));
    Student simon = new Student("Simon", 90, 1000);
    System.out.println(simon.getName());
  }

  public static boolean checker(String value) {
    ArrayDeque<String> openarray = new ArrayDeque<>();
    for (int i = 0; i < value.length(); i++) {
      if ('(' == value.charAt(i)) {
        openarray.push("(");
      } else if ('[' == value.charAt(i)) {
        openarray.push("[");
      } else if ('{' == value.charAt(i)) {
        openarray.push("{");
      } else if (openarray.peek() == null) {
        return false;
      } else if (')' == value.charAt(i)) {
        if (openarray.peek().equals("(")) {
          openarray.pop();
        } else {
          return false;
        }
      } else if (']' == value.charAt(i)) {
        if (openarray.peek().equals("[")) {
          openarray.pop();
        } else {
          return false;
        }
      } else if ('}' == value.charAt(i)) {
        if (openarray.peek().equals("{")) {
          openarray.pop();
        } else {
          return false;
        }
      }
    }
    if (openarray.peek() != null) {
      return false;
    } else {
      return true;
    }
  }
}
