import matplotlib.pyplot as pyplot
import csv


titles = ['min_value', 'max_value', 'avg_value']
colors = ['blue', 'red', 'green']

def plot_min_max_avg_together(filename='min_max_avg.png', xlimit = 1000):
    with open('steps_data.csv') as stepsfile:
        reader = csv.reader(stepsfile)
        plotdata = [row for row in reader]
        plotdata = [ list(data) for data in zip(*plotdata) ]

    for i in range(len(titles)):
        # 0 index is for the x axis
        pyplot.plot(plotdata[0], plotdata[i+1], color = colors[i], label = titles[i])

    pyplot.axis([ 0, xlimit, 0, 25 ])
    pyplot.legend()
    pyplot.title('Min, Max and Avg values')
    pyplot.xlabel('N')
    pyplot.ylabel('number of steps')
    pyplot.savefig(filename)

def plot_experimental_and_theoretical_curves(exp_data, exp_label, theoretical_function, theoretical_label, xlimit = 1000, exp_color = 'green', theoretical_color='magenta'):
    x = [i in range(xlimit+1)]

    theoretical_data = [theoretical_function(i) for i in x]

    pyplot.plot(plotdata[0], exp_data, color = exp_color, label = 'Experimental')
    pyplot.plot(plotdata[0], theoretical_data, color = theoretical_color, label = 'Theoretical')

    pyplot.axis([ 0, xlimit, 0, 25 ])
    pyplot.legend()
    pyplot.title(exp_label + " and " + theoretical_label)
    pyplot.xlabel('N')
    pyplot.ylabel('number of steps')
    pyplot.savefig(exp_label + "_" + theoretical_label + ".png")
