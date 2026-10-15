"""
Functions & Decisions — Intro
PCEP Objectives: PCEP-30-02 4.1 (functions, return, None, generators)
                 PCEP-30-02 2.1 (if, if-else, if-elif, if-elif-else, nesting)
Difficulty: Beginner

HOW THIS FILE WORKS
  Each topic has:  EXAMPLE (finished, read it)  ->  TRAPS  ->  LEARN MORE  ->  DIY (you write it)
  Replace every `pass` in the DIY functions. Run the file to check your work.
"""


# =============================================================================
# 1. DEFINING AND INVOKING A FUNCTION
# =============================================================================

def say_hello(name):                      # define
    print("Hello, " + name + "!")

# say_hello("Sam")                        # invoke  ->  Hello, Sam!

# TRAPS:
#   - Defining a function does NOT run it. You must call it: say_hello("Sam")
#   - Forgetting the ( ) -> say_hello  is the function itself, not a call.
#   - You must define a function BEFORE the line that calls it runs.
# LEARN MORE: https://www.w3schools.com/python/python_functions.asp

def diy_greet_twice(name):
    """
    Print "Hi, <name>" two times (two lines).
    >>> diy_greet_twice("Ava")
    Hi, Ava
    Hi, Ava
    """
    print("hi, " + name)
    print("hi, " + name)


# =============================================================================
# 2. THE return KEYWORD
# =============================================================================

def add(a, b):
    return a + b

# total = add(2, 3)                       # total is 5

# TRAPS:
#   - print() shows a value; return HANDS IT BACK. They are not the same.
#   - Code after return (in the same block) never runs.
#   - A function can only return once per call — the first return wins.
# LEARN MORE: https://www.w3schools.com/python/ref_keyword_return.asp

def diy_square(n):
    """
    Return n times n.
    >>> diy_square(4)
    16
    """
    return n * n


# =============================================================================
# 3. THE None KEYWORD
# =============================================================================

def print_only(x):
    print(x)                              # no return statement

# result = print_only(7)                  # prints 7, but result is None

# TRAPS:
#   - A function with no return (or a bare `return`) gives back None.
#   - None is not 0, not False, and not "" — it is its own type (NoneType).
#   - Check for it with `is None`, not `== None`.
# LEARN MORE: https://www.w3schools.com/python/python_none.asp

def diy_first_letter(word):
    """
    Return the first letter of word. If word is empty (""), return None.
    >>> diy_first_letter("cat")
    'c'
    >>> diy_first_letter("") is None
    True
    """
    if word == "":
        return None
    else:
        return (word)[0]
    


# =============================================================================
# 4. BOOLEAN OPERATORS: and, or, not
# =============================================================================

def can_drive(age, has_license):
    return age >= 16 and has_license

# can_drive(17, True)  -> True
# can_drive(17, False) -> False

# TRAPS:
#   - Priority: not  >  and  >  or.   True or False and False  ->  True
#   - `x == 1 or 2` is ALWAYS truthy. Write `x == 1 or x == 2`.
#   - Python uses the words and/or/not — not &&, ||, !
#   - Capital T and F: True / False (true is an error).
# LEARN MORE: https://www.w3schools.com/python/python_if_logical.asp
#             https://www.w3schools.com/python/python_booleans.asp

def diy_is_weekend(day):
    """
    Return True if day is "Saturday" or "Sunday", otherwise False.
    >>> diy_is_weekend("Sunday")
    True
    >>> diy_is_weekend("Monday")
    False
    """
    if day == "Saturday" or day == "Sunday":
        return True
    else:
        return False


# =============================================================================
# 5. if
# =============================================================================

def warn_if_cold(temp):
    if temp < 32:
        print("Freezing!")

# TRAPS:
#   - Don't forget the colon  :  at the end of the if line.
#   - The body MUST be indented. Mixed tabs/spaces cause errors.
#   - `=` assigns, `==` compares.  `if x = 5:` is a SyntaxError.
# LEARN MORE: https://www.w3schools.com/python/python_conditions.asp

def diy_make_positive(n):
    """
    If n is negative, change it to positive. Return n.
    >>> diy_make_positive(-8)
    8
    >>> diy_make_positive(3)
    3
    """
    if n < 0:
        n = -n
    return n


# =============================================================================
# 6. if-else
# =============================================================================

def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

# TRAPS:
#   - else never has a condition:  `else n > 5:` is an error.
#   - else must line up with its if (same indentation).
# LEARN MORE: https://www.w3schools.com/python/python_if_else.asp

def diy_pass_fail(score):
    """
    Return "pass" if score is 70 or higher, otherwise "fail".
    >>> diy_pass_fail(70)
    'pass'
    >>> diy_pass_fail(69)
    'fail'
    """
    if score >= 70:
        return "pass"
    else:
        return "fail"


# =============================================================================
# 7. if-elif  (no else)
# =============================================================================

def traffic_light(color):
    if color == "red":
        return "stop"
    elif color == "yellow":
        return "slow"
    elif color == "green":
        return "go"
    # no else -> any other color falls through and returns None

# TRAPS:
#   - Without an else, it's possible for NO branch to run.
#   - It's `elif`, not `else if` or `elseif`.
# LEARN MORE: https://www.w3schools.com/python/python_if_elif.asp

def diy_coin_name(cents):
    """
    1 -> "penny", 5 -> "nickel", 10 -> "dime", 25 -> "quarter".
    Use if-elif only (no else). Anything else returns None.
    >>> diy_coin_name(10)
    'dime'
    >>> diy_coin_name(3) is None
    True
    """
    if cents == 1:
        return "penny"
    elif cents == 5:
        print("nickel")
    elif cents == 10:
        return "dime"
    elif cents == 25:
        return "quarter"
    


# =============================================================================
# 8. if-elif-else
# =============================================================================

def sign(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

# TRAPS:
#   - Only the FIRST true branch runs; the rest are skipped.
#   - Order matters! Check the most specific condition first.
#       if score >= 60: ...  elif score >= 90: ...   <- 95 never reaches the 90 branch
# LEARN MORE: https://www.w3schools.com/python/python_if_elif.asp

def diy_letter_grade(score):
    """
    90+ -> "A", 80-89 -> "B", 70-79 -> "C", below 70 -> "F"
    >>> diy_letter_grade(85)
    'B'
    >>> diy_letter_grade(42)
    'F'
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# =============================================================================
# 9. MULTIPLE (separate) if STATEMENTS
# =============================================================================

def describe(n):
    tags = ""
    if n > 0:
        tags += "positive "
    if n % 2 == 0:
        tags += "even "
    if n > 100:
        tags += "big "
    return tags.strip()

# describe(200) -> "positive even big"   (ALL true ifs run)

# TRAPS:
#   - Separate ifs are ALL checked. elif stops at the first match.
#     Using if when you meant elif (or the reverse) is a classic exam trick.
# LEARN MORE: https://www.w3schools.com/python/python_conditions.asp

def diy_count_true(a, b, c):
    """
    Return how many of a, b, c are True. Use three separate if statements.
    >>> diy_count_true(True, False, True)
    2
    """
    count = 0
    # your three if statements here
    if a:
        count += 1
    if b:
        count += 1
    if c:
        count += 1
    return count



# =============================================================================
# 10. NESTED if
# =============================================================================

def ticket_price(age, is_student):
    if age < 18:
        return 5
    else:
        if is_student:
            return 7
        else:
            return 10

# TRAPS:
#   - Indentation decides which if an else belongs to. Line them up carefully.
#   - Deep nesting gets hard to read — sometimes `and` is cleaner.
# LEARN MORE: https://www.w3schools.com/python/python_if_nested_if.asp

def diy_can_enter(has_ticket, age):
    """
    No ticket -> "no ticket".
    Has ticket: age 13+ -> "welcome", under 13 -> "need adult".
    Use a nested if.
    >>> diy_can_enter(False, 20)
    'no ticket'
    >>> diy_can_enter(True, 10)
    'need adult'
    """
    if not has_ticket:
        return("no ticket")
    else:
        if age<=13:
            return( "need adult")
        else:
            return("welcome")

# =============================================================================
# 11. GENERATORS (yield)
# =============================================================================

def count_to(n):
    i = 1
    while i <= n:
        yield i                           # hand back one value, pause here
        i += 1

# for x in count_to(3): print(x)          -> 1  2  3
# list(count_to(3))                       -> [1, 2, 3]

# TRAPS:
#   - Calling count_to(3) does NOT run the code — it returns a generator object.
#   - A generator can only be looped through ONCE. After that it's empty.
#   - yield gives many values over time; return ends the generator.
# LEARN MORE: https://www.w3schools.com/python/python_generators.asp

def diy_evens_up_to(n):
    """
    Yield every even number from 0 up to and including n.
    >>> list(diy_evens_up_to(6))
    [0, 2, 4, 6]
    """
    vaso=0
    while vaso <=n:
        yield vaso
        vaso +=2


# =============================================================================
# TESTS — run this file to check your DIY functions
# =============================================================================
if __name__ == "__main__":
    passed = 0
    total = 0

    def check(label, got, expected):
        global passed, total
        total += 1
        if got == expected:
            passed += 1
            print("  PASS ", label)
        else:
            print("  FAIL ", label, "-> got", repr(got), "expected", repr(expected))

    print("1. diy_greet_twice (look for two lines):")
    diy_greet_twice("Ava")

    check("diy_square(4)", diy_square(4), 16)
    check("diy_first_letter('cat')", diy_first_letter("cat"), "c")
    check("diy_first_letter('')", diy_first_letter(""), None)
    check("diy_is_weekend('Sunday')", diy_is_weekend("Sunday"), True)
    check("diy_is_weekend('Monday')", diy_is_weekend("Monday"), False)
    check("diy_make_positive(-8)", diy_make_positive(-8), 8)
    check("diy_make_positive(3)", diy_make_positive(3), 3)
    check("diy_pass_fail(70)", diy_pass_fail(70), "pass")
    check("diy_pass_fail(69)", diy_pass_fail(69), "fail")
    check("diy_coin_name(25)", diy_coin_name(25), "quarter")
    check("diy_coin_name(3)", diy_coin_name(3), None)
    check("diy_letter_grade(95)", diy_letter_grade(95), "A")
    check("diy_letter_grade(85)", diy_letter_grade(85), "B")
    check("diy_letter_grade(70)", diy_letter_grade(70), "C")
    check("diy_letter_grade(42)", diy_letter_grade(42), "F")
    check("diy_count_true(True, False, True)", diy_count_true(True, False, True), 2)
    check("diy_can_enter(False, 20)", diy_can_enter(False, 20), "no ticket")
    check("diy_can_enter(True, 10)", diy_can_enter(True, 10), "need adult")
    check("diy_can_enter(True, 15)", diy_can_enter(True, 15), "welcome")

    gen = diy_evens_up_to(6)
    check("list(diy_evens_up_to(6))", list(gen) if gen is not None else None, [0, 2, 4, 6])

    print("\nScore:", passed, "/", total)
    # Note: diy_first_letter('') and diy_coin_name(3) pass even before you
    # write them — a `pass` function returns None. Think about why!
