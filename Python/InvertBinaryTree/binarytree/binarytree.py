"""Binary tree operation."""
from .treenode import TreeNode


class BinaryTree:
    PreOrder = "preorder-traversal"
    PostOrder = "postorder-traversal"
    InOrder = "inorder-traversal"
    LevelOrder = "levelorder-traversal"

    def __init__(self, verbose=False):
        '''Create an Binary Tree instance.'''
        self.root = None
        self.verbose = verbose
        self.traverse = dict()
        self.traverse[self.PreOrder] = BinaryTree._preOrderTraversal
        self.traverse[self.PostOrder] = BinaryTree._postOrderTraversal
        self.traverse[self.InOrder] = BinaryTree._inOrderTraversal
        self.traverse[self.LevelOrder] = BinaryTree._levelOrderTraversal

    @staticmethod
    def _preOrderTraversal(root_node, traversal_l, internal=False):
        """Print node in preorder traversal format.

        :param root_node: Root node to traverse
        :type root_node: binarytree.treenode.TreeNode
        :param list traversal_l: Data to be collected in traversal list
        """
        if not root_node:
            return
        if internal:
            trav_data = dict()
            trav_data['data'] = root_node.val
            trav_data['lheight'] = BinaryTree._heightBst(root_node.left)
            trav_data['rheight'] = BinaryTree._heightBst(root_node.right)
            traversal_l.append(trav_data)
        else:
            traversal_l.append(root_node.val)
        BinaryTree._preOrderTraversal(root_node.left, traversal_l, internal)
        BinaryTree._preOrderTraversal(root_node.right, traversal_l, internal)

    @staticmethod
    def _postOrderTraversal(root_node, traversal_l, internal=False):
        """Print node in postorder traversal format.

        :param root_node: Root node to traverse
        :type root_node: binarytree.treenode.TreeNode
        :param list traversal_l: Data to be collected in traversal list
        """
        if not root_node:
            return
        BinaryTree._postOrderTraversal(root_node.left, traversal_l, internal)
        BinaryTree._postOrderTraversal(root_node.right, traversal_l, internal)
        if internal:
            trav_data = dict()
            trav_data['data'] = root_node.val
            trav_data['lheight'] = BinaryTree._heightBst(root_node.left)
            trav_data['rheight'] = BinaryTree._heightBst(root_node.right)
            traversal_l.append(trav_data)
        else:
            traversal_l.append(root_node.val)

    @staticmethod
    def _inOrderTraversal(root_node, traversal_l, internal=False):
        """Print node in inorder traversal format.

        :param root_node: Root node to traverse
        :type root_node: binarytree.treenode.TreeNode
        :param list traversal_l: Data to be collected in traversal list
        """
        if not root_node:
            return
        BinaryTree._inOrderTraversal(root_node.left, traversal_l, internal)
        if internal:
            trav_data = dict()
            trav_data['data'] = root_node.val
            trav_data['lheight'] = BinaryTree._heightBst(root_node.left)
            trav_data['rheight'] = BinaryTree._heightBst(root_node.right)
            traversal_l.append(trav_data)
        else:
            traversal_l.append(root_node.val)
        BinaryTree._inOrderTraversal(root_node.right, traversal_l, internal)

    @staticmethod
    def _left_rotation(parent_node):
        """Do a left rotation on given parent node.

        Example of left rotation (Height of left 3 and height of right 1)
                           5
                          / \
                         /   \
         (parent_node)  4     7
                       /
                      3
                     /
                    2
        End result
                           5
                          / \
                         /   \
         (return_node)  3     7
                       / \
                      2   4
        :param parent_node: parent node on which rotation has to be performed
        :type parent_node: binarytree.treenode.TreeNode
        :return rotated parent node
        :rtype: binarytree.treenode.TreeNode
        """
        if not parent_node:
            raise Exception("Invalid parent node")
        left_node = parent_node.left
        parent_node.left = left_node.right
        left_node.right = parent_node
        return left_node

    @staticmethod
    def _right_rotation(parent_node):
        """Do a right rotation on given parent node.

        Example of right rotation (Height of left 3 and height of right 1)
                           5
                          / \
                         /   \
         (parent_node)  2     7
                         \
                          3
                           \
                            4
        End result
                           5
                          / \
                         /   \
         (return node)  3     7
                       / \
                      2   4

        :param parent_node: parent node on which rotation has to be performed
        :type parent_node: binarytree.treenode.TreeNode
        :return rotated parent node
        :rtype: binarytree.treenode.TreeNode
        """
        if not parent_node:
            raise Exception("Invalid parent node")
        right_node = parent_node.right
        parent_node.right = right_node.left
        right_node.left = parent_node
        return right_node

    @staticmethod
    def _right_left_rotation(parent_node):
        """Do a left right rotation on given parent node.

        Example of left right rotation (Height of left 3 and height of right 1)
                           5
                          / \
                         /   \
         (parent_node)  2     7
                         \
                          4
                         /
                        3
        After First rotation
                           5
                          / \
                         /   \
         (return node)  2     7
                         \
                          3
                           \
                            4

        End result
                           5
                          / \
                         /   \
         (return node)  3     7
                       / \
                      2   4

        :param parent_node: parent node on which rotation has to be performed
        :type parent_node: binarytree.treenode.TreeNode
        :return rotated parent node
        :rtype: binarytree.treenode.TreeNode
        """
        right_node = parent_node.right
        parent_node.right = BinaryTree._left_rotation(right_node)
        return BinaryTree._right_rotation(parent_node)

    @staticmethod
    def _left_right_rotation(parent_node):
        """Do a left right rotation on given parent node.

        Example of left right rotation (Height of left 3 and height of right 1)
                           5
                          / \
                         /   \
         (parent_node)  4     7
                       /
                      2
                       \
                        3
        After First rotation
                           5
                          / \
                         /   \
         (return node)  4     7
                       /
                      3
                     /
                    2

        End result
                           5
                          / \
                         /   \
         (return node)  3     7
                       / \
                      2   4

        :param parent_node: parent node on which rotation has to be performed
        :type parent_node: binarytree.treenode.TreeNode
        :return rotated parent node
        :rtype: binarytree.treenode.TreeNode
        """
        left_node = parent_node.left
        parent_node.left = BinaryTree._right_rotation(left_node)
        return BinaryTree._left_rotation(parent_node)

    @staticmethod
    def _levelOrderTraversal(root_node, traversal_l, internal=False):
        """Print node in inorder traversal format.

        :param root_node: Root node to traverse
        :type root_node: binarytree.treenode.TreeNode
        :param list traversal_l: Data to be collected in traversal list
        """
        level_que = list()
        level = 0
        level_que.append({'node': root_node, 'level': level})
        while len(level_que) > 0:
            level_node = level_que.pop(0)
            node = level_node['node']
            level = level_node['level']
            if internal:
                trav_data = dict()
                trav_data['data'] = node.val
                trav_data['lheight'] = BinaryTree._heightBst(node.left)
                trav_data['rheight'] = BinaryTree._heightBst(node.right)
                trav_data['level'] = level
                traversal_l.append(trav_data)
            else:
                traversal_l.append(node.val)
            if node.left:
                level_que.append({'node': node.left, 'level': level + 1})

            if node.right:
                level_que.append({'node': node.right, 'level': level + 1})

    def printTree(self, traversal=LevelOrder):
        """ Print the contents of the tree.

        :params enum traversal: Traversal order for the tree
        """
        if traversal not in [BinaryTree.PreOrder, BinaryTree.PostOrder,
                             BinaryTree.InOrder, BinaryTree.LevelOrder]:
            traversal = BinaryTree.LevelOrder   # Default traversal order

        traversal_l = list()
        self.traverse[traversal](self.root, traversal_l, internal=self.verbose)
        from pprint import pformat
        print(pformat(traversal_l))

    @staticmethod
    def _findData(root_node, data):
        """Find data in binady tree.

        :param root_node: Root node to traverse
        :type root_node: binarytree.treenode.TreeNode
        :param int data: data to be added to new node
        :return boolean: True if data exists else False
        :rtype bool
        """
        if not root_node:
            return False

        if root_node.val == data:
            return True

        if not BinaryTree._findData(root_node.left, data):
            return BinaryTree._findData(root_node.right, data)

    def existsInTree(self, data):
        """Check if data exists in tree.

        :param int data: data to be added to new node
        :return boolean: True if data exists else False
        :rtype bool
        """
        return self._findData(self.root, data)

    def addToTree(self, data):
        """Add data to the tree.

        :param int data: data to be added to new node
        """
        if self._findData(self.root, data):
            raise Exception("Data already exists")

        node = TreeNode(data)
        tmp_node = self.root
        parent_node = None
        while tmp_node:
            parent_node = tmp_node
            if data < tmp_node.val:
                tmp_node = tmp_node.left
            else:
                tmp_node = tmp_node.right

        if not parent_node:
            self.root = node
        else:
            if parent_node.val > data:
                parent_node.setLeft(node)
            else:
                parent_node.setRight(node)

    @staticmethod
    def _getBalanceFactor(parent_node):
        """Get balance factor of parent node.

        :param parent_node: Node to which balance factor is retrieved
        :type parent_node: binarytree.treenode.TreeNode
        :return balance factor of parent node
        :rtype: int
        """
        l_height = BinaryTree._heightBst(parent_node.left)
        r_height = BinaryTree._heightBst(parent_node.right)
        return l_height - r_height

    @staticmethod
    def _balanceBst(balance_node):
        if not balance_node:
            return balance_node
        balance_node.left = BinaryTree._balanceBst(balance_node.left)
        balance_node.right = BinaryTree._balanceBst(balance_node.right)
        balance_factor = BinaryTree._getBalanceFactor(balance_node)
        if balance_factor not in [-1, 0, 1]:
            # Rotation needed
            if balance_factor < 0:
                # Right subtree needs to be balanced
                bf_r = BinaryTree._getBalanceFactor(balance_node.right)
                if bf_r < 0:
                    # left rotation need to be performed
                    return BinaryTree._left_rotation(balance_node)
                else:
                    # right left rotation
                    return BinaryTree._right_left_rotation(balance_node)
            else:
                # Left subtree needs to be balanced
                bf_l = BinaryTree._getBalanceFactor(balance_node)
                if bf_l > 0:
                    # right rotation need to be performed
                    return BinaryTree._right_rotation(balance_node)
                else:
                    # left right rotation need to be performed
                    return BinaryTree._left_right_rotation(balance_node)
        return balance_node

    def getHeight(self):
        """Get the height of this binary tree."""
        return BinaryTree._heightBst(self.root)

    @staticmethod
    def _heightBst(root_node):
        """Get the height of the binary tree.

        :param root_node: root node of the binary tree
        :type root_node: binarytree.treenode.TreeNode
        :return height of the binary tree
        :rtype int
        """
        if not root_node:
            return 0

        height = max(BinaryTree._heightBst(root_node.left),
                     BinaryTree._heightBst(root_node.right))
        height = height + 1
        return height

