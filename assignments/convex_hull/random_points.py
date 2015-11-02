from Point2D import Point2D
from math import pi, sin, cos, sqrt
from random import random


def random_point_circle(radius=1.0)->Point2D:
    """ Returns a point uniformly sampled in a circle """
    t = 2*pi*random()
    return Point2D(radius*cos(t), radius*sin(t))

def random_point_disk(radius=1.0)->Point2D:
    """ Returns a point uniformly sampled in a disk"""
    t = 2*pi*random()
    u = random()+ random()
    r = ((2-u) if u > 1 else u)*radius
    return Point2D(r*cos(t), r*sin(t))

def random_point_rectangle(base:float, height:float, inf_left_corner = Point2D())->Point2D:
    x = random()
    y = random()
    return Point2D(inf_left_corner.x + x*base, inf_left_corner.y + y*height)

def random_point_triangle(A:Point2D, B:Point2D, C:Point2D)->Point2D:
    """ Returns a point uniformly sampled inside a triangle of vertices A, B and C """
    r1 = random()
    r2 = random()
    return (1 - sqrt(r1)) * A + (sqrt(r1) * (1 - r2)) * B + (sqrt(r1) * r2) * C

def random_list_circle(list_size = 100, radius=1.0)->list:
    return [random_point_circle(radius) for p in range(list_size)]

def random_list_disk(list_size = 100, radius=1.0)->list:
    return [random_point_disk(radius) for p in range(list_size)]

def random_list_rectangle(list_size = 100, base=2.0, height=1.0, inf_left_corner = Point2D())->list:
    return [random_point_rectangle(base, height, inf_left_corner) for p in range(list_size)]

def random_list_triangle(list_size = 100, A=Point2D(-1, 0), B=Point2D(1, 0), C=Point2D(0, 2))->list:
    return [random_point_triangle(A, B, C) for p in range(list_size)]


if __name__ == "__main__":
    random_point_circle()
    random_point_disk()
    random_list_rectangle()
    random_list_triangle()
