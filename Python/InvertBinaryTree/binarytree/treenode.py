'''Definition of a binary tree node.'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def setRight(self, rightNode):
        self.right = rightNode

    def setLeft(self, leftNode):
        self.left = leftNode

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left
