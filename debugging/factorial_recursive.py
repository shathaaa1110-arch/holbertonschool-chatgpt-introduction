#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer using a recursive approach.

    Parameters:
    n (int): The non-negative integer to compute the factorial of.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = factorial(int(sys.argv[1]))
        print(f)
