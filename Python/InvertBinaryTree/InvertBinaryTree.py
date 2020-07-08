'''Invert a binary tree.'''
from binarytree.binarytree import BinaryTree
from binarytree.treenode import TreeNode
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
    while True:
        data = input("Enter Node Data (Numeric), others if you are done:")
        if data.isdigit():
            bt.addToTree(int(data))
        else:
            break
    bt.printTree(traversal=BinaryTree.LevelOrder, verbose=True)
    bt.printTree(traversal=BinaryTree.InOrder)
    print("Height of the tree: ", bt.getHeight())
    bt.printTree(traversal=BinaryTree.LevelOrder, verbose=True)
    bt.root = Solution().invertTree(bt.root)
    bt.printTree(traversal=BinaryTree.InOrder)
