from Point2D import Point2D

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
    current_fake_angle = float('inf')
    for point in points:
        fake_angle = rel_cotan(point, p)
        if (fake_angle < current_fake_angle) and (euclidean_distance2(p, point) > 0):
            next_point = point
            current_fake_angle = fake_angle
            #print(next_point)

    return next_point

def Jarvis(points:list)->list:
    #p0 is a point that we definetily know it belongs to the hull
    next_point = min(points, key=lambda p: (p.y, -p.x))
    hull = [next_point]

    while True:
        #print(next_point)
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
    hull_stack = [p0, points[1], points[2]]

    for p in points[3:]:
        while not turns_left(hull_stack[-2], p, hull_stack[-1]):
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

def eliminate_interior_points(points:list)->list:
    left = right = bottom = up = None
    for p in points:
        if left is None or p.x < left.x:
            left = p
        if right is None or p.x > right.x:
            right = p
        if bottom is None or p.y < bottom.y:
            bottom = p
        if up is None or p.y > up.y:
            up = p

    exterior_points = []
    for p in points:
        if (not turns_left(left, p, bottom)) or (not turns_left(bottom, p, right)) or (not turns_left(right, p, up)) or (not turns_left(up, p, left)):
            exterior_points.append(p)

    return exterior_points



if __name__ == "__main__":
    print("Convex Hull file called as main")

    data_folder = "data/"

    filename = data_folder + "teste.txt"
    points = Point2D.read_from_file(filename)
    points = eliminate_interior_points(points)
    for p in points:
        print(p)
    print('*****************************************')
    convex_hull = Graham_up_down(points)
    for point in convex_hull:
        print(point)
