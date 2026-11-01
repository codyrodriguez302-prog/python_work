
"""
Lists in Lists: Matrices and Cubes - Independent Practice
PCEP Objective: PCEP-30-02 3.1 (lists in lists: matrices and cubes)
Difficulty: Intermediate (Function 5 is an Advanced challenge)

DESCRIPTION:
Practice on your own what we did together in the Matrix Lab. Functions 1-4
work with 2D grids (matrices). Function 5 is the 3D challenge: a parking
garage stored as a cube - a list of floors, where each floor is a grid.

LEARNING OBJECTIVES:
- Build a 2D list where every row is a separate list
- Traverse a matrix by column and search it with nested loops
- Return a transformed copy of a matrix without changing the original
- Index and traverse a 3D list with three nested loops

EXPECTED OUTCOMES:
After completing this assignment, students will be able to:
- Explain why [[0] * cols] * rows is a bug and build grids correctly
- Use grid[row][col] and cube[layer][row][col] indexing with confidence
- Choose the right loop order for row, column, and layer traversals

INSTRUCTIONS:
1. Read each function's docstring carefully
2. Replace each `pass` with your code (do not rename the functions)
3. Run the file - the tests at the bottom check each function
4. Keep going until every function shows [PASS]
"""


def make_grid(rows, cols, fill):
    """
    Build and return a new grid (2D list) with `rows` rows and `cols`
    columns, where every cell holds `fill`.

    Every row must be its own separate list. Changing one cell must
    NOT change any other row.

    Parameters:
        rows (int): number of rows (0 or more)
        cols (int): number of columns (0 or more)
        fill: the value to put in every cell

    Returns:
        list: a list of `rows` lists, each with `cols` items

    Example:
        >>> make_grid(2, 3, 0)
        [[0, 0, 0], [0, 0, 0]]
        >>> make_grid(3, 2, '-')
        [['-', '-'], ['-', '-'], ['-', '-']]
        >>> make_grid(0, 4, 0)
        []

    Hint: [[fill] * cols] * rows looks right but is a trap. Why?
    """
    grid = []

    for row in range(rows):
        new_row = [fill] * cols
        grid.append(new_row)

    return grid



def column_totals(grid):
    """
    Return a list with the total of each column in the grid.

    Think of a gradebook: each row is a student, each column is an
    assignment. Column totals add DOWN each column.

    Parameters:
        grid (list): a rectangular 2D list of numbers with at least
                     one row and one column

    Returns:
        list: one total per column, left to right

    Example:
        >>> column_totals([[1, 2, 3],
        ...                [4, 5, 6]])
        [5, 7, 9]
        >>> column_totals([[10], [20], [30]])
        [60]

    Hint: the number of columns is len(grid[0]).
    """
    totals = []

    for col in range(len(grid[0])):
        total = 0

        for row in range(len(grid)):
            total += grid[row][col]

        totals.append(total)

    return totals



def find_value(grid, target):
    """
    Search the grid row by row (top to bottom, left to right) and
    return the position of the FIRST cell equal to `target`.

    Parameters:
        grid (list): a 2D list
        target: the value to look for

    Returns:
        tuple: (row, col) of the first match
        None: if the target is not in the grid

    Example:
        >>> seats = [['A', 'B', 'C'],
        ...          ['D', 'X', 'F'],
        ...          ['X', 'H', 'I']]
        >>> find_value(seats, 'X')
        (1, 1)
        >>> find_value(seats, 'Z') is None
        True

    Hint: use range(len(...)) in both loops so you know the indexes.
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            if grid[row][col] == target:
                return (row, col)

    return None


def flip_upside_down(grid):
    """
    Return a NEW grid with the rows in reverse order (top row becomes
    the bottom row).

    The original grid must not change, AND the new grid must not share
    row lists with the original. Changing new_grid[0][0] should never
    change anything in `grid`.

    Parameters:
        grid (list): a 2D list

    Returns:
        list: a new 2D list, rows reversed, every row a copy

    Example:
        >>> flip_upside_down([[1, 2],
        ...                   [3, 4],
        ...                   [5, 6]])
        [[5, 6], [3, 4], [1, 2]]

    Hint: grid[::-1] reverses the rows but still SHARES the same row
    lists. Each row needs to be copied too.
    """
    new_grid = []

    for row in range(len(grid) - 1, -1, -1):
        new_row = grid[row].copy()
        new_grid.append(new_row)

    return new_grid



def garage_report(garage):
    """
    *** 3D CHALLENGE ***

    A parking garage is stored as a cube (3D list):

        garage[floor][row][spot]

    Each cell is 0 (open) or 1 (taken). Floor 0 is the ground floor.

    Return a tuple with two things:
      1. a list with the number of OPEN spots on each floor
      2. the (floor, row, spot) of the first open spot, searching
         floor 0 first, then row by row, left to right.
         Use None if the garage is full.

    Do not change the garage.

    Parameters:
        garage (list): a 3D list of 0s and 1s

    Returns:
        tuple: (open_per_floor, first_open)

    Example:
        >>> garage = [
        ...     [[1, 1, 1],      # floor 0, row 0
        ...      [1, 1, 1]],     # floor 0, row 1
        ...     [[1, 0, 1],      # floor 1, row 0
        ...      [0, 0, 1]],     # floor 1, row 1
        ... ]
        >>> garage_report(garage)
        ([0, 3], (1, 0, 1))
        >>> garage_report([[[1, 1]], [[1, 1]]])
        ([0, 0], None)

    Hint: three loops - floors, then rows, then spots. Keep a running
    count for each floor, and only save first_open the first time.
    """
    open_per_floor = []
    first_open = None

    for floor in range(len(garage)):
        open_count = 0

        for row in range(len(garage[floor])):
            for spot in range(len(garage[floor][row])):

                if garage[floor][row][spot] == 0:
                    open_count += 1

                    if first_open is None:
                        first_open = (floor, row, spot)

        open_per_floor.append(open_count)

    return (open_per_floor, first_open)


# OPTIONAL BONUS (not tested): write park_car(garage) that finds the first
# open spot, changes it to 1, and returns where the car parked.


# ---------------------------------------------------------------------------
# PREWRITTEN HELPER - prints a garage so you can see the 3D structure
# ---------------------------------------------------------------------------

def show_garage(garage):
    """Print each floor of a garage. 'P' = taken, '_' = open."""
    for f in range(len(garage) - 1, -1, -1):     # top floor printed first
        print("  Floor", f)
        for row in garage[f]:
            print("    " + " ".join("P" if spot else "_" for spot in row))


# ---------------------------------------------------------------------------
# TESTS (do not change below this line)
# ---------------------------------------------------------------------------

def run_test(name, test):
    """Run one test function and report PASS / FAIL without stopping."""
    try:
        test()
        print("[PASS] " + name)
        return True
    except AssertionError as error:
        print("[FAIL] " + name + " -> " + str(error))
    except Exception as error:
        print("[FAIL] " + name + " -> " + type(error).__name__ + ": " + str(error))
    return False


def test_make_grid():
    result = make_grid(2, 3, 0)
    assert result == [[0, 0, 0], [0, 0, 0]], "make_grid(2, 3, 0) gave " + str(result)
    result = make_grid(3, 2, '-')
    assert result == [['-', '-'], ['-', '-'], ['-', '-']], "make_grid(3, 2, '-') gave " + str(result)
    assert make_grid(0, 4, 0) == [], "0 rows should give []"
    grid = make_grid(3, 3, 0)
    grid[0][0] = 9
    assert grid[1][0] == 0 and grid[2][0] == 0, "rows are aliases - changing one row changed others"


def test_column_totals():
    result = column_totals([[1, 2, 3], [4, 5, 6]])
    assert result == [5, 7, 9], "expected [5, 7, 9], got " + str(result)
    result = column_totals([[10], [20], [30]])
    assert result == [60], "expected [60], got " + str(result)
    result = column_totals([[7, 8]])
    assert result == [7, 8], "one row: expected [7, 8], got " + str(result)
    result = column_totals([[90, 80, 70], [85, 0, 100], [75, 95, 60], [100, 90, 80]])
    assert result == [350, 265, 310], "gradebook: expected [350, 265, 310], got " + str(result)


def test_find_value():
    seats = [['A', 'B', 'C'], ['D', 'X', 'F'], ['X', 'H', 'I']]
    result = find_value(seats, 'X')
    assert result == (1, 1), "first 'X' should be (1, 1), got " + str(result)
    result = find_value(seats, 'A')
    assert result == (0, 0), "'A' should be (0, 0), got " + str(result)
    result = find_value(seats, 'I')
    assert result == (2, 2), "'I' should be (2, 2), got " + str(result)
    result = find_value(seats, 'Z')
    assert result is None, "missing value should return None, got " + str(result)
    result = find_value([[0, 0], [0, 7]], 7)
    assert result == (1, 1), "7 should be at (1, 1), got " + str(result)


def test_flip_upside_down():
    original = [[1, 2], [3, 4], [5, 6]]
    result = flip_upside_down(original)
    assert result == [[5, 6], [3, 4], [1, 2]], "expected [[5, 6], [3, 4], [1, 2]], got " + str(result)
    assert original == [[1, 2], [3, 4], [5, 6]], "the original grid was changed"
    result[0][0] = 99
    assert original[2][0] == 5, "rows are shared - copy each row"
    assert flip_upside_down([[1, 2, 3]]) == [[1, 2, 3]], "one row should stay the same"


def test_garage_report():
    garage = [
        [[1, 1, 1], [1, 1, 1]],
        [[1, 0, 1], [0, 0, 1]],
    ]
    result = garage_report(garage)
    assert result == ([0, 3], (1, 0, 1)), "small garage: expected ([0, 3], (1, 0, 1)), got " + str(result)

    full = [[[1, 1]], [[1, 1]]]
    result = garage_report(full)
    assert result == ([0, 0], None), "full garage: expected ([0, 0], None), got " + str(result)

    big = [
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]],
        [[0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1]],
        [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
    ]
    snapshot = [[row[:] for row in floor] for floor in big]
    result = garage_report(big)
    assert result == ([1, 3, 11], (0, 2, 3)), "3-floor garage: expected ([1, 3, 11], (0, 2, 3)), got " + str(result)
    assert big == snapshot, "the garage was changed - report only, do not park cars"

    empty = [[[0, 0], [0, 0]]]
    result = garage_report(empty)
    assert result == ([4], (0, 0, 0)), "empty garage: expected ([4], (0, 0, 0)), got " + str(result)


if __name__ == "__main__":
    print("Sample garage for the 3D challenge:")
    show_garage([
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]],
        [[0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1]],
        [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
    ])
    print()

    passed = 0
    passed += run_test("1. make_grid", test_make_grid)
    passed += run_test("2. column_totals", test_column_totals)
    passed += run_test("3. find_value", test_find_value)
    passed += run_test("4. flip_upside_down", test_flip_upside_down)
    passed += run_test("5. garage_report (3D challenge)", test_garage_report)

    print()
    print(str(passed) + " of 5 functions passing")
    if passed == 5:
        print("All tests passed! Try the optional bonus: park_car(garage)")
