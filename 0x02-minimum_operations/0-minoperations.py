#!/usr/bin/python3
"""contains minimum_operations function"""


def minOperations(n):
    """Calculates the fewest number of operations
    needed to result in exactly n H characters"""
    # Initialize operations count
    operations = 0
    current = n

    # Loop from 2 to n to find factors
    for i in range(2, n + 1):
        # Check if i is a factor of current
        while current % i == 0:
            operations += i  # Perform Copy All and i-1 Paste operations
            current //= i    # Reduce current by the factor
    return operations
