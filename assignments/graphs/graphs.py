data_folder = "data/"
images_folder = "images/"

from collections import deque
#from data_structures import Min_Priority_Queue as priority_queue
from copy import deepcopy
import heapq
from data_structures import Node, Color


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

def graph_size(graph:list, source = None)->float:
    """Runs a DFS and compute graph size during the process"""
    size = 0
    if source is None:
        source = 1

    for node in graph:
        node.color = Color.white
    stack = []
    stack.append(graph[source-1])
    graph[source-1].color = Color.gray
    while(stack):
        currentNode = stack.pop()
        #print(currentNode.id, currentNode.parent)
        for i in range(len(currentNode.neighbors)):
            neighbor = graph[currentNode.neighbors[i]-1]
            #print(currentNode.id, neighbor.id)
            size += currentNode.costs[i]
            if graph[neighbor.id-1].color == Color.white:
                stack.append(graph[neighbor.id-1])
                graph[neighbor.id-1].color = Color.gray
                #print(neighbor.id, currentNode.costs[i], size)
        currentNode.color = Color.black
    return size/2



def mst_reconstruction(graph:list)->list:
    """Returns the root and the data storage of the tree"""

    tree = [Node(i) for i in range(1, len(graph)+1)]
    for i in range(len(graph)):
        if(graph[i].parent):
            node = graph[i]
            origin = node.parent
            tree[i].parent = origin
            tree[i].weight = node.weight
            tree[i].add(origin, node.weight)
            tree[origin-1].add(node.id, node.weight)
        elif(graph[i].weight < 1):
            root = graph[i]
            tree[i].weight = 0
    return root.id, tree

def minpath_reconstruction(graph:list, dst = None)->list:
    tree = [Node(i) for i in range(1, len(graph)+1)]
    root = dst
    if dst is not None:
        last = dst
        while(graph[last-1].parent is not None):
            node = graph[last-1]
            origin = node.parent
            edge_cost = node.weight - graph[origin-1].weight
            tree[last-1].parent = origin
            tree[last-1].weight = node.weight
            tree[last-1].add(origin, edge_cost)
            tree[origin-1].add(node.id, edge_cost)
            last = origin
        if graph[last-1].weight < 1:
            root = graph[last-1]
            tree[last-1].weight = 0
    else:
        for i in range(len(graph)):
            if(graph[i].parent is not None):
                node = graph[i]
                origin = node.parent
                edge_cost = node.weight - graph[origin-1].weight
                tree[i].parent = origin
                tree[i].weight = node.weight
                tree[i].add(origin, edge_cost)
                tree[origin-1].add(node.id, edge_cost)
            elif(graph[i].weight < 1):
                root = graph[i]
                tree[i].weight = 0
    return root.id, tree

def minimum_spanning_tree(graph:list)->list:
    mst = [Node(i) for i in range(1, len(graph)+1)]
    for node in graph:
        node.weight = float("inf")
        node.parent = None

    graph[0].weight = 0
    last = graph[0]
    queue = [graph[i] for i in range(len(graph))]
    heapq.heapify(queue)
    on_queue = [True for i in range(len(graph))]
    while(queue):
        node = heapq.heappop(queue)
        #print(node.id)
        if on_queue[node.id-1]:
            #if node.color == Color.white #
            for i in range(len(node.neighbors)):
                neighbor = graph[node.neighbors[i]-1]
                #print("neigh", neighbor.id)
                #neighbor = mst[node.neighbors[i]-1]
                if(on_queue[neighbor.id-1] and (node.costs[i] < neighbor.weight)):
                    #print("neigh", neighbor.id)
                    neighbor.parent = node.id
                    neighbor.weight = node.costs[i]

                heapq.heapify(queue)
            on_queue[node.id-1] = False
            #print(node.id, node.parent, node.weight)
            mst[node.id-1] = node
            last = node

    root, mst = mst_reconstruction(mst)
    if(len(mst) != len(graph)):
        print("There's been some weird error in MST")
    #for node in mst:
    #    print(node, node.parent, node.weight)

    return root, mst

#Minimum path finding (from single source) using Djikstra algorithm
def minimum_path(graph:list, source:int, dst = None)->list:
    """Runs a Djikstra algorithm and returns the path subgraph"""
    min_tree = [Node(i) for i in range(len(graph))]
    for node in graph:
        node.weight = float("inf")
        node.parent = None
    graph[source-1].weight = 0
    queue = [graph[i] for i in range(len(graph))]
    heapq.heapify(queue)
    while(queue):
        currentNode = heapq.heappop(queue)
        #currentNode.color = Color.gray
        min_tree[currentNode.id-1] = currentNode
        if dst is not None:
            if(currentNode.id == dst):
                break
        for i in range(len(currentNode.neighbors)):
            neighbor = graph[currentNode.neighbors[i]-1]
            if neighbor.weight > (currentNode.weight + currentNode.costs[i]):
                neighbor.weight = currentNode.weight + currentNode.costs[i]
                neighbor.parent = currentNode.id
        heapq.heapify(queue)

    root = source
    if dst is not None:
        root, min_tree = minpath_reconstruction(min_tree, dst)
    else:
        root, min_tree = minpath_reconstruction(min_tree)
    # for node in min_tree:
    #     edge_cost = 0
    #     if(node.parent is not None):
    #         edge_cost = node.weight - min_tree[node.parent-1].weight
    #     print(node.id, node.parent, edge_cost, node.weight)

    return root, min_tree

def graph_initialization(filename:str, graph_size:int)->list:
    graph = [Node(i) for i in range(1, graph_size+1)]
    #for node in graph:
    #    print(node)
    with open(data_folder + filename) as american_file:
        file_lines = american_file.readlines()
        for line in file_lines:
            #print('UMA LINHA')
            parameters = line.split()
            source = int(parameters[0])
            dst = int(parameters[1])
            cost = float(parameters[2])
            #print(source, dst, cost)
            #print(graph[source-1])
            graph[source-1].add(dst, cost) #add undirected
            graph[dst-1].add(source, cost)
            #print(graph[source-1])
    return graph

if __name__ == "__main__":
    graph = graph_initialization("map.txt", 128)
    print("Total graph size", graph_size(graph))
    root, mst = minimum_spanning_tree(graph)
    print("mst size", graph_size(mst, root) )
    root, path = minimum_path(graph, 93, 112)
    print("min tree size", graph_size(path, root))
    print(root)
