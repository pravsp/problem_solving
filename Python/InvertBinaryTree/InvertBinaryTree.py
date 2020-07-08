'''Invert a binary tree.'''
from binarytree.binarytree import BinaryTree
# Definition of a Binary tree


if __name__ == '__main__':
    print("Create a binary tree")
    bt = BinaryTree(verbose=True)
    while True:
        data = input("Enter Node Data (Numeric), others if you are done:")
        if data.isdigit():
            bt.addToTree(int(data))
        else:
            break
    bt.printTree()
    print("Height of the tree: ", bt.getHeight())
    bt.root = BinaryTree._balanceBst(bt.root)
    bt.printTree()
