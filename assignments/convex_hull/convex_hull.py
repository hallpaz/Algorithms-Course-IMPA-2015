import Point2D


def CCW_test(p1:Point2D, p2:Point2D, origin = None)->float:
    """ Checks if p2 is in counterclockwise position relative to p1"""
    if origin is None:
        origin = Point2D()
    translated_p1 = p1 - origin
    translated_p2 = p2 - origin
    cross_value = translated_p2.x*translated_p1.y - translated_p1.x*translated_p2.y

    return cross_value

def turns_left(p1:Point2D, p2:Point2D, origin:Point2D)->bool:
    """Checks wether an angle p1-origin-p2 turns left or not"""
    if CCW_test(p1, p2, origin) < 0:
        return True
    return False

def Jarvis():
    pass

def Graham(points:list):
    #p0 <- point of min y
    p0 = min(points, key=lambda p: (p.y, p.x))

    #sort other points in counterclockwise order around p0
    points = sorted(points, key=lambda p: CCW_test(Point(), p, p0)) #check if I could change the origin
    #push(p0, p1, p2)
    stack = [p0, p1, p2]

    for p in poits[3:]:
        while not turns_left(stack[-2], p, stack[-1]):
            stack.pop()
        stack.append(p)
    return stack

if __name__ == "__main__":
    print("Convex Hull file called as main")

    data_folder = "data/"

    filename = data_folder + "teste.txt"
    points = Point2D.read_from_file(filename)
    convex_hull = Graham(points)
    for point in convex_hull:
        print(point)
