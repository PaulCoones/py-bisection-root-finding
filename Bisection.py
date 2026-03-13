"""This program provides a standalone function bisection(f, a, b, epsilon)
which applies the bisection root finding method to a provided function."""

def bisection(f, a, b, epsilon):
    """
    Returns an approximation to the root of the provided function f up to an
    error tolerance epsilon, given an initial interval [a, b] such that (f(a) * f(b)) <= 0.

    Args:
        f (function): A function whose root is to be approximated
        a (float): The left end of the interval
        b (float): The right end of the interval
        epsilon (float): The error tolerance in the approximation to the root

    Requires:
        b > a
        (f(a) * f(b)) <= 0
        epsilon is positive

    Returns:
       float: An approximation to the root of the function f
    """
    a_i = a
    b_i = b
    while(abs(a_i - b_i) > epsilon):    # Until within epsilon tolerance
        c_i = (a_i + b_i) / 2           # Half the interval
        if (f(c_i) * f(a_i) <= 0):
            b_i = c_i
        else:
            a_i = c_i
    return (a_i + b_i) / 2