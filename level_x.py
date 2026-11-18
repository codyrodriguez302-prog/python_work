"""
DEBUG RELAY 2  -  LEVEL X  (bonus: beyond the PCEP)

These bugs go past the PCEP. Some functions give wrong answers, some run
far too slowly, and some go so many calls deep that Python crashes with a
RecursionError. Each function has exactly ONE problem to fix. The
docstring says what the function must do and how big an input it has to
handle.

SCORING
  Each Level X bug is worth only 3 points (60 points for the file).
  Clear the easier levels first!

CHECK YOUR WORK
  This level:               python3 level_x.py
  Full test for one bug:    python3 level_x.py 7
  Official Level X score:   python3 check_x.py
  Every test has a 2-second time limit, so a full run can take about
  20 seconds while slow bugs are still unfixed.

RULES FOR THIS LEVEL
  - You may rewrite the inside of a function, but keep its name and
    parameters the same.
  - Do not raise Python's recursion limit. If the checker finds code
    that changes it, the whole file scores 0.
  - Do not edit the docstrings or anything below the TEST CASES line.
"""


# =====================================================================
# BUG X-1                                                    3 points
# =====================================================================

def integrate(f, a, b, n):
    """
    Estimate the area under the function f from x = a to x = b using n
    trapezoids of equal width w = (b - a) / n:

        area = w * ( f(x0)/2 + f(x1) + f(x2) + ... + f(x(n-1)) + f(xn)/2 )

    where x0 = a and xn = b. The two end points count HALF.

    Example:
        >>> def line(x):
        ...     return x
        >>> integrate(line, 0, 10, 10)
        50.0
    """
    width = (b - a) / n
    total = 0
    for i in range(n + 1):
        x = a + i * width
        total += f(x)
    return total * width


# =====================================================================
# BUG X-2                                                    3 points
# =====================================================================

def fib(n):
    """
    Return the nth Fibonacci number: fib(0) = 0, fib(1) = 1, and every
    number after that is the sum of the two before it.
    Must handle n up to 300 almost instantly.

    Example:
        >>> fib(10)
        55
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# =====================================================================
# BUG X-3                                                    3 points
# =====================================================================

def sum_of_squares(n):
    """
    Return 1*1 + 2*2 + 3*3 + ... + n*n. n can be as big as 100,000.

    Example:
        >>> sum_of_squares(3)
        14
    """
    
    if n == 0:
        return 0
    return n * n + sum_of_squares(n + 1)


# =====================================================================
# BUG X-4                                                    3 points
# =====================================================================

def luhn_valid(number_text):
    """
    Luhn check (used on credit cards and ID numbers). Ignore spaces.
    Starting from the RIGHTMOST digit, double every second digit (the 2nd,
    4th, 6th... digit counting from the right). If doubling gives more
    than 9, subtract 9. Add up all the digits. The number is valid if the
    total ends in 0.

    Example:
        >>> luhn_valid("7992 7398 713")
        True
        >>> luhn_valid("4111 1111 1111 1111")
        True
    """
    digits = number_text.replace(" ", "")
    total = 0
    for i in range(len(digits)):
        d = int(digits[i])
        if i % 2 == 1:
            d = d * 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


# =====================================================================
# BUG X-5                                                    3 points
# =====================================================================

def count_primes(n):
    """
    Return how many prime numbers are less than or equal to n.
    Must handle n = 100,000 in about a second or less.

    Example:
        >>> count_primes(10)
        4
    """
    count = 0
    for k in range(2, n + 1):
        is_prime = True
        for d in range(2, k):
            if k % d == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count


# =====================================================================
# BUG X-6                                                    3 points
# =====================================================================

def prime_factors(n):
    """
    Return the prime factors of n (n >= 1) from smallest to largest,
    repeated as many times as they divide n. 1 has no prime factors.

    Example:
        >>> prime_factors(12)
        [2, 2, 3]
        >>> prime_factors(600851475143)
        [71, 839, 1471, 6857]
    """
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    return factors


# =====================================================================
# BUG X-7                                                    3 points
# =====================================================================

def has_duplicate(items):
    """
    Return True if any value appears more than once in the list.
    Must handle a list of 50,000 items almost instantly.

    Example:
        >>> has_duplicate([3, 1, 4, 1])
        True
    """
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False


# =====================================================================
# BUG X-8                                                    3 points
# =====================================================================

def gcd_big(a, b):
    """
    RECURSIVE: return the greatest common divisor of two non-negative
    whole numbers. Must work for numbers up to 10**12.

    Example:
        >>> gcd_big(48, 18)
        6
    """
    if b == 0:
        return a
    if a == 0:
        return b
    if a > b:
        return gcd_big(a - b, b)
    return gcd_big(a, b - a)


# =====================================================================
# BUG X-9                                                    3 points
# =====================================================================

def day_of_week(year, month, day):
    """
    Return the weekday name for a date using Zeller's congruence.
    January and February count as months 13 and 14 of the PREVIOUS year.
    Then, with q = day, m = month, K = year % 100, J = year // 100:

        h = (q + 13 * (m + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

    h = 0 is Saturday, 1 Sunday, 2 Monday, ... 6 Friday.

    Example:
        >>> day_of_week(2026, 10, 30)
        'Friday'
    """
    names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    if month < 3:
        month += 12
    K = year % 100
    J = year // 100
    h = (day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    return names[h]


# =====================================================================
# BUG X-10                                                   3 points
# =====================================================================

def power_mod(base, exponent, modulus):
    """
    Return (base to the power exponent) % modulus. exponent can be as big
    as 10**18, and the answer must come back almost instantly.

    Hint: base**8 = ((base**2)**2)**2, so squaring repeatedly reaches huge
    powers in very few steps. Keep every number small with % as you go.

    Example:
        >>> power_mod(2, 10, 1000)
        24
    """
    result = 1
    for i in range(exponent):
        result = (result * base) % modulus
    return result


# =====================================================================
# BUG X-11                                                   3 points
# =====================================================================

def gcd_pair(a, b):
    """HELPER - this function has no bug. Greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a


def lcm_list(numbers):
    """
    Return the least common multiple of a list of positive whole numbers:
    the smallest number every one of them divides evenly.

    Example:
        >>> lcm_list([4, 6])
        12
        >>> lcm_list([2, 3, 4])
        12
    """
    product = 1
    common = 0
    for n in numbers:
        product *= n
        common = gcd_pair(common, n)
    return product // common


# =====================================================================
# BUG X-12                                                   3 points
# =====================================================================

def median(values):
    """
    Return the median of a list of numbers: the middle value after
    sorting, or the average of the two middle values if the count is
    even. The original list must not change.
    Must handle 50,000 numbers almost instantly.

    Example:
        >>> median([3, 1, 2])
        2
        >>> median([4, 1, 3, 2])
        2.5
    """
    data = values[:]
    for i in range(len(data)):
        smallest = i
        for j in range(i + 1, len(data)):
            if data[j] < data[smallest]:
                smallest = j
        data[i], data[smallest] = data[smallest], data[i]
    middle = len(data) // 2
    if len(data) % 2 == 1:
        return data[middle]
    return (data[middle - 1] + data[middle]) / 2


# =====================================================================
# BUG X-13                                                   3 points
# =====================================================================

def flood_fill_size(grid, row, col):
    """
    grid is a list of strings where "." is open floor and "#" is a wall.
    Return how many open cells can be reached from (row, col) moving up,
    down, left, or right (0 if that cell is a wall). Must work on grids as
    big as 80 x 80.

    Example:
        >>> flood_fill_size(["..#", ".##", "..."], 0, 0)
        6
    """
    rows = len(grid)
    cols = len(grid[0])
    seen = set()

    def visit(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != "." or (r, c) in seen:
            return
        seen.add((r, c))
        visit(r + 1, c)
        visit(r - 1, c)
        visit(r, c + 1)
        visit(r, c - 1)

    visit(row, col)
    return len(seen)


# =====================================================================
# BUG X-14                                                   3 points
# =====================================================================

def newton_sqrt(x):
    """
    Estimate the square root of x (x >= 0) with Newton's method, rounded
    to 6 decimals. Start with guess = x (or 1 if x < 1), then 50 times:
        new guess = the average of guess and x / guess

    Example:
        >>> newton_sqrt(2)
        1.414214
    """
    if x == 0:
        return 0.0
    guess = x
    if x < 1:
        guess = 1
    for i in range(50):
        guess = (guess + x / guess) // 2
    return round(guess, 6)


# =====================================================================
# BUG X-15                                                   3 points
# =====================================================================

def grid_paths(rows, cols):
    """
    A robot starts at the top-left corner of a grid and may only move
    RIGHT or DOWN. Return how many different routes reach the corner that
    is `rows` steps down and `cols` steps right.
    Must handle 30 x 30 almost instantly.

    Example:
        >>> grid_paths(2, 2)
        6
    """
    if rows == 0 or cols == 0:
        return 1
    return grid_paths(rows - 1, cols) + grid_paths(rows, cols - 1)


# =====================================================================
# BUG X-16                                                   3 points
# =====================================================================

def pascal_row(n):
    """
    Return row n of Pascal's triangle as a list of EXACT whole numbers
    (row 0 is [1], row 4 is [1, 4, 6, 4, 1]). Each entry comes from the
    one before it: next = current * (n - k) / (k + 1). Must be exact for
    rows as big as 60.

    Example:
        >>> pascal_row(4)
        [1, 4, 6, 4, 1]
    """
    row = [1]
    value = 1
    for k in range(n):
        value = value * (n - k) / (k + 1)
        row.append(value)
    return row


# =====================================================================
# BUG X-17                                                   3 points
# =====================================================================

def count_pairs_with_sum(numbers, target):
    """
    Count the pairs of positions (i, j) with i < j where
    numbers[i] + numbers[j] == target.
    Must handle 50,000 numbers almost instantly.

    Example:
        >>> count_pairs_with_sum([1, 4, 3, 2], 5)
        2
    """
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                count += 1
    return count


# =====================================================================
# BUG X-18                                                   3 points
# =====================================================================

def matrix_multiply(A, B):
    """
    Multiply matrix A (r x m) by matrix B (m x c). Entry [i][j] of the
    answer is the sum of A[i][k] * B[k][j] for every k.

    Example:
        >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
    """
    rows = len(A)
    cols = len(B[0])
    inner = len(B)
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            total = 0
            for k in range(inner):
                total += A[i][k] * B[j][k]
            row.append(total)
        result.append(row)
    return result


# =====================================================================
# BUG X-19                                                   3 points
# =====================================================================

def is_perfect(n):
    """
    A perfect number equals the sum of its divisors smaller than itself
    (6 = 1 + 2 + 3). Return True if n is perfect.
    Must handle n up to 10 billion in about a second.

    Example:
        >>> is_perfect(28)
        True
        >>> is_perfect(12)
        False
    """
    if n < 2:
        return False
    total = 0
    for d in range(1, n):
        if n % d == 0:
            total += d
    return total == n


# =====================================================================
# BUG X-20                                                   3 points
# =====================================================================

def is_perfect_square(n):
    """
    Return True if n is the square of a whole number. Must be exactly
    right even for numbers with 30+ digits. Negative numbers return False.

    Example:
        >>> is_perfect_square(16)
        True
        >>> is_perfect_square(15)
        False
    """
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n


# =====================================================================
#  TEST CASES  -  DO NOT EDIT ANYTHING BELOW THIS LINE
# =====================================================================

import io
import signal
import sys

TESTS = [
    # (bug number, function name, points, [(test, expected answer), ...])
    (1, 'integrate', 3, [
        ('integrate(_line, 0, 10, 10)', 50.0),
        ('round(integrate(_square, 0, 3, 1000), 3)', 9.0),
        ('integrate(_line, 2, 2, 5)', 0.0),
    ]),
    (2, 'fib', 3, [
        ('fib(10)', 55),
        ('fib(0)', 0),
        ('fib(90)', 2880067194370816120),
        ('fib(300)', 222232244629420445529739893461909967206666939096499764990979600),
    ]),
    (3, 'sum_of_squares', 3, [
        ('sum_of_squares(3)', 14),
        ('sum_of_squares(0)', 0),
        ('sum_of_squares(100000)', 333338333350000),
    ]),
    (4, 'luhn_valid', 3, [
        ("luhn_valid('7992 7398 713')", True),
        ("luhn_valid('4111 1111 1111 1111')", True),
        ("luhn_valid('1234 5678 1234 5670')", True),
        ("luhn_valid('1234 5678')", False),
    ]),
    (5, 'count_primes', 3, [
        ('count_primes(10)', 4),
        ('count_primes(1)', 0),
        ('count_primes(2)', 1),
        ('count_primes(100000)', 9592),
    ]),
    (6, 'prime_factors', 3, [
        ('prime_factors(12)', [2, 2, 3]),
        ('prime_factors(600851475143)', [71, 839, 1471, 6857]),
        ('prime_factors(97)', [97]),
        ('prime_factors(1)', []),
    ]),
    (7, 'has_duplicate', 3, [
        ('has_duplicate([3, 1, 4, 1])', True),
        ('has_duplicate([])', False),
        ('has_duplicate(list(range(50000)))', False),
        ('has_duplicate(list(range(50000)) + [49999])', True),
    ]),
    (8, 'gcd_big', 3, [
        ('gcd_big(48, 18)', 6),
        ('gcd_big(7, 0)', 7),
        ('gcd_big(0, 9)', 9),
        ('gcd_big(1000000, 3)', 1),
        ('gcd_big(10 ** 12, 4 * 10 ** 9)', 4000000000),
    ]),
    (9, 'day_of_week', 3, [
        ('day_of_week(2026, 10, 30)', 'Friday'),
        ('day_of_week(2026, 1, 1)', 'Thursday'),
        ('day_of_week(2000, 2, 29)', 'Tuesday'),
        ('day_of_week(1969, 7, 20)', 'Sunday'),
    ]),
    (10, 'power_mod', 3, [
        ('power_mod(2, 10, 1000)', 24),
        ('power_mod(3, 0, 7)', 1),
        ('power_mod(5, 10 ** 18, 1000000007)', 921116510),
        ('power_mod(7, 123456789012345, 97)', 42),
    ]),
    (11, 'lcm_list', 3, [
        ('lcm_list([4, 6])', 12),
        ('lcm_list([2, 3, 4])', 12),
        ('lcm_list(list(range(1, 11)))', 2520),
        ('lcm_list([5])', 5),
    ]),
    (12, 'median', 3, [
        ('median([3, 1, 2])', 2),
        ('median([4, 1, 3, 2])', 2.5),
        ('median(list(range(50000, 0, -1)))', 25000.5),
    ]),
    (13, 'flood_fill_size', 3, [
        ("flood_fill_size(['..#', '.##', '...'], 0, 0)", 6),
        ("flood_fill_size(['#'], 0, 0)", 0),
        ('flood_fill_size(_open_grid(80), 0, 0)', 6400),
        ('flood_fill_size(_open_grid(80), 40, 40)', 6400),
    ]),
    (14, 'newton_sqrt', 3, [
        ('newton_sqrt(2)', 1.414214),
        ('newton_sqrt(16)', 4.0),
        ('newton_sqrt(0)', 0.0),
        ('newton_sqrt(0.25)', 0.5),
        ('newton_sqrt(1000)', 31.622777),
    ]),
    (15, 'grid_paths', 3, [
        ('grid_paths(2, 2)', 6),
        ('grid_paths(3, 0)', 1),
        ('grid_paths(16, 16)', 601080390),
        ('grid_paths(30, 30)', 118264581564861424),
    ]),
    (16, 'pascal_row', 3, [
        ('pascal_row(4)', [1, 4, 6, 4, 1]),
        ('pascal_row(0)', [1]),
        ('pascal_row(60)[30]', 118264581564861424),
        ('isinstance(pascal_row(5)[2], int)', True),
    ]),
    (17, 'count_pairs_with_sum', 3, [
        ('count_pairs_with_sum([1, 4, 3, 2], 5)', 2),
        ('count_pairs_with_sum([5, 5, 5], 10)', 3),
        ('count_pairs_with_sum([], 1)', 0),
        ('count_pairs_with_sum(list(range(50000)), 49999)', 25000),
    ]),
    (18, 'matrix_multiply', 3, [
        ('matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])', [[19, 22], [43, 50]]),
        ('matrix_multiply([[1, 2, 3]], [[1], [2], [3]])', [[14]]),
        ('matrix_multiply([[2, 0], [0, 2]], [[1, 2], [2, 1]])', [[2, 4], [4, 2]]),
    ]),
    (19, 'is_perfect', 3, [
        ('is_perfect(6)', True),
        ('is_perfect(12)', False),
        ('is_perfect(1)', False),
        ('is_perfect(8589869056)', True),
    ]),
    (20, 'is_perfect_square', 3, [
        ('is_perfect_square(16)', True),
        ('is_perfect_square(15)', False),
        ('is_perfect_square(0)', True),
        ('is_perfect_square((10 ** 17 + 3) ** 2)', True),
        ('is_perfect_square(-4)', False),
    ]),
]


def _line(x):
    return x


def _square(x):
    return x * x


def _open_grid(size):
    return ["." * size] * size


def printed(func, *args):
    """Run func(*args) and return everything it printed, as one string."""
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        func(*args)
        text = sys.stdout.getvalue()
    finally:
        sys.stdout = saved
    return text


TIME_LIMIT = 2  # seconds per test


class TooSlow(Exception):
    pass


def _alarm(signum, frame):
    raise TooSlow("took longer than " + str(TIME_LIMIT) + " seconds")


def check_bug(cases):
    """Return None if every test passes, otherwise (test, expected, got)."""
    use_alarm = hasattr(signal, "SIGALRM")
    if use_alarm:
        signal.signal(signal.SIGALRM, _alarm)
    for expression, expected in cases:
        try:
            if use_alarm:
                signal.alarm(TIME_LIMIT)
            result = eval(expression)
            if use_alarm:
                signal.alarm(0)
            if result == expected:
                continue
            got = repr(result)
        except Exception as error:
            if use_alarm:
                signal.alarm(0)
            got = "ERROR -> " + type(error).__name__ + ": " + str(error)
        return (expression, repr(expected), got)
    return None


def short(text, size):
    if len(text) > size:
        return text[:size - 3] + "..."
    return text


def run_tests(only):
    fixed = 0
    points = 0
    possible = 0
    print("=" * 70)
    print("  DEBUG RELAY 2  -  LEVEL X   (3 points per bug)")
    print("=" * 70)
    if not hasattr(signal, "SIGALRM"):
        print("  NOTE: time limits only work on Linux/macOS. A slow bug may hang here;")
        print("  press Ctrl+C to stop it.")
    for number, name, value, cases in TESTS:
        possible += value
        if only and number not in only:
            continue
        failure = check_bug(cases)
        if failure is None:
            fixed += 1
            points += value
        label = "Bug X-" + str(number).ljust(3) + " " + name.ljust(24)
        if failure is None:
            print(label + "FIXED")
        elif only:
            print(label + "not fixed")
            print("         test:      " + failure[0])
            print("         expected:  " + short(failure[1], 50))
            print("         got:       " + short(failure[2], 50))
        else:
            print(label + "not fixed")
            print("         expected " + short(failure[1], 24) +
                  "   got " + short(failure[2], 30))
    print("-" * 70)
    if only:
        print("  Checked only bug(s): " + ", ".join(str(n) for n in only))
    else:
        print("  Level X:  bugs fixed " + str(fixed) + " / " + str(len(TESTS)) +
              "      points " + str(points) + " / " + str(possible))
    print("-" * 70)
    if not only:
        print("  Full test for one bug:   python3 level_x.py 7")
        print("  Official Level X score:  python3 check_x.py")


if __name__ == "__main__":
    chosen = []
    for arg in sys.argv[1:]:
        if arg.isdigit():
            chosen.append(int(arg))
    run_tests(chosen)
