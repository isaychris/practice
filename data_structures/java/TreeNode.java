public class TreeNode <T extends Comparable<T>> {
    public TreeNode left;
    public TreeNode right;
    public T data;

    public TreeNode() {
        this.left = null;
        this.right = null;
        this.data = null;
    }

    public TreeNode(T data) {
        this.left = null;
        this.right = null;
        this.data = data;
    }
}
