# Assignment 0. Python 3.4

from random import randrange

def mdc(a: int, b: int) -> int:
    """Returns the MDC between two natural numbers

    This function is an implementation of the Euclid's algorithm to compute the greatest common divisor (GDC) between two natural numbers. This algorithm does not use modular arithmetic so it won't work with negative integers. The name stands for the portuguese version."""

    steps = 0
    while b != 0:
        a, b = b, a%b
        steps += 1
    return a, steps

def run_mdc_with_limits_randomly(limit: int, filename = 'steps_data.csv' , samples = 1000000 ):
    max_steps = 0
    min_steps = -1
    avg_steps = 0
    for i in range(samples):
        a = randrange(1, limit+1)
        b = randrange(1, limit+1)
        res, steps = mdc(a, b)

        if steps > max_steps:
            max_steps = steps
        if steps < min_steps or min_steps == -1:
            min_steps = steps
        avg_steps += steps
    avg_steps /= samples
    with open(filename, 'a+') as steps_file:
        line = "{0}, {1}, {2}, {3}\n".format(limit, min_steps, max_steps, avg_steps)
        steps_file.write(line)


def run_mdc_with_limits(limit: int, filename = 'allcombinations_data.csv' ):
    max_steps = 0
    min_steps = -1
    avg_steps = 0
    worst_case = []
    counter = 0
    for a in range(1, limit+1):
        for b in range(1, a+1):
            res, steps = mdc(a, b)
            counter += 1
            if steps > max_steps:
                max_steps = steps
                worst_case = [a, b]
            if steps < min_steps or min_steps == -1:
                min_steps = steps
            avg_steps += steps
    avg_steps /= counter
    with open(filename, 'a+') as steps_file:
        line = "{0}, {1}, {2}, {3}\n".format(a, min_steps, max_steps, avg_steps)
        steps_file.write(line)
    with open('worst_case.csv', 'a+') as worst_case_file:
        worst_case_file.write("{0}, {1}, {2}\n".format(a, worst_case[0], worst_case[1] ) )

#script for execution
if __name__ == "__main__":
    n = int(input("Digite o valor de N: "))
    for limit in range(1, n+1):
        run_mdc_with_limits(limit)
        print("iteracao: ", limit)
