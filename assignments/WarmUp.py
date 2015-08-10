

def mdc(a: int, b: int) -> int:
    """Returns the MDC between two natural numbers

    This function is an implementation of the Euclid's algorithm to compute the greatest common divisor (GDC) between two natural numbers. This algorithm does not use modular arithmetic so it won't work with negative integers. The name stands for the portuguese version."""

    while (a - b) != 0:
        if(a > b):
            a, b = b, a-b
        else:
            b = b-a

    return a

#script for execution
if __name__ == "__main__":
    while True:
        a = int( input() )
        b = int( input() )
        if a == '' or b == '':
            break
        print( mdc(a, b) )
