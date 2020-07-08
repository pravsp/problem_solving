'''Invert a binary tree.'''
import __init__
from binarytree import BinaryTree
from treenode import TreeNode
from util.btutil import BinaryTreeUtil
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Invert:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            right = root.right
            left = root.left
            root.right = self.invertTree(left)
            root.left = self.invertTree(right)
        return root

if __name__ == '__main__':
    print("Create a binary tree")
    bt = BinaryTree()
    btutil = BinaryTreeUtil()
    btutil.constructBinaryTree(bt)
    bt.printTree(traversal=BinaryTree.LevelOrder, verbose=True)
    bt.printTree(traversal=BinaryTree.InOrder)
    print("Height of the tree: ", bt.getHeight())
    bt.printTree(traversal=BinaryTree.LevelOrder, verbose=True)
    bt.root = Invert().invertTree(bt.root)
    bt.printTree(traversal=BinaryTree.InOrder)
