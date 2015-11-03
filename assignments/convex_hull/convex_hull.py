from Point2D import Point2D
from postscript_writer import *

DEBUG = False

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
    if CCW_test(p1, p2, origin) > 0:
        return True
    return False

def rel_cotan(p1:Point2D, p2:Point2D)->float:
    if(p1 == p2):
        return -float("inf")
    a = p1.y - p2.y
    b = p1.x - p2.x
    if(a < 1e-4):
        if(b < 0):
            return -float("inf")
        elif(b > 0):
            return float("inf")
    return -b/a

def euclidean_distance2(p1:Point2D, p2:Point2D)->float:
    return (p1.x-p2.x)**2 + (p1.y-p2.y)**2

def find_next_hull_point(points:list, p:Point2D)->Point2D:
    """ Jarvis helper procedure to find the next point from the hull given the last point found """
    next_point = p
    for point in points:
        fake_angle = CCW_test(p, point, next_point)
        if fake_angle < 0 or (fake_angle == 0 and (euclidean_distance2(p, point) > euclidean_distance2(p, next_point))):
            next_point = point

    return next_point

def Jarvis(points:list)->list:
    #p0 is a point that we definetily know it belongs to the hull
    next_point = min(points, key=lambda p: (p.y, -p.x))
    hull = [next_point]

    while True:
        next_point = find_next_hull_point(points, hull[-1])
        if(next_point != hull[0]):
            hull.append(next_point)
        else:
            break
    return hull

def Graham(points:list)->list:
    #p0 <- point of min y
    p0 = min(points, key=lambda p: (p.y, p.x))

    #sort other points in counterclockwise order around p0
    points = sorted(points, key=lambda p: (rel_cotan(p,p0), p.y) )
    #push(p0, p1, p2)
    offset = 1
    if(DEBUG):
        for p in points:
            print(p, rel_cotan( p, p0) )
        print('-----------------------------------------') #for debug purposes

    hull_stack = []
    for p in points:
        while (len(hull_stack) > 1) and (not turns_left(hull_stack[-2], p, hull_stack[-1])):
            hull_stack.pop()
        hull_stack.append(p)
    return hull_stack

def Graham_up_down(points:list)->list:
    points = sorted(points, key=lambda p: (p.x, p.y))

    lower_hull = []
    for p in points:
        while (len(lower_hull) > 1) and (not turns_left(lower_hull[-2], p, lower_hull[-1])):
            lower_hull.pop()
        lower_hull.append(p)

    upper_hull = []
    for p in reversed(points):
        while (len(upper_hull) > 1) and (not turns_left(upper_hull[-2], p, upper_hull[-1])) :
            upper_hull.pop()
        upper_hull.append(p)

    #merge both lists
    return (lower_hull[:-1] + upper_hull[:-1])

if __name__ == "__main__":
    print("Convex Hull file called as main")

    data_folder = "data/"

    #filename = data_folder + "teste.txt"
    filename = data_folder + "america.txt"
    points = Point2D.read_from_file(filename)
    convex_hull = Jarvis(points)
    for point in convex_hull:
        print(point)
    write_hull(convex_hull, data_folder + "hull_america.txt")
