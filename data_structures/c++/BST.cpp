#include <iostream>

template <class T>
class TreeNode
{
public:
	TreeNode<T> * left;
	TreeNode<T> * right;
	T data;

	TreeNode()
	{
		left = nullptr;
		right = nullptr;
		data {};
	}

	TreeNode(T value)
	{
		left = nullptr;
		right = nullptr;
		data = value;
	}
};

template <class T>
class BST
{
public:
	TreeNode<T> * root;

	BST()
	{
		root = nullptr;
	}

	 void insert(TreeNode<T> * root, T value) 
	{
        if (this->root == nullptr) {
            this->root = new TreeNode<T>(value);
        } else {
            if (root->data < value) {
                if (root->right == nullptr) {
                    root->right = new TreeNode<T>(value);
                } else {
                    insert(root->right, value);
                }
            } else {
                if (root->left == nullptr) {
                    root->left = new TreeNode<T>(value);
                } else {
                    insert(root->right, value);
                }
            }
        }
    }

	 bool search(TreeNode<T> * root, T value) {
		 if (root == nullptr) {
			 return false;
		 }
		 if (root->data == value) {
			 return true;
		 }
		 if (root->data < value) {
			 return search(root->right, value);
		 }
		 if (root->data > value) {
			 return search(root->left, value);
		 }
		 return false;
	 }

	 void inorder(TreeNode<T> * root) {
		 if (root != nullptr) {
			 inorder(root->left);
			 std::cout << root->data << std::endl;
			 inorder(root->right);
		 }
	 }
};

int main()
{
	BST<int> my_bst;
	my_bst.insert(my_bst.root, 5);
	my_bst.insert(my_bst.root, 1);
	my_bst.insert(my_bst.root, 7);
	my_bst.inorder(my_bst.root);
	std::cout << my_bst.search(my_bst.root, 7) << std::endl;

}