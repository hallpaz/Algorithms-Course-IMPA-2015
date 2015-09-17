import matplotlib.pyplot as pyplot
import csv
from time import clock
from copy import deepcopy
from math import log, log10, pi, floor

from Sorting import *
from TestScripts import *

#data initialization

images_folder = '/images/'
data_folder = '/data/'
colors = {selection_sort.__name__: 'black', insertion_sort.__name__: 'yellow', mergesort.__name__: 'green', quicksort.__name__: 'red', heapsort.__name__: 'blue', adaptative_mergesort.__name__: 'magenta', adaptative_quicksort: 'cyan'}

def compare_algorithms_with_generated_data(sorting_algorithms:list, list_generator, min_size=100, max_size=10000):
    sorting_times = { alg.__name__ : [] for alg in sorting_algorithms }

    for size in range(min_size, maxsize+1):
        test_list = list_generator(size)
        for algorithm in sorting_algorithms:
            current_list = deepcopy(test_list)
            #start time
            start = clock()
            algorithm(current_list)
            sorting_times[algorithm.__name__].append(clock()-start)

    x = [i for i in range(min_size, max_size)]
    for algorithm, times in sorting_times.iteritems():
        pyplot.plot(x, times[min_size:maxsize+1], color = colors[algorithm], label = algorithm)
        #pyplot.plot(x, theoretical_data, color = theoretical_color, label = 'Theoretical')
        #pyplot.axis([ 0, xlimit, 0, 20 ])
        pyplot.legend()
        pyplot.title("Execution time (" + list_generator.__name__ + " ) for " algorithm)
        pyplot.xlabel('N')
        pyplot.ylabel('Time (s)')
        pyplot.savefig( images_folder + algorithm  + "_" + list_generator.__name__ ".png")

    for algorithm, times in sorting_times.iteritems():
        pyplot.plot(x, times[min_size:maxsize+1], color = colors[algorithm], label = algorithm)
    pyplot.legend()
    pyplot.title("Execution time (" + list_generator.__name__ + " ) for all")
    pyplot.xlabel('N')
    pyplot.ylabel('Time (s)')
    pyplot.savefig( images_folder +  "all_" + list_generator.__name__ ".png")

def compare_algorithms_with_test_file(sorting_algorithms:list, test_file:str):
    sorting_times = { alg.__name__ : 0 for alg in sorting_algorithms }

    with open(data_folder + test_file) as file:
        test_list = file.read().splitlines()
        for algorithm in sorting_algorithms:
            current_list = deepcopy(test_list)
            #start time
            start = clock()
            algorithm(current_list)
            sorting_times[algorithm.__name__] = (clock()-start)

        #plot bar graph
                                                        dictionary = plt.figure()
                                                        pyplot.bar(range(len(D)), D.values(), align='center')
                                                        plt.xticks(range(len(D)), D.keys())

                                                        pyplot_mpl(dictionary, filename='mpl-dictionary')


if __name__ == '__main__':
    sorting_algorithms = [selection_sort, insertion_sort, mergesort, quicksort, heapsort, adaptative_mergesort, adaptative_quicksort]
    list_generator_functions = [generate_list_random_numbers, generate_list_ordered, generate_list_reverse_ordered, generate_list_unique]

    for algorithm in sorting_algorithms:
        validate_sorting_algorithm(algorithm)

    for list_generator in list_generator_functions:
        compare_algorithms_with_generated_data(sorting_algorithms, list_generator)

    compare_algorithms_with_test_file("BR4.txt")
    compare_algorithms_with_test_file("BR5.txt")

def compare_algorithms_with_random_numbers(sorting_algorithms:list, min_size=100, max_size=10000):
    sorting_times = { alg.__name__ : [] for alg in sorting_algorithms }

    for size in range(min_size, maxsize+1):
        test_list = generate_list_random_numbers(size)
        for algorithm in sorting_algorithms:
            current_list = deepcopy(test_list)
            #start time
            start = clock()
            algorithm(current_list)
            sorting_times[algorithm.__name__].append(clock()-start)

    x = [i for i in range(min_size, max_size)]
    for algorithm, times in sorting_times.iteritems():
        pyplot.plot(x, times[0:xlimit], color = exp_color, label = algorithm)
        #pyplot.plot(x, theoretical_data, color = theoretical_color, label = 'Theoretical')
        #pyplot.axis([ 0, xlimit, 0, 20 ])
        pyplot.legend()
        pyplot.title("Execution time (random input) for " algorithm)
        pyplot.xlabel('N')
        pyplot.ylabel('Time (s)')
        pyplot.savefig( algorithm  + "_random.png")
