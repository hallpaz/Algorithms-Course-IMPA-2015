

class Point2D:

    def read_from_file(filename:str)->list:
        points = []
        index = 0
        with open(filename) as myfile:
            file_lines = myfile.readlines()
            for line in file_lines:
                content = line.split()
                if len(content) == 2:
                    index += 1
                    points.append(Point2D(float(content[0]), float(content[1]), "P" + str(index) ))
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

    def __eq__(self, other):
         return (Point2D.isclose(self.x, other.x) and Point2D.isclose(self.y, other.y))
