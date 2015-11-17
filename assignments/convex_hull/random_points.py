import matplotlib.pyplot as pyplot
from Point2D import Point2D
from convex_hull import Graham, Graham_up_down, Jarvis, eliminate_interior_points
from copy import deepcopy
from math import pi, sin, cos, sqrt
from random import random
from time import clock

import csv

colors = { Graham.__name__: 'green', Jarvis.__name__: 'red', Graham_up_down.__name__: 'purple' }
images_folder = 'images/'
data_folder = 'data/'

DEBUG = False

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


def compare_algorithms_with_generated_data(hull_algorithms:list, list_generator, xsamples=None, trimm_interior=False):
    hull_times = { alg.__name__ : [] for alg in hull_algorithms }
    trimm_times_percentage = { alg.__name__ : [] for alg in hull_algorithms }
    if(xsamples is None):
        xsamples = list(range(100, 1001, 100))

    for x in xsamples:
        test_list = list_generator(x)
        trimm_time = 0
        if trimm_interior:
            start = clock()
            test_list = eliminate_interior_points(test_list)
            trimm_time = clock() - start
        for algorithm in hull_algorithms:
            current_list = deepcopy(test_list)
            if DEBUG:
                print(algorithm.__name__, len(current_list))
            #start time
            start = clock()
            algorithm(current_list)
            trimm_times_percentage[algorithm.__name__].append( (100*trimm_time)/(trimm_time+(clock()-start)) )

            hull_times[algorithm.__name__].append(clock()-start)

    for algorithm, times in hull_times.items():
        with open(data_folder + algorithm + list_generator.__name__ + str(trimm_interior) + ".csv", 'w+', newline='') as wfile:
            a = csv.writer(wfile, delimiter=',')
            a.writerows(zip(xsamples, times, trimm_times_percentage[algorithm]))
    for algorithm, times in hull_times.items():
        pyplot.figure()
        pyplot.plot(xsamples, times, color = colors[algorithm], label = algorithm)
        pyplot.legend()
        pyplot.title("Execution time (" + list_generator.__name__ + " ) for " + algorithm)
        pyplot.xlabel('N')
        pyplot.ylabel('Time (s)')
        pyplot.savefig( images_folder + algorithm  + "_" + list_generator.__name__ + str(trimm_interior) + ".png")
        if not trimm_interior:
            pyplot.show()
        pyplot.close()

    pyplot.figure()
    for algorithm, times in hull_times.items():
        pyplot.plot(xsamples, times, color = colors[algorithm], label = algorithm)
    pyplot.legend()
    pyplot.title("Execution time (" + list_generator.__name__ + " ) for all")
    pyplot.xlabel('N')
    pyplot.ylabel('Time (s)')
    pyplot.savefig( images_folder +  "all_" + list_generator.__name__ + str(trimm_interior) +".png")
    if not trimm_interior:
        pyplot.show()
    pyplot.close()

def compare_interior_elimination_effect(algorithm, generator):
    basename = data_folder + algorithm.__name__ + generator.__name__
    plotdata = []
    with open(basename + str(False) + ".csv", 'r') as falsefile:
        reader = csv.reader(falsefile)
        plotdata = [row for row in reader]
        plotdata = [ list(data) for data in zip(*plotdata) ]
        pyplot.plot(plotdata[0], plotdata[1], color = colors[algorithm.__name__], label = "no elimination")

    with open(basename + str(True) + ".csv", 'r') as truefile:
        reader = csv.reader(truefile)
        plotdata = [row for row in reader]
        plotdata = [ list(data) for data in zip(*plotdata) ]
        pyplot.plot(plotdata[0], plotdata[1], color = 'blue', label = "interior elimination")
    pyplot.legend()
    pyplot.title(algorithm.__name__ + " points elimination effects analysis")
    pyplot.xlabel('N')
    pyplot.ylabel('Time (s)')
    pyplot.savefig( images_folder +  algorithm.__name__   + "_trimm_analysis.png")
    pyplot.show()

    # with open(basename + str(True) + ".csv", 'r') as truefile:
    #     reader = csv.reader(truefile)
    #     plotdata = [row for row in reader]
    #     plotdata = [ list(data) for data in zip(*plotdata) ]
    pyplot.plot(plotdata[0], plotdata[2], color = 'blue', label = "elimination %")
    pyplot.legend()
    pyplot.title(algorithm.__name__ + " points elimination % performance analysis")
    pyplot.xlabel('N')
    pyplot.ylabel('Time %')
    pyplot.savefig( images_folder +  algorithm.__name__   + "_percentual_analysis.png")
    pyplot.show()


def plot_random_list_circle_results(trimm_interior):
    algorithms = [Graham, Graham_up_down, Jarvis]
    all_data = []
    for algorithm in algorithms:
        basename = data_folder + algorithm.__name__ + random_list_circle.__name__
        plotdata = []
        with open(basename + str(trimm_interior) + ".csv", 'r') as falsefile:
            reader = csv.reader(falsefile)
            plotdata = [row for row in reader]
            plotdata = [ list(data) for data in zip(*plotdata) ]
            all_data.append(plotdata)
            pyplot.plot(plotdata[0], plotdata[1], color = colors[algorithm.__name__], label = algorithm.__name__)
            pyplot.legend()
            pyplot.title("Execution time (" + random_list_circle.__name__ + " ) for " + algorithm.__name__)
            pyplot.xlabel('N')
            pyplot.ylabel('Time (s)')
            pyplot.savefig( images_folder + algorithm.__name__  + "_" + random_list_circle.__name__ + str(trimm_interior) + ".png")
            pyplot.show()

if __name__ == "__main__":
    generators = [random_list_rectangle, random_list_triangle, random_list_disk, random_list_circle]
    algorithms = [Graham, Graham_up_down, Jarvis]
    xsamples = [i*100 for i in range(1,10)]
    xsamples += [i*1000 for i in range(1,10)]
    #xsamples += [i*10000 for i in range(1,11)]

    # for g in generators:
    #     compare_algorithms_with_generated_data(algorithms, g, xsamples)
    compare_algorithms_with_generated_data(algorithms, random_list_circle, xsamples, True)
