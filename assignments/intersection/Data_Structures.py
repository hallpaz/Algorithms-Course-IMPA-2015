


class ListNode():
    def __init__(self, payload):
        self.data = payload
        self.next = None
        self.prev = None

class DoublyLinkedList():
    """Doubly linked list class. The nodes are expected to have prev and next fields"""
    
    def __init__(self, node):
        if node is None:
            self.head = None
            self.tail = None
        else:
            node.prev = None
            self.head = node
            self.tail = node

    def insertHead(self, node):
        """This method inserts a node into the head position.
        The node is assumed to be isolated (no prev or next)"""

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insertTail(self, node):
        """This method inserts a node into the tail position.
        The node is assumed to be isolated (no prev or next)"""

        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def successor(self, arg):
        pass

    def anteccesor(self, arg):
        pass
