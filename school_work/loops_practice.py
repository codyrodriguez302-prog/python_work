"""
Loops Practice: for and while
PCEP Objective: PCEP-30-02 2.2 (Loops and Iterations)
Difficulty: Beginner

DESCRIPTION:
This assignment practices the two loop types in Python: the for loop (repeat a
known number of times, or once per item) and the while loop (repeat as long as
a condition is True). The first two functions are class walkthroughs. The last
four are yours to complete on your own.

LEARNING OBJECTIVES:
- Use a for loop with range() to repeat an action a set number of times
- Use a while loop that updates its own condition so it eventually stops
- Use an accumulator variable (a running total, counter, or string)
- Iterate over a list with a for loop
- Nest one for loop inside another

EXPECTED OUTCOMES:
After completing this assignment, students will be able to:
- Choose between a for loop and a while loop for a given problem
- Trace a loop by hand and predict how many times it runs
- Avoid infinite loops by changing the loop variable inside a while loop
- Build output row by row with nested loops

INSTRUCTIONS:
1. Functions 1 and 2 are INSTRUCTOR WALKTHROUGHS. Leave them blank until we
   complete them together as a class.
2. Functions 3-6 are INDEPENDENT PRACTICE. Read each docstring carefully.
3. Replace each `pass` with your code. Do not change the function names.
4. Run this file. The tests at the bottom print PASS or FAIL for each function.
5. All tests should pass before you submit.
"""


# ============================================================================
# PART 1: INSTRUCTOR WALKTHROUGHS (complete together as a class)
# ============================================================================

def sum_range(start, end):
    """
    WALKTHROUGH 1 - FOR LOOP

    Add up every whole number from start to end, INCLUDING both start and end.

    Parameters:
        start (int): The first number to add
        end (int): The last number to add (end >= start)

    Returns:
        int: The total of all numbers from start through end

    Example:
        >>> sum_range(1, 5)
        15
        >>> sum_range(3, 3)
        3
        >>> sum_range(10, 12)
        33
    """
    total=0
    for num in range(start, end + 1):
        total += num
    return total


def countdown(n):
    """
    WALKTHROUGH 2 - WHILE LOOP

    Build a countdown string from n down to 1, separated by spaces,
    followed by the word "Liftoff!".

    Parameters:
        n (int): The number to count down from (n >= 0)

    Returns:
        str: The countdown text

    Example:
        >>> countdown(5)
        '5 4 3 2 1 Liftoff!'
        >>> countdown(1)
        '1 Liftoff!'
        >>> countdown(0)
        'Liftoff!'
    """
    result = ""
    current = n
    
    while current > 0:
        result += str(current) + " "
        current -= 1
        
    result += "Liftoff!"
    return result


# ============================================================================
# PART 2: INDEPENDENT PRACTICE
# ============================================================================

def count_digits(number):
    """
    PRACTICE 3 - WHILE LOOP

    Count how many digits are in a positive whole number WITHOUT converting
    it to a string. Use a while loop and integer division (//) to "chop off"
    the last digit each time through the loop.

    Parameters:
        number (int): A whole number (number >= 0)

    Returns:
        int: How many digits the number has

    Example:
        >>> count_digits(7)
        1
        >>> count_digits(4052)
        4
        >>> count_digits(0)
        1

    Hint: 4052 // 10 is 405. How many times can you do that before you hit 0?
          Watch out for 0 - it still has one digit.
    """
    if number == 0:
        return 1
    
    count = 0
    while number > 0:
        number = number // 10  # Chop off the last digit
        count += 1
        
    return count


def collatz_steps(n):
    """
    PRACTICE 4 - WHILE LOOP

    The Collatz rule: if n is even, divide it by 2. If n is odd, multiply it
    by 3 and add 1. Keep applying the rule until n becomes 1.
    Return how many steps it took to reach 1.

    Parameters:
        n (int): A starting number (n >= 1)

    Returns:
        int: The number of steps needed to reach 1

    Example:
        >>> collatz_steps(1)
        0
        >>> collatz_steps(6)
        8
        >>> collatz_steps(7)
        16

    Trace for 6:  6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1   (8 steps)

    Hint: You don't know ahead of time how many steps it will take.
          That is exactly why this is a while loop, not a for loop.
          Use // (not /) so n stays an int.
    """
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
        
    return steps


def find_largest(numbers):
    """
    PRACTICE 5 - FOR LOOP (with a list)

    Find the largest number in a list WITHOUT using the built-in max()
    function or sort(). Use a for loop to look at each number one at a time.

    Parameters:
        numbers (list): A list of numbers with at least one item

    Returns:
        int or float: The largest value in the list

    Example:
        >>> find_largest([4, 17, 9, 2])
        17
        >>> find_largest([-8, -3, -12])
        -3
        >>> find_largest([42])
        42

    Hint: Start by assuming the FIRST number is the largest. Then loop through
          the list and replace your "largest so far" whenever you find a
          bigger number. (Why is starting at 0 a bad idea? Look at example 2.)
    """
    largest = numbers[0]
    
    for num in numbers:
        if num > largest:
            largest = num
            
    return largest


def star_triangle(rows):
    """
    PRACTICE 6 - NESTED FOR LOOP

    Build a right triangle of stars. Row 1 has 1 star, row 2 has 2 stars,
    and so on. Put a newline character "\\n" between rows (but NOT after
    the last row).

    You MUST use a nested for loop: the outer loop picks the row, and the
    inner loop adds one star at a time. Do NOT use string multiplication
    like "*" * 3.

    Parameters:
        rows (int): How many rows to draw (rows >= 1)

    Returns:
        str: The triangle as a single string

    Example:
        >>> star_triangle(1)
        '*'
        >>> star_triangle(3)
        '*\\n**\\n***'
        >>> print(star_triangle(4))
        *
        **
        ***
        ****

    Hint: Outer loop: for row in range(1, rows + 1)
          Inner loop: how many stars belong on this row?
          Add the "\\n" only when you are NOT on the last row.
    """
    result = ""
    
    for row in range(1, rows + 1):
        # Outer loop chooses the current row
        for star in range(row):
            # Inner loop adds one star at a time
            result += "*"
            
        # Add a newline character after every row EXCEPT the last one
        if row < rows:
            result += "\n"
            
    return result


# ============================================================================
# TESTS - Run this file to check your work. Do not edit below this line.
# ============================================================================

def check(name, actual, expected):
    """Print PASS or FAIL for a single test."""
    if actual == expected:
        print(f"  PASS  {name}")
        return True
    print(f"  FAIL  {name}  ->  expected {expected!r}, got {actual!r}")
    return False


if __name__ == "__main__":
    results = []

    print("\nWalkthrough 1: sum_range")
    results.append(check("sum_range(1, 5)", sum_range(1, 5), 15))
    results.append(check("sum_range(3, 3)", sum_range(3, 3), 3))
    results.append(check("sum_range(10, 12)", sum_range(10, 12), 33))

    print("\nWalkthrough 2: countdown")
    results.append(check("countdown(5)", countdown(5), "5 4 3 2 1 Liftoff!"))
    results.append(check("countdown(1)", countdown(1), "1 Liftoff!"))
    results.append(check("countdown(0)", countdown(0), "Liftoff!"))

    print("\nPractice 3: count_digits")
    results.append(check("count_digits(7)", count_digits(7), 1))
    results.append(check("count_digits(4052)", count_digits(4052), 4))
    results.append(check("count_digits(0)", count_digits(0), 1))
    results.append(check("count_digits(1000000)", count_digits(1000000), 7))

    print("\nPractice 4: collatz_steps")
    results.append(check("collatz_steps(1)", collatz_steps(1), 0))
    results.append(check("collatz_steps(6)", collatz_steps(6), 8))
    results.append(check("collatz_steps(7)", collatz_steps(7), 16))
    results.append(check("collatz_steps(27)", collatz_steps(27), 111))

    print("\nPractice 5: find_largest")
    results.append(check("find_largest([4, 17, 9, 2])", find_largest([4, 17, 9, 2]), 17))
    results.append(check("find_largest([-8, -3, -12])", find_largest([-8, -3, -12]), -3))
    results.append(check("find_largest([42])", find_largest([42]), 42))
    results.append(check("find_largest([3, 3, 1])", find_largest([3, 3, 1]), 3))

    print("\nPractice 6: star_triangle")
    results.append(check("star_triangle(1)", star_triangle(1), "*"))
    results.append(check("star_triangle(3)", star_triangle(3), "*\n**\n***"))
    results.append(check("star_triangle(4)", star_triangle(4), "*\n**\n***\n****"))

    passed = results.count(True)
    print(f"\n{passed} / {len(results)} tests passed.")
    if passed == len(results):
        print("All tests passed - nice work!")
