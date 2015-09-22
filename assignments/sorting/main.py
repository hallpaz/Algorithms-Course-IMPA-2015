import matplotlib.pyplot as pyplot
import csv
from time import clock
from copy import deepcopy
from math import log, log10, pi, floor

from Sorting import *
from TestScripts import *

#data initialization

images_folder = 'images/'
data_folder = 'data/'
colors = {selection_sort.__name__: 'black', insertion_sort.__name__: 'yellow', mergesort.__name__: 'green', quicksort.__name__: 'red', heapsort.__name__: 'blue', adaptative_mergesort.__name__: 'magenta', adaptative_quicksort.__name__: 'cyan', adaptative_quicksort_v2.__name__: 'brown', tco_quicksort.__name__: 'purple'}

def compare_algorithms_with_generated_data(sorting_algorithms:list, list_generator, xsamples = None):
    sorting_times = { alg.__name__ : [] for alg in sorting_algorithms }
    if(xsamples is None):
        xsamples = list(range(100, 1001, 100))

    for x in xsamples:
        test_list = list_generator(x)
        for algorithm in sorting_algorithms:
            current_list = deepcopy(test_list)
            print(algorithm.__name__, len(current_list))
            #start time
            start = clock()
            algorithm(current_list)
            sorting_times[algorithm.__name__].append(clock()-start)

    for algorithm, times in sorting_times.items():
        with open(data_folder + algorithm + list_generator.__name__ + ".csv", 'w+', newline='') as wfile:
            a = csv.writer(wfile, delimiter=',')
            a.writerows(zip(xsamples, times))

    for algorithm, times in sorting_times.items():
        pyplot.figure()
        pyplot.plot(xsamples, times, color = colors[algorithm], label = algorithm)
        pyplot.legend()
        pyplot.title("Execution time (" + list_generator.__name__ + " ) for " + algorithm)
        pyplot.xlabel('N')
        pyplot.ylabel('Time (s)')
        pyplot.savefig( images_folder + algorithm  + "_" + list_generator.__name__ + ".png")
        pyplot.close()

    pyplot.figure()
    for algorithm, times in sorting_times.items():
        pyplot.plot(xsamples, times, color = colors[algorithm], label = algorithm)
    pyplot.legend()
    pyplot.title("Execution time (" + list_generator.__name__ + " ) for all")
    pyplot.xlabel('N')
    pyplot.ylabel('Time (s)')
    pyplot.savefig( images_folder +  "all_" + list_generator.__name__ + ".png")
    pyplot.close()

def compare_algorithms_with_test_file(sorting_algorithms:list, test_file:str):
    sorting_times = { alg.__name__ : 0 for alg in sorting_algorithms }

    with open(data_folder + test_file) as file:
        test_list = file.read().splitlines()
        for algorithm in sorting_algorithms:
            print("running ", algorithm.__name__, "on ", test_file)
            current_list = deepcopy(test_list)
            #start time
            start = clock()
            algorithm(current_list)
            sorting_times[algorithm.__name__] = (clock()-start)

        # for algorithm, times in sorting_times.items():
        #     with open(data_folder + algorithm + test_file + ".csv", 'a+', newline='') as wfile:
        #         a = csv.writer(wfile, delimiter=',')
        #         a.writerow(times)
        #plot bar graph
        left_edges = [i for i in range(len(sorting_algorithms))]
        width = 1.0
        pyplot.bar(left_edges, list(sorting_times.values()), color=list(colors.values()))
        pyplot.ylabel('Time (s)')
        pyplot.title("Execution time (file " + test_file + ") all algorithms")
        pyplot.legend()
        pyplot.xticks([i + width/2 for i in left_edges], list(sorting_times.keys()))
        pyplot.savefig( images_folder +  "comparison_" + test_file + ".png")
        pyplot.close()

        logtimes = [sorting_times[mergesort.__name__], sorting_times[heapsort.__name__], sorting_times[quicksort.__name__]]
        logcolors = [colors[mergesort.__name__], colors[heapsort.__name__], colors[quicksort.__name__]]
        loglabels = ["merge", "heap", "quick"]
        loglefts = [i for i in range(len(logtimes))]
        pyplot.bar(loglefts, logtimes , color=logcolors)
        pyplot.ylabel('Time (s)')
        pyplot.title("Execution time (file " + test_file + ") log algorithms")
        pyplot.legend()
        pyplot.xticks([i + width/2 for i in loglefts], loglabels)
        pyplot.savefig( images_folder +  "comparison_log" + test_file + ".png")


def read_and_plot(sorting_algorithms, list_generator):
    flag = True
    for algorithm in sorting_algorithms:
        with open(data_folder + algorithm.__name__ + "_repetitions_70" + ".csv") as datafile:
            reader = csv.reader(datafile)
            if(flag):
                plotdata = [row for row in reader]
                plotdata = [ list(data) for data in zip(*plotdata) ]
                flag = False
            else:
                aux = [row for row in reader]
                aux = [ list(data) for data in zip(*aux) ]
                plotdata.append(aux[1])

    pyplot.figure()
    for i in range(3):
        algorithm = sorting_algorithms[i].__name__
        pyplot.plot(plotdata[0], plotdata[i+1], color = colors[algorithm], label = algorithm)
    pyplot.legend()
    pyplot.title("Execution time (repetitions_70"  + " ) insertion and selection")
    pyplot.xlabel('N')
    pyplot.ylabel('Time (s)')
    pyplot.savefig( images_folder +  "ins_sel"   + "repetitions_70.png")
    pyplot.close()

    pyplot.figure()
    for i in range(3, len(sorting_algorithms)):
        algorithm = sorting_algorithms[i].__name__
        pyplot.plot(plotdata[0], plotdata[i+1], color = colors[algorithm], label = algorithm)
    pyplot.legend()
    pyplot.title("Execution time (repetitions_70"  + " ) log algorithms")
    pyplot.xlabel('N')
    pyplot.ylabel('Time (s)')
    pyplot.savefig( images_folder +  "log_alg"  + "repetitions_70.png")
    pyplot.close()

def compare_adaptative_algorithm(algorithm, list_generator, list_length=10000):
    #thresholds = list(range(0, 201, 20))
    thresholds = list(range(1, 102, 10))
    sorting_times = []
    test_list = list_generator(list_length)
    smooth_times = 200
    for x in thresholds:
        current_list = deepcopy(test_list)
        print(algorithm.__name__, x)
        #start time
        cum_time = 0
        for k in range(smooth_times):
            start = clock()
            algorithm(current_list, 0, len(test_list)-1, x)
            cum_time += (clock()-start)
        sorting_times.append(cum_time/smooth_times)

    # left_edges = [i for i in range(len(thresholds))]
    # width = 0.4
    # pyplot.bar(left_edges, sorting_times, color=colors[algorithm.__name__])
    # pyplot.ylabel('Time (s)')
    # pyplot.title("Execution time many thresholds " + algorithm.__name__ )
    # pyplot.legend()
    # pyplot.xticks([i + width/2 for i in left_edges], thresholds, rotation='vertical')
    # pyplot.savefig( images_folder +  "comparison_" + algorithm.__name__ + ".png")
    # pyplot.close()
    pyplot.figure()
    #for i in range(2, len(sorting_algorithms)):
    pyplot.plot(thresholds, sorting_times, color = colors[algorithm.__name__], label = algorithm.__name__)
    pyplot.legend()
    pyplot.title("Execution time (" + list_generator.__name__ + " ) log algorithms")
    pyplot.xlabel('N')
    pyplot.ylabel('Time (s)')
    pyplot.savefig( images_folder +  algorithm.__name__ + list_generator.__name__ + "_smoothed.png")
    pyplot.close()


def compare_algorithms_with_repetitions(sorting_algorithms:list, rep_factor, xsamples = None):
    sorting_times = { alg.__name__ : [] for alg in sorting_algorithms }
    if(xsamples is None):
        xsamples = list(range(100, 1001, 100))

    for x in xsamples:
        test_list = generate_list_many_repetitions(x, rep_factor)
        for algorithm in sorting_algorithms:
            current_list = deepcopy(test_list)
            print(algorithm.__name__, len(current_list))
            #start time
            start = clock()
            algorithm(current_list)
            sorting_times[algorithm.__name__].append(clock()-start)

    for algorithm, times in sorting_times.items():
        with open(data_folder + algorithm + "_repetitions_" + str(rep_factor) + ".csv", 'w+', newline='') as wfile:
            a = csv.writer(wfile, delimiter=',')
            a.writerows(zip(xsamples, times))

    for algorithm, times in sorting_times.items():
        pyplot.figure()
        pyplot.plot(xsamples, times, color = colors[algorithm], label = algorithm)
        pyplot.legend()
        pyplot.title("Execution time (repetitions " +str(rep_factor) + " ) for " + algorithm)
        pyplot.xlabel('N')
        pyplot.ylabel('Time (s)')
        pyplot.savefig( images_folder + algorithm  + "_repetitions" + str(rep_factor) + ".png")
        pyplot.close()

    pyplot.figure()
    for algorithm, times in sorting_times.items():
        pyplot.plot(xsamples, times, color = colors[algorithm], label = algorithm)
    pyplot.legend()
    pyplot.title("Execution time (%" + str(rep_factor) + " repetitions) for all")
    pyplot.xlabel('N')
    pyplot.ylabel('Time (s)')
    pyplot.savefig( images_folder +  "all_" + str(rep_factor) + ".png")
    pyplot.close()



if __name__ == '__main__':
    #sorting_algorithms = [selection_sort, insertion_sort, mergesort, quicksort, heapsort, adaptative_mergesort, adaptative_quicksort]
    sorting_algorithms = [selection_sort, insertion_sort, tco_quicksort, mergesort, heapsort ]
    list_generator_functions = [generate_list_random_numbers, generate_list_ordered, generate_list_reverse_ordered, generate_list_unique]

    #for algorithm in sorting_algorithms:
    #    validate_sorting_algorithm(algorithm)

    xsamples  = [x*100 for x in range(1, 10) ]
    xsamples = xsamples + [x*1000 for x in range(1, 10)]
    xsamples = xsamples + [x*10000 for x in range(1, 5)]
    #for list_generator in list_generator_functions:
    #    print("Applying test method " + list_generator.__name__)
    #    compare_algorithms_with_generated_data(sorting_algorithms, list_generator)
    #compare_algorithms_with_generated_data(sorting_algorithms, list_generator, xsamples)
    #compare_algorithms_with_generated_data([selection_sort], generate_list_unique, xsamples)

    #compare_algorithms_with_test_file(sorting_algorithms, "BR4.txt")
    #compare_algorithms_with_test_file(sorting_algorithms, "BR5.txt")

    #read_and_plot(sorting_algorithms, generate_list_random_numbers)
    #read_and_plot(sorting_algorithms, generate_list_ordered)
    #read_and_plot(sorting_algorithms, generate_list_reverse_ordered)
    #read_and_plot(sorting_algorithms, generate_list_unique)
    #read_and_plot(sorting_algorithms, generate_list_many_repetitions)

    #compare_adaptative_algorithm(adaptative_quicksort_v2, generate_list_random_numbers)
    compare_adaptative_algorithm(adaptative_quicksort, generate_list_random_numbers)
    #compare_adaptative_algorithm(adaptative_mergesort, generate_list_random_numbers)
    #for rep_factor in range(1000, 100000, 1000):
    #    compare_algorithms_with_repetitions([tco_quicksort], rep_factor, xsamples)
