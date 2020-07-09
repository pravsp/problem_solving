"""Delete node solution except tail."""
import __init__
from singlyLinkedList import SinglyLinkedList
from utils.ll_util import LinkedListUtil

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead
        """
        nextnode = node.getNextNode()
        if not nextnode:
            del node
            return

        node.data = nextnode.data
        node.setNextNode(nextnode.getNextNode())

if __name__ == '__main__':
    print('Deleting a node form linked list')
    llist = SinglyLinkedList()
    LinkedListUtil().constructList(llist)
    llist.printList()
    dataToDelete = input("Enter Node data to delete:")
    node = llist.getNode(int(dataToDelete))
    # llist.delNode(int(dataToDelete))
    Solution().deleteNode(node)
    llist.printList()

