# Assignment 0. Python 3.4

def mdc(a: int, b: int) -> int:
    """Returns the MDC between two natural numbers

    This function is an implementation of the Euclid's algorithm to compute the greatest common divisor (GDC) between two natural numbers. This algorithm does not use modular arithmetic so it won't work with negative integers. The name stands for the portuguese version."""

    steps = 0
    while b != 0:
        a, b = b, a%b
        steps += 1
    return a, steps

#script for execution
if __name__ == "__main__":

    n = input("Digite o valor de N: ")
    for limit in range(n):
        run_mdc_with_limits(limit)



def run_mdc_with_limits(limit: int, samples = 100000 ):
    max_steps = 0
    min_steps = -1
    avg_steps = 0
    for i in range(samples):
        a = randrange(1, limit+1)
        b = randrange(1, limit+1)
        res, steps = mdc(a, b)

        max_steps = steps > max_steps ? steps : max_steps
        if steps < min_steps or min_steps == -1:
            min_steps = steps
        avg_steps += steps
    avg_steps /= samples
    with open("steps_data.csv", 'w+') as steps_file:
        line = "{0}, {1}, {2}, {3}".format(limit, min_steps, max_steps, avg_steps)
        steps_file.write(line)
