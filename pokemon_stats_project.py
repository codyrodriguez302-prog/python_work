"""
Pokemon Stats Data Project
PCEP Objectives: PCEP-30-02 2.2 (loops), 3.1 (lists, slicing, nested lists), 4.1 (functions)
Difficulty: Intermediate

DESCRIPTION:
You have the base stats for all 386 Pokemon from the first three generations.
You will load the data into a 2D list (a list of rows), then write functions
that slice, loop through, filter, rank, and summarize it. At the end you will
use your functions to answer twelve questions about the data.

LEARNING OBJECTIVES:
- Index and slice a 2D list to pull out rows, columns, and single values
- Use for loops and accumulators to total, average, and count data
- Build new lists by filtering rows that match a condition
- Find the largest value in a list without using max() or sort()
- Combine small functions to answer bigger questions

INSTRUCTIONS:
1. Put pokemon_gen1-3.csv in the SAME folder as this file.
2. Do not change load_data() or anything below the "DO NOT EDIT" line.
3. Work through the functions in order. Replace each "pass" with your code.
4. Run the file often. The checks at the bottom tell you which functions work.
5. When every check passes, finish answer_questions() and run it one last time.

RULES:
- Write your own loops. Do NOT use sum(), max(), min(), sort(), or sorted().
- Do not use dictionaries. Everything in this project is a list.
- You may use len(), range(), round(), append(), and the "in" operator.

THE DATA:
Every row in the data list looks like this:

    index:   0       1       2       3       4    5        6        7       8       9      10          11
           [Number, Name,   Type1,  Type2,  HP,  Attack,  Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary]
    e.g.   [6, "Charizard", "Fire", "Flying", 78, 84, 78, 109, 85, 100, 1, "No"]

- Type2 is the string "None" if the Pokemon has only one type.
- Legendary is "Yes" for legendary and mythical Pokemon, otherwise "No".
- Number, the six stats, and Generation are ints. Everything else is a string.
- Stats and types are from the current games (so Clefairy is a Fairy type).
Use the column constants below (NAME, TYPE1, ...) instead of typing numbers.
"""
import os



# Column positions -- use these instead of typing 0, 1, 2, ...
NUMBER = 0
NAME = 1
TYPE1 = 2
TYPE2 = 3
HP = 4
ATTACK = 5
DEFENSE = 6
SP_ATK = 7
SP_DEF = 8
SPEED = 9
GENERATION = 10
LEGENDARY = 11

FILENAME = "pokemon_gen1-3.csv"


def load_data():
    """
    PROVIDED -- do not change.
    Reads the CSV file and returns a 2D list. Each inner list is one Pokemon.
    The header row is NOT included.
    """
    folder = os.path.dirname(os.path.abspath(__file__))
    file = open(os.path.join(folder, FILENAME))
    lines = file.readlines()
    file.close()

    data = []
    for line in lines[1:]:
        parts = line.strip().split(",")
        if len(parts) != 12:
            continue
        row = [int(parts[0])]
        for text in parts[1:4]:
            row.append(text)
        for number in parts[4:11]:
            row.append(int(number))
        row.append(parts[11])
        data.append(row)
    return data


# =============================================================================
# PART A -- LOOK AROUND (indexing and slicing)
# =============================================================================

def first_rows(data, n):
    """
    Return the first n rows of the data.

    Parameters:
        data (list): the 2D list of Pokemon
        n (int): how many rows to return

    Returns:
        list: a new 2D list with the first n rows

    Example:
        >>> first_rows(SAMPLE, 2)
        [[1, 'Bulbasaur', ...], [6, 'Charizard', ...]]

    Hint: one slice. No loop needed.
    """
    return data[:n]
    

def last_rows(data, n):
    """
    Return the last n rows of the data.

    Parameters:
        data (list): the 2D list of Pokemon
        n (int): how many rows to return (n is at least 1)

    Returns:
        list: a new 2D list with the last n rows

    Example:
        >>> last_rows(SAMPLE, 1)
        [[381, 'Latios', 'Dragon', 'Psychic', 80, 90, 80, 130, 110, 110, 3, 'Yes']]

    Hint: negative indexes count from the end.
    """
    return data[-n:]


def get_page(data, page, per_page):
    """
    Split the data into "pages" and return one page, like a Pokedex app
    showing 10 Pokemon at a time. Page 1 is the first page.

    Parameters:
        data (list): the 2D list of Pokemon
        page (int): which page to return (1 = first page)
        per_page (int): how many rows are on each page

    Returns:
        list: the rows on that page (the last page may be shorter;
              a page past the end returns [])

    Example:
        >>> get_page(SAMPLE, 1, 3)      # rows 0, 1, 2
        >>> get_page(SAMPLE, 2, 3)      # rows 3, 4, 5
        >>> get_page(SAMPLE, 3, 3)      # rows 6, 7 (only two left)

    Hint: work out the start index and stop index first, then slice.
    """
    start= (page - 1) * per_page
    stop=start + per_page
    return data[start:stop]


def get_column(data, col):
    """
    Return every value in one column as a flat list.

    Parameters:
        data (list): the 2D list of Pokemon
        col (int): the column number (use a constant like TYPE1)

    Returns:
        list: one value from each row, in the same order as the rows

    Example:
        >>> get_column(SAMPLE, TYPE1)
        ['Grass', 'Fire', 'Electric', 'Ghost', 'Normal', 'Dark', 'Rock', 'Dragon']
    """
    ls=[]
    for i in data:
         ls.append(i[col])
    return ls
    



# =============================================================================
# PART B -- ADD IT UP (accumulators)
# =============================================================================

def stat_total(row):
    """
    Return the base stat total for ONE Pokemon:
    HP + Attack + Defense + Sp_Atk + Sp_Def + Speed.

    Parameters:
        row (list): a single Pokemon (one inner list)

    Returns:
        int: the total of the six stats

    Example:
        >>> stat_total([1, 'Bulbasaur', 'Grass', 'Poison', 45, 49, 49, 65, 65, 45, 1, 'No'])
        318

    Hint: slice out the six stat columns, then loop over that slice.
    """
    
    ls=row [4:10]
    total=0
    for i in ls:
        total+=i
    return int(total)

def stat_averages(data):
    """
    Find the average of EACH of the six stats across all Pokemon.

    Parameters:
        data (list): the 2D list of Pokemon (at least one row)

    Returns:
        list: [avg HP, avg Attack, avg Defense, avg Sp_Atk, avg Sp_Def, avg Speed],
              each rounded to 2 places

    Example:
        >>> stat_averages(SAMPLE)
        [81.62, 81.5, 74.0, 88.0, 90.62, 76.38]

    Hint: start with [0, 0, 0, 0, 0, 0]. You may need a loop inside a loop.
    """
    for rows in data():
        stats=rows[4:10]


def column_average(data, col):
    """
    Return the average of one number column.

    Parameters:
        data (list): the 2D list of Pokemon (at least one row)
        col (int): a number column (a stat or GENERATION)

    Returns:
        float: the average, rounded to 2 decimal places

    Example:
        >>> column_average(SAMPLE, SPEED)
        76.38
    """
    pass  # TODO: replace this line with your code


# =============================================================================
# PART C -- FILTER (build new lists)
# =============================================================================

def filter_rows(data, col, value):
    """
    Return only the rows where the given column equals value.

    Parameters:
        data (list): the 2D list of Pokemon
        col (int): the column to check
        value: what that column must equal (a string or a number)

    Returns:
        list: a new 2D list of matching rows, in their original order
              (an empty list if nothing matches)

    Example:
        >>> filter_rows(SAMPLE, LEGENDARY, "Yes")
        [[381, 'Latios', ...]]
        >>> filter_rows(SAMPLE, GENERATION, 2)
        [[197, 'Umbreon', ...], [248, 'Tyranitar', ...]]
    """
    pass  # TODO: replace this line with your code


def rows_between(data, col, low, high):
    """
    Return the rows where a number column is between low and high,
    INCLUDING low and high.

    Parameters:
        data (list): the 2D list of Pokemon
        col (int): a number column
        low (int): smallest allowed value
        high (int): largest allowed value

    Returns:
        list: a new 2D list of matching rows, in their original order

    Example:
        >>> rows_between(SAMPLE, SPEED, 90, 110)    # Charizard, Pikachu, Gengar, Latios
        >>> rows_between(SAMPLE, HP, 0, 50)         # Bulbasaur, Pikachu
    """
    pass  # TODO: replace this line with your code


def unique_values(data, col):
    """
    Return each different value in a column ONE time,
    in the order they first appear.

    Parameters:
        data (list): the 2D list of Pokemon
        col (int): the column to look at

    Returns:
        list: the values with no repeats

    Example:
        >>> unique_values(SAMPLE, TYPE2)
        ['Poison', 'Flying', 'None', 'Dark', 'Psychic']

    Hint: "not in"
    """
    pass  # TODO: replace this line with your code


def has_type(data, type_name):
    """
    Return the rows where type_name is EITHER the first or the second type.

    Parameters:
        data (list): the 2D list of Pokemon
        type_name (str): a type such as "Fire" or "Poison"

    Returns:
        list: a new 2D list of matching rows, in their original order

    Example:
        >>> has_type(SAMPLE, "Poison")      # Bulbasaur (Type2) and Gengar (Type2)
        [[1, 'Bulbasaur', ...], [94, 'Gengar', ...]]
        >>> has_type(SAMPLE, "Dark")        # Umbreon (Type1) and Tyranitar (Type2)
        [[197, 'Umbreon', ...], [248, 'Tyranitar', ...]]
    """
    pass  # TODO: replace this line with your code


# =============================================================================
# PART D -- FIND AND RANK (no max(), no sort())
# =============================================================================

def max_row(data, col):
    """
    Return the whole row that has the largest value in a number column.
    If there is a tie, return the one that comes FIRST.

    Parameters:
        data (list): the 2D list of Pokemon (at least one row)
        col (int): a number column

    Returns:
        list: one row (a single Pokemon)

    Example:
        >>> max_row(SAMPLE, DEFENSE)        # Umbreon and Tyranitar both have 110; return the first
        [197, 'Umbreon', 'Dark', 'None', 95, 65, 110, 60, 130, 65, 2, 'No']

    Hint: assume the first row is the best so far, then loop and compare.
    """
    pass  # TODO: replace this line with your code


def strongest(data):
    """
    Return the row with the highest stat total (use stat_total).
    If there is a tie, return the one that comes FIRST.

    Parameters:
        data (list): the 2D list of Pokemon (at least one row)

    Returns:
        list: one row (a single Pokemon)

    Example:
        >>> strongest(SAMPLE)               # Tyranitar and Latios both total 600; return the first
        [248, 'Tyranitar', 'Rock', 'Dark', 100, 134, 110, 95, 100, 61, 2, 'No']
    """
    pass  # TODO: replace this line with your code


def top_strongest(data, n):
    """
    Return the n Pokemon with the highest stat totals, highest first.
    Ties keep their original order. Do NOT change the original data list.

    Parameters:
        data (list): the 2D list of Pokemon
        n (int): how many to return (n <= len(data))

    Returns:
        list: a new 2D list with n rows, strongest first

    Example:
        >>> top = top_strongest(SAMPLE, 3)
        >>> top[0][NAME], top[1][NAME], top[2][NAME]
        ('Tyranitar', 'Latios', 'Snorlax')

    Hint: make a copy of data with a slice. Then repeat n times:
          find the strongest in the copy, add it to your answer,
          and remove it from the copy.
    """
    pass  # TODO: replace this line with your code


# =============================================================================
# PART E -- GROUP AND SUMMARIZE (lists inside lists)
# =============================================================================

def count_by(data, col):
    """
    Count how many rows have each different value in a column.

    Parameters:
        data (list): the 2D list of Pokemon
        col (int): the column to group by

    Returns:
        list: a 2D list of [value, count] pairs, in the order each
              value first appears

    Example:
        >>> count_by(SAMPLE, GENERATION)
        [[1, 5], [2, 2], [3, 1]]

    Hint: unique_values() gives you the groups. Then count each one.
    """
    pass  # TODO: replace this line with your code


def average_total_by(data, col):
    """
    Find the average stat total (use stat_total) for each different
    value in a column.

    Parameters:
        data (list): the 2D list of Pokemon
        col (int): the column to group by

    Returns:
        list: a 2D list of [value, average stat total] pairs, in the order
              each value first appears; averages rounded to 2 places

    Example:
        >>> average_total_by(SAMPLE, GENERATION)
        [[1, 442.4], [2, 562.5], [3, 600.0]]
    """
    pass  # TODO: replace this line with your code


def average_stat_by(data, group_col, stat_col):
    """
    Find the average of one stat for each different value in a column.

    Parameters:
        data (list): the 2D list of Pokemon
        group_col (int): the column to group by
        stat_col (int): the stat to average

    Returns:
        list: a 2D list of [value, average] pairs, in the order each
              value first appears; averages rounded to 2 places

    Example:
        >>> average_stat_by(SAMPLE, GENERATION, SPEED)
        [[1, 75.0], [2, 63.0], [3, 110.0]]

    Hint: you already wrote filter_rows() and column_average().
    """
    pass  # TODO: replace this line with your code


# =============================================================================
# PART F -- ANSWER THE QUESTIONS
# Replace each None with code that finds the answer. Use your functions!
# Some answers need a few lines of code (a loop to find the biggest pair, etc.).
# =============================================================================

def answer_questions(data):
    # Q1. How many Pokemon (rows) are in the data?
    q1 = None
    print("Q1.  Number of Pokemon:", q1)

    # Q2. How many DIFFERENT first types (Type1) are there?
    q2 = None
    print("Q2.  Different first types:", q2)

    # Q3. What is the strongest Pokemon that is NOT legendary? Give its name and stat total.
    q3 = None
    print("Q3.  Strongest non-legendary:", q3)

    # Q4. List the 5 strongest Pokemon overall. Print each name and stat total on its own line.
    print("Q4.  Top 5 strongest:")
    # TODO: loop and print

    # Q5. Which first type (Type1) has the most Pokemon? Give the type and count.
    q5 = None
    print("Q5.  Most common first type:", q5)

    # Q6. Which first type (Type1) has the highest average stat total? Give the type and average.
    q6 = None
    print("Q6.  Strongest type on average:", q6)

    # Q7. What percent of these Pokemon are legendary? Round to 1 decimal place.
    q7 = None
    print("Q7.  Percent legendary:", q7)

    # Q8. What is the fastest Generation 3 Pokemon? Give its name and Speed.
    q8 = None
    print("Q8.  Fastest Gen 3 Pokemon:", q8)

    # Q9. How many Pokemon have an Attack of 100 or higher?
    q9 = None
    print("Q9.  Pokemon with 100+ Attack:", q9)

    # Q10. Which generation has the highest average stat total? Give the generation and average.
    q10 = None
    print("Q10. Strongest generation on average:", q10)

    # Q11. How many Pokemon are part Flying type (Flying as EITHER type)?
    q11 = None
    print("Q11. Part-Flying Pokemon:", q11)

    # Q12. Which Water-type Pokemon (either type) has the highest Sp_Atk? Give its name and Sp_Atk.
    q12 = None
    print("Q12. Best Water-type Sp_Atk:", q12)


# =============================================================================
# DO NOT EDIT BELOW THIS LINE -- self-checks that run your functions
# on a small sample of 8 Pokemon so you can see if they work.
# =============================================================================

SAMPLE = [
    [1, "Bulbasaur", "Grass", "Poison", 45, 49, 49, 65, 65, 45, 1, "No"],
    [6, "Charizard", "Fire", "Flying", 78, 84, 78, 109, 85, 100, 1, "No"],
    [25, "Pikachu", "Electric", "None", 35, 55, 40, 50, 50, 90, 1, "No"],
    [94, "Gengar", "Ghost", "Poison", 60, 65, 60, 130, 75, 110, 1, "No"],
    [143, "Snorlax", "Normal", "None", 160, 110, 65, 65, 110, 30, 1, "No"],
    [197, "Umbreon", "Dark", "None", 95, 65, 110, 60, 130, 65, 2, "No"],
    [248, "Tyranitar", "Rock", "Dark", 100, 134, 110, 95, 100, 61, 2, "No"],
    [381, "Latios", "Dragon", "Psychic", 80, 90, 80, 130, 110, 110, 3, "Yes"],
]


def _same(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) < 0.006
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not _same(a[i], b[i]):
                return False
        return True
    return a == b


def _sample():
    copy = []
    for row in SAMPLE:
        copy.append(row[:])
    return copy


def _top_keeps_data():
    data = _sample()
    result = top_strongest(data, 3)
    if result is None:
        return None
    return data == SAMPLE


def run_checks():
    S = SAMPLE
    checks = [
        ("first_rows", lambda: first_rows(_sample(), 2), [S[0], S[1]]),
        ("first_rows", lambda: first_rows(_sample(), 0), []),
        ("last_rows", lambda: last_rows(_sample(), 1), [S[7]]),
        ("last_rows", lambda: last_rows(_sample(), 3), [S[5], S[6], S[7]]),
        ("get_page", lambda: get_page(_sample(), 1, 3), [S[0], S[1], S[2]]),
        ("get_page", lambda: get_page(_sample(), 2, 3), [S[3], S[4], S[5]]),
        ("get_page", lambda: get_page(_sample(), 3, 3), [S[6], S[7]]),
        ("get_page", lambda: get_page(_sample(), 5, 3), []),
        ("get_column", lambda: get_column(_sample(), TYPE1),
         ["Grass", "Fire", "Electric", "Ghost", "Normal", "Dark", "Rock", "Dragon"]),
        ("get_column", lambda: get_column(_sample(), SPEED), [45, 100, 90, 110, 30, 65, 61, 110]),
        ("stat_total", lambda: stat_total(S[0][:]), 318),
        ("stat_total", lambda: stat_total(S[2][:]), 320),
        ("stat_averages", lambda: stat_averages(_sample()), [81.62, 81.5, 74.0, 88.0, 90.62, 76.38]),
        ("column_average", lambda: column_average(_sample(), SPEED), 76.38),
        ("column_average", lambda: column_average(_sample(), GENERATION), 1.5),
        ("filter_rows", lambda: filter_rows(_sample(), LEGENDARY, "Yes"), [S[7]]),
        ("filter_rows", lambda: filter_rows(_sample(), GENERATION, 2), [S[5], S[6]]),
        ("filter_rows", lambda: filter_rows(_sample(), TYPE1, "Water"), []),
        ("rows_between", lambda: rows_between(_sample(), SPEED, 90, 110), [S[1], S[2], S[3], S[7]]),
        ("rows_between", lambda: rows_between(_sample(), HP, 0, 50), [S[0], S[2]]),
        ("unique_values", lambda: unique_values(_sample(), TYPE2),
         ["Poison", "Flying", "None", "Dark", "Psychic"]),
        ("unique_values", lambda: unique_values(_sample(), GENERATION), [1, 2, 3]),
        ("has_type", lambda: has_type(_sample(), "Poison"), [S[0], S[3]]),
        ("has_type", lambda: has_type(_sample(), "Dark"), [S[5], S[6]]),
        ("has_type", lambda: has_type(_sample(), "Water"), []),
        ("max_row", lambda: max_row(_sample(), DEFENSE), S[5]),
        ("max_row", lambda: max_row(_sample(), SPEED), S[3]),
        ("max_row", lambda: max_row(_sample(), HP), S[4]),
        ("strongest", lambda: strongest(_sample()), S[6]),
        ("strongest", lambda: strongest(_sample()[0:4]), S[1]),
        ("top_strongest", lambda: top_strongest(_sample(), 3), [S[6], S[7], S[4]]),
        ("top_strongest", lambda: _top_keeps_data(), True),
        ("count_by", lambda: count_by(_sample(), GENERATION), [[1, 5], [2, 2], [3, 1]]),
        ("count_by", lambda: count_by(_sample(), TYPE2),
         [["Poison", 2], ["Flying", 1], ["None", 3], ["Dark", 1], ["Psychic", 1]]),
        ("average_total_by", lambda: average_total_by(_sample(), GENERATION),
         [[1, 442.4], [2, 562.5], [3, 600.0]]),
        ("average_stat_by", lambda: average_stat_by(_sample(), GENERATION, SPEED),
         [[1, 75.0], [2, 63.0], [3, 110.0]]),
    ]

    print("=" * 60)
    print("SELF-CHECKS (using the 8-Pokemon SAMPLE)")
    print("=" * 60)
    passed = 0
    for name, test, expected in checks:
        try:
            got = test()
        except Exception as error:
            print("  ERROR      ", name, "->", type(error).__name__ + ":", error)
            continue
        if got is None:
            print("  not done   ", name)
        elif _same(got, expected):
            print("  PASS       ", name)
            passed += 1
        else:
            print("  FAIL       ", name)
            print("        expected:", expected)
            print("        got:     ", got)
    print("-" * 60)
    print("  ", passed, "of", len(checks), "checks passed")
    print("=" * 60)
    return passed == len(checks)


if __name__ == "__main__":
    pokemon = load_data()
    print("Loaded", len(pokemon), "Pokemon from", FILENAME)
    print()
    all_passed = run_checks()
    print()
    if not all_passed:
        print("Keep going! Answers below may be wrong until every check passes.")
        print()
    print("=" * 60)
    print("ANSWERS (using all of", FILENAME + ")")
    print("=" * 60)
    answer_questions(pokemon)
