from enum import Enum

class Color(Enum):
    white = 1
    gray = 2
    black = 3

class Node:
    def __init__(self, identifier = None):
        self.neighbors = []
        self.costs = []
        self.id = identifier
        self.parent = None
        self.color = Color.white
        self.weight = float("inf")

    def __str__(self):
        representation = "id " + str(self.id) + "\n"
        for i, j in zip(self.neighbors, self.costs):
            representation += "(" + str(i) + ", " + str(j) + ") "
        return representation

    def add(self, neighbor: int, cost = 1):
        self.neighbors.append(neighbor)
        self.costs.append(cost)

    def __lt__(self, other):
         return (self.weight < other.weight)
    def __le__(self, other):
         return (self.weight <= other.weight)
    def __eq__(self, other):
         return (self.weight == other.weight)
    def __ne__(self, other):
         return (self.weight != other.weight)
    def __gt__(self, other):
         return (self.weight > other.weight)
    def __ge__(self, other):
         return (self.weight >= other.weight)

#A min priority-queue (not necessary)
class Min_Priority_Queue():
    def __init__(self, array = []):
        self.storage = array
        self.build_heap(self.storage)

    def min_heapify(self, index:int):
        """Makes the ith element of a list to respect the min heap property"""

        min_index = index
        left = 2*index+1
        if((left < self.size()) and (self.storage[left] <= self.storage[min_index])):
            min_index = left
        right = 2*index+2
        if((right < self.size()) and (self.storage[right] <= self.storage[min_index])):
            min_index = right
        if(min_index != index):
            aux_bucket = self.storage[index]
            self.storage[index] = self.storage[min_index]
            self.storage[min_index] = aux_bucket

            self.min_heapify(min_index)
        return

    def decrease_key(self, index, key):
        pass
    def add(element):
        pass

    def validate_heap(self)->str:

        for i in range(heap_size//2):
            left = 2*i+1
            right = 2*i+2
            if(left < self.size() and self.storage[i] > self.storage[2*i+1]):
                print("HEAP PROPERTY VIOLATION", self.size(), self.storage)
                break
            if(right < self.size() and self.storage[i] > self.storage[2*i+2]):
                print("HEAP PROPERTY VIOLATION", self.size(), self.storage)
                break
        return "HEAP IS OK"

    def build_heap(self, array:list):
        """Builds a heap of minimum from a list"""

        for i in range(len(array)//2, -1, -1):
            self.min_heapify(i)

    def size(self):
        return len(self.storage)
    def empty(self):
        return bool(self.storage)
