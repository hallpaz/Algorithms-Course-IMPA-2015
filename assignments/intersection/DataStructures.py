from enum import Enum

class Color(Enum):
    """docstring for Color"""
    Red = 0;
    Black = 1;


class ListNode():
    def __init__(self, payload):
        self.data = payload
        self.next = None
        self.prev = None

class DoublyLinkedList():
    """Doubly linked list class. The nodes are expected to have prev and next fields"""

    def __init__(self, node = None):
        if node is None:
            self.head = None
            self.tail = None
        else:
            node.prev = None
            self.head = node
            self.tail = node

    def insertHead(self, value):
        """This method inserts a node into the head position.
        The node is assumed to be isolated (no prev or next)"""
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insertTail(self, value):
        """This method inserts a node into the tail position.
        The node is assumed to be isolated (no prev or next)"""

        node = ListNode(value)
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


class TreeNode():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self, value = None):
        pass

    def insert(self, value):
        pass

    def remove(self, value):


class RBNode(TreeNode):
    """docstring for RBNode"""
    def __init__(self, value):
        super(RBNode, self).__init__()
        self.color =


class RBTree():
    def __init__(self, arg):
        pass
