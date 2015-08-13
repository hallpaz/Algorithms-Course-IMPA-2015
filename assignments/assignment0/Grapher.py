import matplotlib.pyplot as pyplot
import csv
from math import log, log10, pi, floor


titles = ['min_value', 'max_value', 'avg_value']
colors = ['blue', 'red', 'green']
filename = 'allcombinations_data.csv'

def plot_min_max_avg_together(filename='min_max_avg.png', xlimit = 1000):

    for i in range(len(titles)):
        # 0 index is for the x axis
        pyplot.plot(plotdata[0], plotdata[i+1], color = colors[i], label = titles[i])

    pyplot.axis([ 0, xlimit, 0, 25 ])
    pyplot.legend()
    pyplot.title('Min, Max and Avg values')
    pyplot.xlabel('N')
    pyplot.ylabel('number of steps')
    pyplot.savefig(filename)

def plot_experimental_and_theoretical_curves(exp_data, exp_label, theoretical_function, theoretical_label, xlimit = 1000, exp_color = 'green', theoretical_color='cyan'):
    x = [i for i in range(1, xlimit+1)]

    theoretical_data = [theoretical_function(i) for i in x]

    pyplot.plot(x, exp_data[0:xlimit], color = exp_color, label = 'Experimental')
    pyplot.plot(x, theoretical_data, color = theoretical_color, label = 'Theoretical')

    pyplot.axis([ 0, xlimit, 0, 25 ])
    pyplot.legend()
    pyplot.title(exp_label + " and " + theoretical_label)
    pyplot.xlabel('N')
    pyplot.ylabel('number of steps')
    pyplot.savefig(exp_label + "_" + theoretical_label + "floor.png")


if __name__ == '__main__':

    with open(filename) as stepsfile:
        reader = csv.reader(stepsfile)
        plotdata = [row for row in reader]
        plotdata = [ list(data) for data in zip(*plotdata) ]

    pyplot.figure(1)
    plot_min_max_avg_together()

    pyplot.figure(2)
    plot_experimental_and_theoretical_curves(plotdata[2], 'exp_max', lambda x: (4.785*log10(x) + 1.6723-2), 'theo_max', exp_color='red')

    pyplot.figure(3)
    plot_experimental_and_theoretical_curves(plotdata[3], 'exp_avg', lambda x: ( 12/(pi*pi) )*log(2)*log(x) + 0.06, 'theo_avg', theoretical_color='magenta')
