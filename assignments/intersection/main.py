from DataStructures import BinarySearchTree, OrderedDoublyLinkedList, RBTree
from Segment import Segment
from Point2D import Point2D



def hasIntersectionOnSet(setOfSegments):
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
    setOfPoints = sorted(setOfPoints, key=lambda p:(p.x, p.y))

    processingSegments = OrderedDoublyLinkedList()
    #processingSegments = BinarySearchTree()

    for point in setOfPoints:
        currentSegment = setOfSegments[point.id]
        print("Current Point: ", point)
        #first endpoint
        if(not segmentsSeen[point.id]):
            processingSegments.insert(currentSegment)

            #processingSegments.inOrderPrint(processingSegments.root)
            processingSegments.printNodes()
            print("--------------------------------------")

            segmentsSeen[currentSegment.id] = True
            aboveSegment = processingSegments.successor(currentSegment)
            belowSegment = processingSegments.antecesor(currentSegment)
            if (aboveSegment is not None) and currentSegment.intersects(aboveSegment.data) or (belowSegment is not None) and currentSegment.intersects(belowSegment.data):
                return True
        else:
            segmentsSeen[currentSegment.id] = False
            aboveSegment = processingSegments.successor(currentSegment)
            belowSegment = processingSegments.antecesor(currentSegment)
            if((aboveSegment is not None) and (belowSegment is not None) and (aboveSegment.data.intersects(belowSegment.data))):
                return True
            processingSegments.remove(currentSegment)

            processingSegments.printNodes()
            print("--------------------------------------")

    return False


if __name__ == '__main__':
    print("Called main module")
    a = Segment(Point2D(0, 5), Point2D(4,4), "a")
    b = Segment(Point2D(1,0), Point2D(11, 6), "b")
    c = Segment(Point2D(2,2), Point2D(6, 4), "c")
    d = Segment(Point2D(3,5), Point2D(10, 3), "d")
    e = Segment(Point2D(5,6), Point2D(9, 4), "e")
    f = Segment(Point2D(7,2), Point2D(8, 1), "f")
    segments = [a, b, c, d, e, f]

    print(hasIntersectionOnSet(segments))
