"""Singly Linked-List operations."""
from linkedlist import LinkedList
from listnode import ListNode


class SinglyLinkedList(LinkedList):
    def __init__(self):
        self.head = None

    def _addToTail(self, node:ListNode):
        """Add node to tail."""
        if not self.head:
            self.head = node
            return

        parent = self.head
        while parent.nextNode:
            parent = parent.nextNode

        node.setNextNode(parent.getNextNode())
        parent.setNextNode(node)

    def addNode(self, data: int, addToTail:bool=False):
        """Add new node to the SinglyLinked List.

        :param int data: data to be stored in linked list
        :param bool addToTail: Indicate whether data to be added at tail
        """
        if self.findNode(data):
            raise Exception("Duplicate Data")
        node = ListNode(data)
        if addToTail:
            return self._addToTail(node)
        node.setNextNode(self.head)
        self.head = node

    def findNode(self, data: int) -> bool:
        """Find the node available in linked list."""
        node = self._findAndGetNode(data)

        return True if node else False

    def _findAndGetNode(self, data: int) -> ListNode:
        """Find and get the node corresponding to data."""
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.getNextNode()
        return None

    def getNode(self, data: int) -> ListNode:
        """Get the node corresponding to the data."""
        return self._findAndGetNode(data)

    def delNode(self, data: int) -> bool:
        """Delete the list node with the data."""
        parent = self.head
        node = parent.getNextNode()
        if parent.data == data:
            self.head = node
            del parent
            return True
        while node:
            if node.data == data:
                parent.setNextNode(node.getNextNode())
                del node 
                return True
            parent = node
            node = node.getNextNode()
        return False

    def printList(self):
        """Print the Singly Linked List."""
        list_str = ''
        if not self.head:
            print("Empty Linked List!!!")
            return
        list_str = str(self.head.data)
        node = self.head.getNextNode()
        while node:
            list_str = list_str + '->' + str(node.data)
            node = node.getNextNode()

        print(list_str)

