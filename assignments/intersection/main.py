from copy import deepcopy
from DataStructures import BinarySearchTree, OrderedDoublyLinkedList, RBTree
from Segment import Segment
from Point2D import Point2D
from time import clock
import TestData
import matplotlib.pyplot as pyplot

data_folder = "data/"
images_folder = "images/"

def hasIntersectionOnSet(setOfSegments, activeSegments):
    idCounter = 0
    setOfPoints = []
    for segment in setOfSegments:
        segment.id = idCounter
        idCounter += 1
        #add the segment id to its end points
        segment.first.id = segment.id
        segment.second.id = segment.id
        #add the points to a set of points
        setOfPoints.append(segment.first)
        setOfPoints.append(segment.second)

    segmentsSeen = [False for i in range(idCounter+1)]
    #sort points lexicographically
    start = clock()
    setOfPoints = sorted(setOfPoints, key=lambda p:(p.x, p.y))

    for point in setOfPoints:
        currentSegment = setOfSegments[point.id]
        #print("Current Point: ", point)
        #first endpoint
        if(not segmentsSeen[point.id]):
            activeSegments.insert(currentSegment)

            #activeSegments.inOrderPrint(activeSegments.root)
            activeSegments.printNodes()
            print("--------------------------------------")

            segmentsSeen[currentSegment.id] = True
            aboveSegment = activeSegments.successor(currentSegment)
            belowSegment = activeSegments.antecessor(currentSegment)
            print("AB", aboveSegment, belowSegment)
            if (aboveSegment is not None) and currentSegment.intersects(aboveSegment.data) or (belowSegment is not None) and currentSegment.intersects(belowSegment.data):
                return True, (clock() - start)
        else:
            segmentsSeen[currentSegment.id] = False
            aboveSegment = activeSegments.successor(currentSegment)
            belowSegment = activeSegments.antecessor(currentSegment)
            print("AB REM", aboveSegment, belowSegment)

            if((aboveSegment is not None) and (belowSegment is not None) and (aboveSegment.data.intersects(belowSegment.data))):
                return True
            activeSegments.remove(currentSegment)

            activeSegments.printNodes()
            print("--------------------------------------")

    return False, (clock() - start)


def compareDataStructuresPerformance(testPrefix, data_structures, limit):
    N = 1
    times = []
    counter = 0
    for i in data_structures:
        times.append([])
        counter +=1

    for i in range(limit):
        N = N*10
        segments = Segment.readFromFile(data_folder + testPrefix + str(N) + ".txt")
        index = 0
        for data_structure in data_structures:
            #t = clock()
            structure = deepcopy(data_structure)
            result, t = hasIntersectionOnSet(segments, structure)
            #t = clock() - t
            times[index].append(t)
            index = (index + 1)%counter
    return times

def plotPerformanceGraph(limit, times, data_structures, colors, testlabel):

    x = [10**i for i in range(1, limit+1)]

    #data_structures contains the names of the data strcutures used
    index = 0
    for data_structure in data_structures:
        pyplot.plot(x, times[index], color = colors[data_structure], label = data_structure)
        index += 1

    #pyplot.axis([ 0, xlimit, 0, 20 ])
    pyplot.legend()
    pyplot.title("Line sweep performance comparison for different data structures")
    pyplot.xlabel('N')
    pyplot.ylabel('time (s)')
    pyplot.savefig( images_folder + testlabel + ".png")
    pyplot.close()
    #pyplot.show()


def segmentsToPostscript(setOfSegments, filename):
    with open(filename, "w") as myfile:
        myfile.write("0.1 setlinewidth\n")
        for segment in setOfSegments:
            myfile.write("{0} {1} moveto\n".format(segment.first.x, segment.first.y))
            myfile.write("{0} {1} lineto\n".format(segment.second.x, segment.second.y))
        myfile.write("0 setgray\n")
        myfile.write("stroke")

if __name__ == '__main__':
    print("Called main module")
    a = Segment(Point2D(0, 5), Point2D(4,4), "a")
    b = Segment(Point2D(1,0), Point2D(11, 6), "b")
    c = Segment(Point2D(2,2), Point2D(6, 4), "c")
    d = Segment(Point2D(3,5), Point2D(10, 3), "d")
    e = Segment(Point2D(5,6), Point2D(9, 4), "e")
    f = Segment(Point2D(7,2), Point2D(8, 1), "f")
    segments = [a, b, c, d, e, f]
    segmentsToPostscript(segments, "teste.eps")

    print(hasIntersectionOnSet(segments, RBTree()))
    #TestData.writeFirstTest()
    #TestData.writeSecondTest()
    #segments = Segment.readFromFile(data_folder + "second_100.txt")
    #print(hasIntersectionOnSet(segments, BinarySearchTree()))
    # data_structures = [OrderedDoublyLinkedList(), RBTree()]
    # names = [OrderedDoublyLinkedList.__name__, RBTree.__name__]
    # colors = dict(zip(names, ["blue", "red"]))
    # limit = 3
    # third_test_times = compareDataStructuresPerformance("third_", data_structures, limit)
    # testlabel = "Second Test"
    # plotPerformanceGraph(limit, third_test_times, names, colors, testlabel)


    # rb_tree = RBTree()
    # for i in range(100):
    #     rb_tree.insert(i)
    #     #print(i)
    #
    # print(rb_tree.getHeight())
