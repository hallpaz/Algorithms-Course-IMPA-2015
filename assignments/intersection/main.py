from DataStructures import BinarySearchTree, DoublyLinkedList, RBTree
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
    sorted(setOfPoints, key=lambda p:(p.x, p.y))

    DoublyLinkedList processingSegments = DoublyLinkedList()

    for point in setOfPoints:
        currentSegment = setOfSegments[point.id]
        #first endpoint
        if(not segmentsSeen[point.id]):
            processingSegments.insert(currentSegment)
            segmentsSeen[currentSegment.id] = True
            aboveSegment = processingSegments.above(currentSegment)
            belowSegment = processingSegments.below(currentSegment)
            if (aboveSegment is not None) and currentSegment.intersects(aboveSegment)
            or (belowSegment is not None) and currentSegment.intersects(belowSegment):
                return True
        else:
            segmentsSeen[currentSegment.id] = False
            aboveSegment = processingSegments.above(currentSegment)
            belowSegment = processingSegments.below(currentSegment)
            if((aboveSegment is not None) and (belowSegment is not None) and (aboveSegment.intersects(belowSegment))):
                return True
            processingSegments.remove(currentSegment)

        return False


if __name__ == '__main__':
    print("Called main module")
