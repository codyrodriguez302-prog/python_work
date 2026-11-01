"""
Math Operations Practice
PCEP Objective: PCEP-30-02 1.4 (operators and data types), 1.3 (literals), 3.1 (lists)
Difficulty: Beginner

DESCRIPTION:
Each function in this file performs one arithmetic or logic operation from the
math warm-up packet. Every function body is one or two lines. There are no loops
and no algorithms to design here -- the goal is to connect a math idea you
already know to the Python operator or built-in function that performs it.

INSTRUCTIONS:
1. Read each function's docstring before writing any code.
2. Replace the 'pass' statement with your implementation. Do not change the
   function names or their parameters.
3. Return the value described. Do not use print() inside these functions.
4. Run this file to check your work. The test section at the bottom reports
   which functions pass.
"""

import math


def quotient_and_remainder(dividend, divisor):
    """
    Split a division into its whole-number quotient and its remainder.

    This demonstrates floor division (//) and modulo (%), the two operators
    that answer "how many whole groups?" and "how much is left over?"

    Parameters:
        dividend (int): The number being divided
        divisor (int): The number to divide by

    Returns:
        tuple: (quotient, remainder), both integers

    Example:
        >>> quotient_and_remainder(17, 5)
        (3, 2)
        >>> quotient_and_remainder(40, 8)
        (5, 0)

    Hint: A tuple is written with a comma: return a, b
    """

    return dividend // divisor, dividend % divisor


def round_to_places(value, places):
    """
    Round a number to a given number of decimal places.

    This demonstrates the round() function's second argument.

    Parameters:
        value (float): The number to round
        places (int): How many decimal places to keep

    Returns:
        float: The rounded number

    Example:
        >>> round_to_places(3.14159, 2)
        3.14
        >>> round_to_places(2.71828, 3)
        2.718

    Note: Python breaks exact ties toward the even neighbor, so round(2.5)
    is 2 and not 3. That is expected behavior, not an error.
    """
    return round(value, places)


def floor_and_ceiling(value):
    """
    Return the integers immediately below and above a decimal number.

    This demonstrates math.floor() and math.ceil(). Remember that floor always
    moves down the number line, so floor(-3.2) is -4, not -3.

    Parameters:
        value (float): Any number

    Returns:
        tuple: (floor_value, ceiling_value), both integers

    Example:
        >>> floor_and_ceiling(6.2)
        (6, 7)
        >>> floor_and_ceiling(-3.2)
        (-4, -3)
    """
    return math.floor(value), math.ceil(value)


def is_even(number):
    """
    Report whether a whole number is even.

    This demonstrates using % together with == to produce a Boolean. Return the
    comparison itself -- you do not need an if statement.

    Parameters:
        number (int): Any whole number

    Returns:
        bool: True if the number is even, False otherwise

    Example:
        >>> is_even(10)
        True
        >>> is_even(7)
        False

    Hint: The expression number % 2 == 0 is already True or False.
    """
    return number % 2 == 0


def in_range(value, low, high):
    """
    Report whether a value falls between two bounds, including the bounds.

    This demonstrates combining two comparisons with the 'and' operator.

    Parameters:
        value (int or float): The number to test
        low (int or float): The lower bound
        high (int or float): The upper bound

    Returns:
        bool: True if low <= value <= high, False otherwise

    Example:
        >>> in_range(15, 10, 20)
        True
        >>> in_range(20, 10, 20)
        True
        >>> in_range(9, 10, 20)
        False
    """
    return low <= value <= high


def greatest_common_factor(a, b):
    """
    Return the largest whole number that divides both inputs evenly.

    This demonstrates math.gcd(). You do not need to write the algorithm.

    Parameters:
        a (int): First whole number
        b (int): Second whole number

    Returns:
        int: The greatest common factor

    Example:
        >>> greatest_common_factor(48, 180)
        12
        >>> greatest_common_factor(35, 64)
        1
    """
    return math.gcd(a, b)


def average(numbers):
    """
    Return the mean of a list of numbers.

    This demonstrates sum() and len(). Because / always produces a float, the
    result is a float even when the numbers divide evenly.

    Parameters:
        numbers (list): A list of numbers with at least one element

    Returns:
        float: The mean of the values

    Example:
        >>> average([2, 4, 4, 10])
        5.0
        >>> average([8, 15, 4, 16, 23, 42])
        18.0
    """
    return sum(numbers) / len(numbers)


def middle_value(numbers):
    """
    Return the median of a list holding an odd number of values.

    This demonstrates sorted() and index arithmetic. The data must be sorted
    before you can take a middle value, and the middle position of a list of
    n items is at index n // 2.

    Parameters:
        numbers (list): A list with an odd number of elements

    Returns:
        The middle value of the sorted list

    Example:
        >>> middle_value([7, 3, 9])
        7
        >>> middle_value([10, 2, 8, 1, 5])
        5

    Hint: Sort the list into a new variable first, then index into it.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    return sorted_numbers[n // 2]


def data_range(numbers):
    """
    Return the spread of a data set: the largest value minus the smallest.

    This demonstrates max() and min().

    Parameters:
        numbers (list): A list of numbers with at least one element

    Returns:
        The difference between the largest and smallest values

    Example:
        >>> data_range([4, 8, 15, 16, 23, 42])
        38
        >>> data_range([7, 7, 7])
        0
    """
    return max(numbers) - min(numbers)


def binary_to_decimal(bits):
    """
    Convert a string of binary digits into its decimal value.

    This demonstrates int() with a base argument. int("1011", 2) reads the
    string as a base-2 numeral rather than a base-10 one.

    Parameters:
        bits (str): A string containing only the characters 0 and 1

    Returns:
        int: The decimal value of that binary numeral

    Example:
        >>> binary_to_decimal("1011")
        11
        >>> binary_to_decimal("100000")
        32
    """
    return int(bits, 2)


# ---------------------------------------------------------------------------
# Test section. Run this file to check your work.
# Do not edit anything below this line.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    passed = 0
    failed = []

    def check(name, actual, expected):
        global passed
        if actual == expected:
            passed += 1
        else:
            failed.append(f"{name}: expected {expected!r}, got {actual!r}")

    check("quotient_and_remainder(17, 5)", quotient_and_remainder(17, 5), (3, 2))
    check("quotient_and_remainder(40, 8)", quotient_and_remainder(40, 8), (5, 0))
    check("quotient_and_remainder(7, 10)", quotient_and_remainder(7, 10), (0, 7))

    check("round_to_places(3.14159, 2)", round_to_places(3.14159, 2), 3.14)
    check("round_to_places(2.71828, 3)", round_to_places(2.71828, 3), 2.718)

    check("floor_and_ceiling(6.2)", floor_and_ceiling(6.2), (6, 7))
    check("floor_and_ceiling(-3.2)", floor_and_ceiling(-3.2), (-4, -3))
    check("floor_and_ceiling(9.0)", floor_and_ceiling(9.0), (9, 9))

    check("is_even(10)", is_even(10), True)
    check("is_even(7)", is_even(7), False)

    check("in_range(15, 10, 20)", in_range(15, 10, 20), True)
    check("in_range(20, 10, 20)", in_range(20, 10, 20), True)
    check("in_range(9, 10, 20)", in_range(9, 10, 20), False)

    check("greatest_common_factor(48, 180)", greatest_common_factor(48, 180), 12)
    check("greatest_common_factor(35, 64)", greatest_common_factor(35, 64), 1)

    check("average([2, 4, 4, 10])", average([2, 4, 4, 10]), 5.0)
    check("average([8, 15, 4, 16, 23, 42])", average([8, 15, 4, 16, 23, 42]), 18.0)

    check("middle_value([7, 3, 9])", middle_value([7, 3, 9]), 7)
    check("middle_value([10, 2, 8, 1, 5])", middle_value([10, 2, 8, 1, 5]), 5)

    check("data_range([4, 8, 15, 16, 23, 42])", data_range([4, 8, 15, 16, 23, 42]), 38)
    check("data_range([7, 7, 7])", data_range([7, 7, 7]), 0)

    check("binary_to_decimal('1011')", binary_to_decimal("1011"), 11)
    check("binary_to_decimal('100000')", binary_to_decimal("100000"), 32)

    total = passed + len(failed)
    print(f"Passed {passed} of {total} checks.")
    if failed:
        print("\nStill to fix:")
        for line in failed:
            print("  " + line)
    else:
        print("All checks passed.")
