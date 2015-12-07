from enum import Enum

class Direction(Enum):
    """docstring for Direction"""
    Left = 0
    Right = 1

class Point2D:

    def read_from_file(filename:str)->list:
        points = []
        with open(filename) as myfile:
            file_lines = myfile.readlines()
            for line in file_lines:
                content = line.split()
                if len(content) == 2:
                    points.append(Point2D(float(content[0]), float(content[1]) ))
                elif len(content) == 3:
                    points.append(Point2D(float(content[1]), float(content[2]), content[0]))
                else:
                    print("Weird file. Result undefined")
        return points

    def isclose(a, b, rel_tol=1e-5):
        if(a - b < rel_tol):
            return True
        return False

    def __init__(self, x=0, y=0, name = None):
        self.x = x
        self.y = y
        self.name = name
        #self.comparator = (self.x, self.y)

    def __str__(self):
        representation = ""
        if self.name is not None:
            representation += self.name + " "
        representation += "({0}, {1})".format(str(self.x), str(self.y))
        return representation

    def __add__(self, other):
        """ Addition of 2 points  """
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Subtraction of 2 points """
        return Point2D(self.x - other.x, self.y - other.y)

    def __rmul__(self, other):
        """ Multiplication by scalar """
        return Point2D(other*self.x, other*self.y)

    # def __lt__(self, other):
    #     if(Point2D.CCW_test(other, self) < 0):
    #         return True
    #     elif(Point2D.CCW_test == 0):
    #         return ((self.y, self.x) < (other.y, other.x))
    #     return False
    # def __le__(self, other):
    #      return (self.comparator <= other.comparator)
    def __eq__(self, other):
         return (Point2D.isclose(self.x, other.x) and Point2D.isclose(self.y, other.y))
    # def __ne__(self, other):
    #      return (self.comparator != other.comparator)
    # def __gt__(self, other):
    #      return (self.comparator > other.comparator)
    # def __ge__(self, other):
    #      return (self.comparator >= other.comparator)


def CCW_test(p1:Point2D, p2:Point2D, origin = None)->float:
    """ Checks if p2 is in counterclockwise position relative to p1
    If p2 is CCW p1, returns a positive value. If p2 is CW p1, returns a negative value"""
    if origin is None:
        origin = Point2D()
    translated_p1 = p1 - origin
    translated_p2 = p2 - origin
    cross_value = translated_p2.x*translated_p1.y - translated_p1.x*translated_p2.y

    return cross_value

def direction(p1:Point2D, p2:Point2D, origin = None):
    if CCW(p1, p2, origin) > 0:
        return LEFT
