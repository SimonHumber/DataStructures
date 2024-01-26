import java.util.ArrayDeque;

// hot potato program
public class Potato {
  public static void main(String[] args) {
    String[] kids = {"Brad", "Kent", "Jane", "Susan", "David", "Bill"};
    System.out.println(potato(kids, 5));
  }

  public static String potato(String[] kids, int limit) {
    int x = 0;
    ArrayDeque<String> potato = new ArrayDeque<>();
    int counter = kids.length;
    for (int index = 0; index < kids.length; index++) {
      potato.addLast(kids[index]);
    }
    System.out.println(potato);
    while (counter > 1) {
      x += 1;
      if (x < limit) {
        String changepotato = potato.peekLast();
        potato.addFirst(potato.removeLast());
      } else {
        System.out.println(potato);
        potato.removeLast();
        x = 0;
        counter -= 1;
      }
    }
    return potato.peekFirst();
  }
}
