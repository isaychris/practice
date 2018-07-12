class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, node):
        if self.root is None:
            self.root = node

        else:
            if root.data < node.data:
                if root.right is None:
                    root.right = node
                else:
                    return self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    return self.insert(root.left, node)


    def search(self, root, data):
        if root is None:
            return False

        elif root.data == data:
            return True

        elif root.data < data:
            return self.search(root.right, data)

        else:
            return self.search(root.left, data)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.preorder(root.left)
            self.preorder(root.right)
            print(root.data)

my_bst = BST()
my_bst.insert(my_bst.root, Node(5))
my_bst.insert(my_bst.root, Node(1))
my_bst.insert(my_bst.root, Node(7))
my_bst.inorder(my_bst.root)

print(my_bst.search(my_bst.root, 7))