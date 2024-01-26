public class BinaryTree {
  public static void main(String[] args) {
    Tree tree = new Tree();
    tree.insert(5);
    tree.insert(4);
    tree.insert(6);
    tree.insert(3);

    System.out.println(tree.dfs());
    System.out.println(tree.bfs());
  }
}
