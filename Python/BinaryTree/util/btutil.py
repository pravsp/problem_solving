"""Binary Tree util."""
from binarytree import BinaryTree


class BinaryTreeUtil:
    def constructBinaryTree(self, btree: BinaryTree):
        """Construct the binary tree based on user input.
        :param btree: Binary tree on which new nodes to be added
        :type btree: BinaryTree
        """
        while True:
            data = input("Enter Node Data (Numeric), others if you are done:")
            if data.isdigit():
                btree.addToTree(int(data))
            else:
                return

