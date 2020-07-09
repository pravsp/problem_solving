"""Linked list utils."""
from linkedlist import LinkedList


class LinkedListUtil:
    def constructList(self, llist: LinkedList):
        return self._constructList(llist)
    def _constructList(self, llist: LinkedList, atTail:bool=False):
        """Construct linked list."""
        while True:
            data = input("Enter Node Data (Numeric), others if you are done:")
            if data.isdigit():
                llist.addNode(int(data), addToTail=atTail)
            else:
                return

    def constructListAtTail(self, llist: LinkedList):
        """Construct linked list at tail."""
        return self._constructList(llist, atTail=True)
