import __init__
from singlyLinkedList import SinglyLinkedList
from utils.ll_util import LinkedListUtil


if __name__ == '__main__':
    print('Deleting a node form linked list')
    llist = SinglyLinkedList()
    LinkedListUtil().constructList(llist)
    llist.printList()
    dataToDelete = input("Enter Node data tp delete:")
    llist.delNode(int(dataToDelete))
    llist.printList()

