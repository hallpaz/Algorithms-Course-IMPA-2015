

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
        representation = str(self.name) + " " + str(self.x) + " " + str(self.y)
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
