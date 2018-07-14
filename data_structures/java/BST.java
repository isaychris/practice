public class BST<T extends Comparable<T>> {
    public TreeNode<T> root;

    public BST() {
        this.root = null;
    }

    public void insert(TreeNode<T> root, T value) {
        if (this.root == null) {
            this.root = new TreeNode<T>(value);
        } else {
            if (root.data.compareTo(value) < 0) {
                if (root.right == null) {
                    root.right = new TreeNode<T>(value);
                } else {
                    insert(root.right, value);
                }
            } else {
                if (root.left == null) {
                    root.left = new TreeNode<T>(value);
                } else {
                    insert(root.right, value);
                }
            }
        }
    }

    public boolean search(TreeNode<T> root, T value) {
        if (root == null) {
            return false;
        } else if (root.data == value) {
            return true;
        } else if (root.data.compareTo(value) < 0) {
            return search(root.right, value);
        } else if (root.data.compareTo(value) > 0) {
            return search(root.left, value);
        }
        return false;
    }

    public void inorder(TreeNode<T> root) {
        if (root != null) {
            inorder(root.left);
            System.out.println(root.data);
            inorder(root.right);
        }
    }

    public void preorder(TreeNode<T> root) {
        if (root != null) {
            System.out.println(root.data);
            inorder(root.left);
            inorder(root.right);
        }
    }

    public void postorder(TreeNode<T> root) {
        if (root != null) {
            inorder(root.left);
            inorder(root.right);
            System.out.println(root.data);
        }
    }

    public static void main(String[] args) {
        BST<Integer> my_bst = new BST();
        my_bst.insert(my_bst.root, 5);
        my_bst.insert(my_bst.root, 1);
        my_bst.insert(my_bst.root, 7);
        my_bst.inorder(my_bst.root);
        System.out.println(my_bst.search(my_bst.root, 7));
    }
}
