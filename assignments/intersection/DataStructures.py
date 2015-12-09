from enum import Enum
from Segment import Segment
from Point2D import Point2D
import random


class Color(Enum):
    """docstring for Color"""
    Red = 0
    Black = 1


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

    def find(self, value):
        currentNode = self.head
        while(currentNode is not None):
            if currentNode.data == value:
                return currentNode
            currentNode = currentNode.next

        return None

    def remove(self, value):
        node = self.find(value)

        if node == self.head:
            self.head = node.next
            if node.next:
                node.next.prev = None
        elif node == self.tail:
            self.tail = node.prev
            if node.prev:
                node.prev.next = None
        else:
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

    def antecessor(self, value):
        node = self.find(value)
        if node is not None:
            return node.prev
        return None


class TreeNode():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

    def insert(self, value):
        if value < self.data:
            if self.left is None:
                node = TreeNode(value)
                self.left = node
                node.parent = self
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                node = TreeNode(value)
                self.right = node
                node.parent = self
            else:
                self.right.insert(value)

    def find(self, value):
        if value == self.data:
            return self

        if value < self.data:
            if self.left is not None:
                return self.left.find(value)
            return None
        else:
            if self.right is not None:
                return self.right.find(value)
            return None


    def printNodes(self, branch):
        if branch is None:
            return
        self.printNodes(branch.left)
        print(branch)
        self.printNodes(branch.right)

    def leftMost(self):
        if self.left is None:
            return self
        return self.left.leftMost()

    def rightMost(self):
        if self.right is None:
            return self
        return self.right.rightMost()

    def successor(self):
        if self.right is not None:
            return self.right.leftMost()

        parent = self.parent
        aux = self
        while parent is not None and aux == parent.right:
            aux = parent
            parent = parent.parent
        return parent

    def antecessor(self):
        if self.left is not None:
            return self.left.rightMost()

        parent = self.parent
        aux = self
        while parent is not None and aux == parent.left:
            aux = parent
            parent = parent.parent
        return parent

    def remove(self, value):
        if self.data == value:
            if (self.left is not None) and (self.right is not None):
                substitute = self.successor()
                if substitute.parent.left == substitute:
                    substitute.parent.left = substitute.right
                else:
                    substitute.parent.right = substitute.right

                if substitute.right is not None:
                    substitute.right.parent = substitute.parent

                substitute.left = self.left
                substitute.right = self.right
                substitute.parent = self.parent

                if substitute.right is not None:
                    substitute.right.parent = substitute
                if substitute.left is not None:
                    substitute.left.parent = substitute

                return substitute

            elif self.left is not None:
                self.left.parent = self.parent
                return self.left
            elif self.right is not None:
                self.right.parent = self.parent
                return self.right
            else:
                return None
        else:
            if value < self.data:
                if self.left is not None:
                    self.left = self.left.remove(value)
            else:
                if self.right is not None:
                    self.right = self.right.remove(value)
        return  self


    def getHeight(self):
        if (self.left is None) and (self.right is None):
            return 0
        elif self.left is not None:
            return self.left.getHeight() + 1
        elif self.right is not None:
            return self.right.getHeight() + 1
        else:
            return max(self.left.getHeight(), self.right.getHeight()) + 1

class BinarySearchTree():
    def __init__(self, value = None):
        self.root = None
        if value is not None:
            self.insert(value)

    def insert(self, value):
        if self.root is not None:
            self.root.insert(value)
        else:
            self.root = TreeNode(value)

    def find(self, value):
        if self.root is not None:
            return self.root.find(value)
        return None

    def successor(self, value):
        node = self.find(value)
        if node is not None:
            return node.successor()
        return None

    def antecessor(self, value):
        node = self.find(value)
        if node is not None:
            return node.antecessor()
        return None

    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)

    def printNodes(self):
        if self.root is not None:
            self.root.printNodes(self.root)

    def getHeight(self):
        if self.root is not None:
            return self.root.getHeight()
        return 0

# def inOrderPrint(self, branch):
#     if(branch is None):
#         return
#
#     self.inOrderPrint(branch.left)
#     print(branch)
#     self.inOrderPrint(branch.right)


class SentinelNIL():
    """docstring for NIL"""
    def __init__(self):
        self.data = 7777777
        self.parent = self
        self.left = self
        self.right = self
        self.color = Color.Black


    def __str__(self):
        return "NIL SENTINEL"

    def __eq__(self, other):
        #if (type(other.data) is type(self.data)):
        if other.data == self.data:
            return True
        return False

    def __ne__(self, other):
        return not (self.__eq__(other))


class RBNode(TreeNode):
    """docstring for RBNode"""
    NIL = SentinelNIL()

    def __init__(self, value):
        self.data = value
        self.parent = RBNode.NIL
        self.left = RBNode.NIL
        self.right = RBNode.NIL
        self.color = Color.Red


    def find(self, value):
        if value == self.data:
            return self

        if value < self.data:
            if self.left != RBNode.NIL:
                return self.left.find(value)
            return None
        else:
            if self.right != RBNode.NIL:
                return self.right.find(value)
            return None

    def printNodes(self, branch):
        if branch == RBNode.NIL:
            return
        self.printNodes(branch.left)
        print(branch)
        self.printNodes(branch.right)

    def successor(self):
        if self.right != RBNode.NIL:
            return self.right.leftMost()

        parent = self.parent
        aux = self
        while parent != RBNode.NIL and aux == parent.right:
            aux = parent
            parent = parent.parent
        if parent == RBNode.NIL:
            parent = None
        return parent

    def antecessor(self):
        if self.left != RBNode.NIL:
            return self.left.rightMost()

        parent = self.parent
        aux = self
        while parent != RBNode.NIL and aux == parent.left:
            aux = parent
            parent = parent.parent
        if parent == RBNode.NIL:
            parent = None
        return parent

    def leftMost(self):
        if self.left == RBNode.NIL:
            return self
        return self.left.leftMost()

    def rightMost(self):
        if self.right == RBNode.NIL:
            return self
        return self.right.rightMost()

    def insert(self, value):
        if value < self.data:
            if self.left == RBNode.NIL:
                node = RBNode(value)
                self.left = node
                node.parent = self
                return node
                #self.insert_fixup(node)
            else:
                return self.left.insert(value)
        else:
            if self.right == RBNode.NIL:
                node = RBNode(value)
                self.right = node
                node.parent = self
                return node
                #self.insert_fixup(node)
            else:
                return self.right.insert(value)

    def getHeight(self):
        if (self.left == RBNode.NIL) and (self.right == RBNode.NIL):
            return 0
        elif self.left != RBNode.NIL:
            return self.left.getHeight() + 1
        elif self.right != RBNode.NIL:
            return self.right.getHeight() + 1
        else:
            return max(self.left.getHeight(), self.right.getHeight()) + 1

class RBTree(BinarySearchTree):
    def __init__(self):
        self.root = RBNode.NIL

    def printNodes(self):
        if self.root != RBNode.NIL:
            self.root.printNodes(self.root)

    def find(self, value):
        if self.root != RBNode.NIL:
            return self.root.find(value)
        return None

    # def insert(self, value):
    #     if self.root != RBNode.NIL:
    #         #print(self.root, self.root == RBNode.NIL, self.root == RBNode.NIL)
    #         inserted_node = self.root.insert(value)
    #         self.insert_fixup(inserted_node)
    #     else:
    #         self.root = RBNode(value)
    #         self.root.color = Color.Black

    def insert(self, value):
        node = RBNode(value)
        y = RBNode.NIL
        x = self.root
        while x != RBNode.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == RBNode.NIL:
            self.root = node
        else:
            if node.data < y.data:
                y.left = node
            else:
                y.right = node
        node.left = RBNode.NIL
        node.right = RBNode.NIL
        node.color = Color.Red
        self.insert_fixup(node)

    def left_rotate(self, pivot):
        y = pivot.right
        pivot.right = y.left

        if y.left != RBNode.NIL:
            y.left.parent = pivot
        y.parent = pivot.parent
        if pivot.parent == RBNode.NIL:
            self.root = y
        elif pivot == pivot.parent.left:
            pivot.parent.left = y
        else:
            pivot.parent.right = y

        y.left = pivot
        pivot.parent = y


    def right_rotate(self, pivot):
        x = pivot.left
        pivot.left = x.right

        if x.right != RBNode.NIL:
            x.right.parent = pivot
        x.parent = pivot.parent
        if pivot.parent == RBNode.NIL:
            self.root = x
        elif pivot.parent.left == pivot:
            pivot.parent.left = x
        else:
            pivot.parent.right = x

        x.right = pivot
        pivot.parent = x


    def insert_fixup(self, z):
        #print("fixing")
        #while  (z != self.root) and (z.parent.color is Color.Red):
        while z.parent.color is Color.Red:
            #print("root", self.root)
            if z.parent == (z.parent).parent.left:
                y = (z.parent).parent.right
                if y.color is Color.Red:
                    z.parent.color = Color.Black
                    y.color = Color.Black
                    (z.parent).parent.color = Color.Red
                    z = (z.parent).parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = Color.Black
                    z.parent.parent.color = Color.Red
                    self.right_rotate(z.parent.parent)
            else:
                y = (z.parent).parent.left
                if y is None:
                    y = RBNode.NIL
                if y.color is Color.Red:
                    z.parent.color = Color.Black
                    y.color = Color.Black
                    (z.parent).parent.color = Color.Red
                    z = (z.parent).parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = Color.Black

                    z.parent.parent.color = Color.Red
                    self.left_rotate(z.parent.parent)
        self.root.color = Color.Black


    def remove(self, value):
        node = self.find(value)
        if node is None:
            return
        #print("to be removed: ", node)
        y = x = RBNode.NIL
        if (node.left == RBNode.NIL) or (node.right == RBNode.NIL):
            y = node
        else:
            y = node.successor()
            if y is None:
                y = RBNode.NIL
        if y.left != RBNode.NIL:
            x = y.left
        else:
            x = y.right

        x.parent = y.parent

        if y.parent == RBNode.NIL:
            self.root = x
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x

        if y != node:
            node.data = y.data
        if y.color is Color.Black:
                self.remove_fixup(x)
        return y

    def remove_fixup(self, x):
        while (x != self.root) and (x.color is Color.Black):
            if x == x.parent.left:
                w = x.parent.right
                if w.color is Color.Red:
                    w.color = Color.Black
                    x.parent.color = Color.Red
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color is Color.Black and w.right.color is Color.Black:
                    w.color = Color.Red
                    x = x.parent
                else:
                    if w.right.color is Color.Black:
                        w.left.color = Color.Black
                        w.color = Color.Red
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.Black
                    w.right.color = Color.Black
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color is Color.Red:
                    w.color = Color.Black
                    x.parent.color = Color.Red
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color is Color.Black and w.left.color is Color.Black:
                    w.color = Color.Red
                    x = x.parent
                else:
                    if w.left.color is Color.Black:
                        w.right.color = Color.Black
                        w.color = Color.Red
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.Black
                    w.left.color = Color.Black
                    self.right_rotate(x.parent)
                    x = self.root
            x.color = Color.Black

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
