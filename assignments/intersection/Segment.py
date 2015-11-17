from Point2D import Point2D


class Segment():

    def __init__(self, pointA:Point2D, pointB:Point2D):
        self.first = A
        self.second = B
        if A.name and B.name:
            self.name = A.name + B.name
        else:
            self.name = None

    def intersects(self, other):
        pass




if __name__ == "__main__":
    print("Module called as main")
