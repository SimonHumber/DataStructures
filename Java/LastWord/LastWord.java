public class LastWord {
  public static void main(String[] args) {
    String word = "Hello World";
    System.out.println(lengthOfLastWord(word));
  }

  public static int lengthOfLastWord(String s) {
    String words[] = s.split(" ");
    return words[words.length - 1].length();
  }
}
