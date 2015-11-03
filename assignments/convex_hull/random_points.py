import matplotlib.pyplot as pyplot
from Point2D import Point2D
from convex_hull import Graham, Graham_up_down, Jarvis
from copy import deepcopy
from math import pi, sin, cos, sqrt
from random import random
from time import clock

import csv

colors = { Graham.__name__: 'green', Jarvis.__name__: 'red', Graham_up_down.__name__: 'purple' }
images_folder = 'images/'
data_folder = 'data/'

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


def compare_algorithms_with_generated_data(hull_algorithms:list, list_generator, xsamples = None):
    hull_times = { alg.__name__ : [] for alg in hull_algorithms }
    if(xsamples is None):
        xsamples = list(range(100, 1001, 100))

    for x in xsamples:
        test_list = list_generator(x)
        for algorithm in hull_algorithms:
            print(len(test_list), list_generator.__name__)
            current_list = deepcopy(test_list)
            print(algorithm.__name__, len(current_list))
            #start time
            start = clock()
            algorithm(current_list)
            hull_times[algorithm.__name__].append(clock()-start)

    for algorithm, times in hull_times.items():
        with open(data_folder + algorithm + list_generator.__name__ + ".csv", 'w+', newline='') as wfile:
            a = csv.writer(wfile, delimiter=',')
            a.writerows(zip(xsamples, times))
    for algorithm, times in hull_times.items():
        pyplot.figure()
        pyplot.plot(xsamples, times, color = colors[algorithm], label = algorithm)
        pyplot.legend()
        pyplot.title("Execution time (" + list_generator.__name__ + " ) for " + algorithm)
        pyplot.xlabel('N')
        pyplot.ylabel('Time (s)')
        pyplot.savefig( images_folder + algorithm  + "_" + list_generator.__name__ + ".png")
        pyplot.close()

    pyplot.figure()
    for algorithm, times in hull_times.items():
        pyplot.plot(xsamples, times, color = colors[algorithm], label = algorithm)
    pyplot.legend()
    pyplot.title("Execution time (" + list_generator.__name__ + " ) for all")
    pyplot.xlabel('N')
    pyplot.ylabel('Time (s)')
    pyplot.savefig( images_folder +  "all_" + list_generator.__name__ + ".png")
    pyplot.close()

if __name__ == "__main__":
    generators = [random_list_rectangle, random_list_triangle, random_list_disk, random_list_circle]
    algorithms = [Graham, Graham_up_down, Jarvis]
    xsamples = [i*100 for i in range(1,10)]
    #xsamples += [i*1000 for i in range(1,10)]
    #xsamples += [i*10000 for i in range(1,11)]

    for g in generators:
        compare_algorithms_with_generated_data(algorithms, g, xsamples)
