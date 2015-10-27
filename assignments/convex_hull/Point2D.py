

class Point2D:

    def read_from_file(filename:str)->list:
        points = []
        with open(filename) as myfile:
            file_lines = myfile.readlines()
            for line in file_lines:
                if len(line) == 2:
                    points.append(Point2D(line[0], line[1]))
                elif len(line) == 3:
                    points.append(Point2D(line[1], line[2], line[0]))
                else:
                    print("Weird file. Result undefined")
        return points
    def __init__(self, x=0, y=0, name = None):
        self.x = x
        self.y = y
        self.name = name
        self.comparator = (self.x, self.y)

    def __str__(self):
        representation = str(self.name) + " " + str( (self.x, self.y) )
        return representation

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # def __lt__(self, other):
    #      return (self.comparator < other.comparator)
    # def __le__(self, other):
    #      return (self.comparator <= other.comparator)
    # def __eq__(self, other):
    #      return (self.comparator == other.comparator)
    # def __ne__(self, other):
    #      return (self.comparator != other.comparator)
    # def __gt__(self, other):
    #      return (self.comparator > other.comparator)
    # def __ge__(self, other):
    #      return (self.comparator >= other.comparator)
