public class Student {
  private String name;
  private int grade;
  private int id;

  public Student(String fname, int score, int num) {
    name = fname;
    grade = score;
    id = num;
  }

  public String getName() {
    return name;
  }

  public int getGrade() {
    return grade;
  }

  public int getId() {
    return id;
  }
}
