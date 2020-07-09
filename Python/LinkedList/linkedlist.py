from abc import ABC, abstractmethod
from listnode import ListNode

class LinkedList(ABC):

    @abstractmethod
    def addNode(self, data: int, addNode: bool):
        pass

    @abstractmethod
    def findNode(self, data: int) -> bool:
        pass

    @abstractmethod
    def getNode(self, data: int) -> ListNode:
        pass

    @abstractmethod
    def delNode(self, data: int) -> bool:
        pass

    @abstractmethod
    def printList(self):
        pass
