"""List node data structure."""


class ListNode:
    def __init__(self, data: int, nextNode:'ListNode'=None):
        self.data = data
        self.nextNode = nextNode

    def setNextNode(self, nextNode:'ListNode'):
        self.nextNode = nextNode

    def getNextNode(self) -> 'ListNode':
        return self.nextNode
