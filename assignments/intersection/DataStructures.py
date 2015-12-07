from enum import Enum
from Segment import Segment
from Point2D import Point2D
import random


class Color(Enum):
    """docstring for Color"""
    Red = 0;
    Black = 1;


class ListNode():
    def __init__(self, payload):
        self.data = payload
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

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

    def find(self, value)->ListNode:
        currentNode = self.head
        while(currentNode is not None):
            if currentNode.data == value:
                return currentNode
            currentNode = currentNode.next

        return None

    def remove(self, value):
        node = self.find(value)
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None

    def printNodes(self):
        if self.head is None:
            return

        aux = self.head
        while aux is not None:
            print(aux)
            aux = aux.next

    def printNodesReverse(self):
        if self.tail is None:
            return

        aux = self.tail
        while aux is not None:
            print(aux)
            aux = aux.prev

class OrderedDoublyLinkedList(DoublyLinkedList):

    def insert(self, value):
        node = ListNode(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        elif value < self.head.data:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return
        elif self.tail.data < value:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            return
        else:
            aux = self.head.next
            while aux.data < value:
                aux = aux.next
            node.next = aux
            node.prev = aux.prev
            aux.prev.next = node
            aux.prev = node

    def successor(self, value):
        node = self.find(value)
        if node is not None:
            return node.next
        return None

    def antecesor(self, value):
        node = self.find(value)
        if node is not None:
            return node.prev
        return None


class TreeNode():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree():
    def __init__(self, value = None):
        if value is not None:
            node = TreeNode(value)
            self.root = node
        else:
            self.root = None

    def insert(self, value, branch = None):
        branch = branch or self.root
        if self.root is None:
            node = TreeNode(value)
            self.root = node
        else:
            if value < branch.data:
                if branch.left is None:
                    node = TreeNode(value)
                    branch.left = node
                else:
                    self.insert(value, branch.left)
            else:
                if branch.right is None:
                    node = TreeNode(value)
                    branch.right = node
                else:
                    self.insert(value, branch.right)

    def inOrderPrint(self, branch):
        if(branch is None):
            return

        self.inOrderPrint(branch.left)
        print(branch)
        self.inOrderPrint(branch.right)


    def leftMost(self, node):
        if node.left is None:
            return node
        return self.leftMost(node.left)

    def rightMost(self, node):
        if node.right is None:
            return node
        return self.rightMost(node.right)

    def find(self, value, branch):
        if self.root is None:
            return None
        if branch.data == value:
            return branch
        if value < branch.data:
            return self.find(value, branch.left)
        else:
            return self.find(value, branch.right)

    def remove(self, value, branch = None):
        if branch is None:
            branch = self.root

        parent = branch
        fromLeft = True

        while(branch.data != value):
            if value < branch.data:
                parent = branch
                branch = branch.left
                fromLeft = True
            else:
                parent = branch
                branch = branch.right
                fromLeft = False

        if branch.left and branch.right:
            node = self.leftMost(branch.right)
            self.remove(node.data, branch.right)
            branch.data = node.data
        elif branch.left:
            if fromLeft:
                parent.left = branch.left
            else:
                parent.right = branch.left
        elif branch.right:
            if fromLeft:
                parent.left = branch.right
            else:
                parent.right = branch.right
        else:
            if fromLeft:
                parent.left = None
            else:
                parent.right = None

    def successor(self, value)->TreeNode:
        node = self.find(value, self.root)
        if node.right is None:
            return None
        return self.leftMost(node.right)

    def antecesor(self, value)->TreeNode:
        node = self.find(value, self.root)
        if node.left is None:
            return None
        return self.rightMost(node.left)

class RBNode(TreeNode):
    """docstring for RBNode"""
    def __init__(self, value):
        super(RBNode, self).__init__()
        self.color = Color.Red


class RBTree():
    def __init__(self, arg):
        pass


if __name__ == '__main__':

    myList = OrderedDoublyLinkedList()
    myTree = BinarySearchTree()

    # for i in range(10):
    #     n = random.randint(0, 100)
    #     myList.insert(n)
    #     myTree.insert(n)
    #
    # myList.printNodes()
    # print("------------------------------------")
    # myList.printNodesReverse()
    # print("------------------------------------")
    # myTree.inOrderPrint(myTree.root)

    a = Segment(Point2D(0, 5), Point2D(4,4), "a")
    b = Segment(Point2D(1,0), Point2D(11, 6), "b")
    c = Segment(Point2D(2,2), Point2D(6, 4), "c")
    d = Segment(Point2D(3,5), Point2D(10, 3), "d")
    e = Segment(Point2D(5,6), Point2D(9, 4), "e")
    f = Segment(Point2D(7,2), Point2D(8, 1), "f")
    segments = [a, b, c, d, e, f]
    for seg in segments:
        myTree.insert(seg)
        myTree.inOrderPrint(myTree.root)
        print("---------------------------------")
