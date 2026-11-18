"""
DEBUG RELAY 2  -  CHECK LEVEL X

Runs the official tests for level_x.py and prints the Level X score
(3 points per bug, 60 points total). Each test has a 2-second time limit.

    python3 check_x.py            score level_x.py in this folder
    python3 check_x.py -v         also list every bug
    python3 check_x.py team1 team2    (instructors) score team folders

The file scores 0 if it changes Python's recursion limit.
"""

import importlib.util
import os
import signal
import sys

TESTS_X = [
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

HELPERS_X = 'def _line(x):\n    return x\n\n\ndef _square(x):\n    return x * x\n\n\ndef _open_grid(size):\n    return ["." * size] * size'

LEVEL_X = ('X', 'level_x.py', TESTS_X, HELPERS_X, 2)

PRINTED = 'import io\nimport sys\n\ndef printed(func, *args):\n    """Run func(*args) and return everything it printed, as one string."""\n    saved = sys.stdout\n    sys.stdout = io.StringIO()\n    try:\n        func(*args)\n        text = sys.stdout.getvalue()\n    finally:\n        sys.stdout = saved\n    return text'


class TestTimeout(Exception):
    pass


def _alarm(signum, frame):
    raise TestTimeout("time limit")


LOAD_COUNT = [0]


def load(path):
    LOAD_COUNT[0] += 1
    spec = importlib.util.spec_from_file_location("relay_file_" + str(LOAD_COUNT[0]), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def grade_level(folder, level):
    """Return (list of (number, name, points, passed), problem message or None)."""
    label, filename, tests, helpers, limit = level
    path = os.path.join(folder, filename)
    results = [(t[0], t[1], t[2], False) for t in tests]
    if not os.path.exists(path):
        return results, "file not found"
    with open(path) as source:
        if "setrecursionlimit" in source.read():
            return results, "uses setrecursionlimit, which is not allowed - file scores 0"
    try:
        module = load(path)
    except Exception as error:
        return results, "file would not run -> " + type(error).__name__ + ": " + str(error)
    sys.setrecursionlimit(1000)
    space = module.__dict__
    exec(PRINTED, space)
    if helpers:
        exec(helpers, space)
    use_alarm = hasattr(signal, "SIGALRM")
    if use_alarm:
        signal.signal(signal.SIGALRM, _alarm)
    results = []
    for number, name, value, cases in tests:
        ok = True
        for expression, expected in cases:
            try:
                if use_alarm:
                    signal.alarm(limit)
                if eval(expression, space) != expected:
                    ok = False
            except KeyboardInterrupt:
                raise
            except BaseException:
                ok = False
            finally:
                if use_alarm:
                    signal.alarm(0)
            if not ok:
                break
        results.append((number, name, value, ok))
    return results, None


def grade_folder(folder, levels, title, verbose):
    print()
    print("=" * 70)
    print("  " + title + "   (" + os.path.abspath(folder) + ")")
    print("=" * 70)
    total_fixed = 0
    total_points = 0
    total_possible = 0
    total_bugs = 0
    for level in levels:
        label, filename = level[0], level[1]
        results, problem = grade_level(folder, level)
        fixed = 0
        points = 0
        possible = 0
        for number, name, value, ok in results:
            possible += value
            if ok:
                fixed += 1
                points += value
        total_fixed += fixed
        total_points += points
        total_possible += possible
        total_bugs += len(results)
        print("  Level " + label + "  " + filename.ljust(16) +
              ("bugs fixed " + str(fixed) + " / " + str(len(results))).ljust(22) +
              "points " + str(points).rjust(3) + " / " + str(possible))
        if problem:
            print("           ** " + problem)
        if verbose:
            for number, name, value, ok in results:
                print("           " + label + "-" + str(number).ljust(3) + name.ljust(24) +
                      ("FIXED" if ok else "-"))
    if len(levels) > 1:
        print("-" * 70)
        print("  TOTAL                   " +
              ("bugs fixed " + str(total_fixed) + " / " + str(total_bugs)).ljust(22) +
              "points " + str(total_points).rjust(3) + " / " + str(total_possible))
    print("-" * 70)
    return (folder, total_fixed, total_points)


def leaderboard(scores):
    scores.sort(key=lambda s: (-s[2], -s[1], s[0]))
    print()
    print("=" * 70)
    print("  LEADERBOARD")
    print("=" * 70)
    place = 0
    for folder, fixed, points in scores:
        place += 1
        print("  " + str(place).rjust(2) + ".  " + folder.ljust(30) + str(points).rjust(4) +
              " points   (" + str(fixed) + " bugs fixed)")


if __name__ == "__main__":
    args = sys.argv[1:]
    verbose = "-v" in args
    folders = [a for a in args if a != "-v"]
    if not folders:
        folders = [os.path.dirname(os.path.abspath(__file__))]
    if not hasattr(signal, "SIGALRM"):
        print("NOTE: time limits only work on Linux/macOS; a slow bug may hang (Ctrl+C stops it).")
    scores = []
    for folder in folders:
        scores.append(grade_folder(folder, [LEVEL_X], "DEBUG RELAY 2  -  LEVEL X SCORE", verbose))
    if len(scores) > 1:
        leaderboard(scores)
