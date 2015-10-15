data_folder = "data/"
images_folder = "images/"


from enum import Enum
from collections import deque

class Color(Enum):
    white = 1
    gray = 2
    black = 3

class Node:
    def __init__(self, identifier = None, adj = [], costs = []):
        self.neighbors = adj
        self.costs = costs
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

def BFS(graph:list, visit_function):
    for node in graph:
        node.color = Color.white
    queue = Queue()
    for node in graph:
        if node.color == Color.white:
            queue.put(node)
        while(not queue.empty()):
            currentNode = queue.get()
            currentNode.color = Color.gray
            visit_function(currentNode)
            for i in currentNode.neighbors:
                if graph[i].color == Color.white:
                    queue.put(graph[i])
            currentNode.color = Color.black

def BFS(graph:list, visit_function):
    """Runs a BFS and compute graph size during the process"""

    for node in graph:
        node.color = Color.white
    queue = deque()
    for node in graph:
        if(node.color == Color.white):
            queue.append(node)
        while(not queue.empty()):
            currentNode = queue.popleft()
            currentNode.color = Color.gray
            visit_function(currentNode)
            for i in currentNode.neighbors:
                if graph[i].color == Color.white:
                    queue.append(graph[i])
            currentNode.color = Color.black
    return size

def graph_size(graph:list)->float:
    """Runs a DFS and compute graph size during the process"""
    size = 0
    for node in graph:
        node.color = Color.white
    stack = []
    stack.append(graph[0])
    graph[0].color = Color.gray
    while(stack):
        currentNode = stack.pop()
        for i in range(len(currentNode.neighbors)):
            neighbor = graph[currentNode.neighbors[i]-1]
            #print(currentNode.id, neighbor.id)
            if graph[neighbor.id-1].color == Color.white:
                stack.append(graph[neighbor.id-1])
                graph[neighbor.id-1].color = Color.gray
                size += currentNode.costs[i]
        currentNode.color = Color.black
    return size


def trimm_isolated(graph:list)->list:
    return [graph[i] for i in range(len(graph)) if graph[i].neighbors ]


def tree_reconstruction(graph:list, last:Node)->list:
    tree = [Node(i) for i in range(1, len(graph)+1)]
    while(last.parent is not None):
        tree[last.id].add(last.parent, last.weight)
        tree[last.parent].add(last.id, last.weight)

    return trimm_isolated(tree)

#Minimum Spanning Tree using Prim's algorithm
def minimum_spanning_tree(graph:list)->list:
    mst = []
    for node in graph:
        node.weight = float("inf")
        node.parent = None

    graph[0].weight = 0
    queue = priority_queue(graph)
    while(not queue.empty):
        node = queue.pop()
        for i in node.neighbors:
            if(graph[i].color == Color.white and node.cost[i] < graph[i].weight):
                graph[i].parent = node
                graph[i].weight = node.cost[i] #change priority
        node.color = Color.black
        last = node
    #tree reconstruction

    mst = tree_reconstruction(graph, last)
    if(len(mst) != len(graph)):
        print("There's been some weird error in MST")

    return mst

#Minimum path finding (from single source) using Djikstra algorithm
def minimum_path(graph:list, source:int, dst = None)->list:
    """Runs a Djikstra algorithm and returns the path subgraph"""

    for node in graph:
        node.color = Color.white
        node.weight = float("inf")
        node.parent = None
    graph[source-1].weight = 0
    queue = Priority_Queue()
    queue.append(graph[source-1]) #graph is numbered from 1 to n
    while(not queue.empty()):
        currentNode = queue.pop()
        currentNode.color = Color.gray

        for i in range(len(currentNode.neighbors)):
            neighbor = graph[currentNode.neighbors[i].id]
            if(graph[neighbor.id-1].weight > currentNode.weight + currentNode.costs[i])
            if graph[i].color == Color.white:
                queue.append(graph[i])
        currentNode.color = Color.black
    return size

    return path

def graph_initialization(filename:str, graph_size:int)->list:
    graph = [Node(i) for i in range(1, graph_size+1)]
    with open(data_folder + filename) as american_file:
        for line in american_file:
            parameters = line.split()
            source = int(parameters[0])
            dst = int(parameters[1])
            cost = int(parameters[2])
            graph[source-1].add(dst, cost)
            graph[dst-1].add(source, cost)
    return graph

if __name__ == "__main__":
    graph = graph_initialization("map.txt", 128)
    print(graph_size(graph))
