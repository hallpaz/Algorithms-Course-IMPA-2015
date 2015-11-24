from Point2D import Point2D


class Segment():

    def __init__(self, pointA:Point2D, pointB:Point2D):
        self.first = A
        self.second = B
        if A.name and B.name:
            self.name = A.name + B.name
        else:
            self.name = None

    def intersects(self, other)->bool:
        d1 = CCW_test(other.second, self.first, other.first)
        d2 = CCW_test(other.second, self.second, other.first)
        d3 = CCW_test(self.second, other.first, self.first)
        d4 = CCW_test(self.second, other.second, self.first)

        if( ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0))):
            return True
        elif d1 == 0 and other.contains(p1)

    def contains(self, point)->bool:
        if (min(self.first.x, self.second.x) <= point.x and
        point.x <= max(self.first.x, self.second.x) and
        min(self.first.y, self.second.y) <= point.y and
        point.y <= max(self.first.x, self.second.y)):
            return true
        return False;




if __name__ == "__main__":
    print("Module called as main")
