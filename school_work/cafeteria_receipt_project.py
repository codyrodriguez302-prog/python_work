"""
Cafeteria Receipt System - Group Project
PCEP Objective: PCEP-30-02 1.3, 1.4, 1.5 (Section 1: Programming and Python Fundamentals)
Team Size: 4 students

DESCRIPTION:
Your group is building the register software for the school cafeteria. A cash
register takes a raw price string and a scanned quantity code, applies the
"buy 4, get the 5th free" rule, and prints one formatted line on a receipt.

The system is split into five functions. Each of the four team members owns one
function; the fifth function is written by the group together and calls the
other four. No function is useful on its own -- the grader only awards points
for tests that run data through the whole chain, so the group's score depends
on all five functions working together.

GROUP ROLES (write your names here):
    Student A: __________________  owns  to_cents()
    Student B: __________________  owns  read_quantity()
    Student C: __________________  owns  line_total()
    Student D: __________________  owns  format_money()
    ALL FOUR:  together            own   print_receipt_line()

LEARNING OBJECTIVES:
- Convert between strings and numbers with int(), float(), str(), and round()
- Read integer literals written in binary, octal, decimal, and hexadecimal
- Apply arithmetic operators (*, -, //, %) and respect operator precedence
- Recognize and work around floating-point accuracy problems
- Control print() output using the sep= and end= keyword parameters

EXPECTED OUTCOMES:
After completing this assignment, students will be able to:
- Explain why input() and raw text must be cast before arithmetic
- Explain why money is stored as whole cents instead of floats
- Read and produce values in the four numeral systems Python supports
- Build formatted output from arithmetic alone, without string formatting tools
- Integrate independently written functions into one working program

INSTRUCTIONS:
1. Divide the four numbered functions among your four team members.
2. Read your function's docstring carefully. Implement ONLY your own function.
   Do not edit a teammate's function -- report bugs to its owner instead.
3. Run this file (python cafeteria_receipt_project.py) at any time. The
   DIAGNOSTIC section tells each member whether their own function is behaving;
   it is NOT worth any points.
4. Once all four are passing diagnostics, write print_receipt_line() together.
5. The GRADED section is worth 100 points. Every graded check passes data
   through several functions at once, so a single broken function will cost
   your group points on many checks. Aim for 100/100.
6. Submit this one file with all five functions implemented.

A WARNING ABOUT TESTING:
The grader does not check a handful of hand-picked prices. It sweeps EVERY
price from $0.00 to $99.99, samples prices up to $9,999.99, and sweeps every
quantity from 0 to 255 in all four numeral systems. Code that happens to work
on the examples in the docstrings but not on the other several thousand cases
will lose points. Write each function so it is correct for every input, not
for the examples.

RULES:
- Do not import anything. Everything you need is built in.
- Do not change the function names, parameters, or the test section.
- Money is always handled as a whole number of CENTS inside the program.
"""


# =============================================================================
# FUNCTION 1 - owner: Student A
# =============================================================================

def to_cents(price_string):
    """
    Convert a price written as text into a whole number of cents.

    The register receives prices as text (exactly what input() would give you),
    always in dollars with two decimal places. Every later calculation works in
    whole cents, so this function is the front door of the whole program.

    This function demonstrates type casting and floating-point accuracy.

    Parameters:
        price_string (str): A price in dollars with exactly two decimal places,
                            e.g. "4.99", "0.07", "12.00", "1503.60"

    Returns:
        int: The same amount expressed in whole cents

    Example:
        >>> to_cents("4.99")
        499
        >>> to_cents("0.07")
        7
        >>> to_cents("12.00")
        1200

    THE TRAP:
        Computers store 1.15 as a number very slightly BELOW 1.15, so
        float("1.15") * 100 comes out as 114.99999999999999, and int() throws
        away the fraction and hands you 114. The customer is undercharged by a
        penny and your group loses points.

        This is not a rare accident. Out of the 10,000 prices from $0.00 to
        $99.99, more than 600 of them break if you use int() this way -- and
        "4.99" is NOT one of them, so testing only the example above will fool
        you into thinking your function works.

    THE FIX:
        round() moves to the NEAREST whole number instead of chopping downward.
        The floating-point error is always far smaller than half a penny, so
        rounding lands on the correct cent for every price the register will
        ever see. Round first, then make sure what you return is an int.
    """
     


# =============================================================================
# FUNCTION 2 - owner: Student B
# =============================================================================

def read_quantity(quantity_code):
    """
    Convert a scanned quantity code into an integer.

    The cafeteria's barcode scanners are old and different models encode the
    quantity in different numeral systems. A code always arrives as text and
    may be plain decimal or carry a Python numeral-system prefix:

        "7"      decimal          -> 7
        "0b101"  binary (0b)      -> 5
        "0o17"   octal (0o)       -> 15
        "0x1F"   hexadecimal (0x) -> 31

    Hex codes may use upper or lower case letters ("0x1f" and "0x1F" are the
    same quantity), and any code may be zero.

    This function demonstrates literals, numeral systems, and casting.

    Parameters:
        quantity_code (str): A quantity as text, with or without a base prefix

    Returns:
        int: The quantity as an ordinary decimal integer

    Example:
        >>> read_quantity("12")
        12
        >>> read_quantity("0b1100")
        12
        >>> read_quantity("0o14")
        12
        >>> read_quantity("0xC")
        12
        >>> read_quantity("0b0")
        0

    Hint: int() takes an optional SECOND argument, the base. Passing base 0
    tells Python "figure out the base from the prefix." One line handles all
    four systems -- you should not need to test for the prefix yourself.
    """
    pass  # TODO: Student B implements this function


# =============================================================================
# FUNCTION 3 - owner: Student C
# =============================================================================

def line_total(unit_cents, quantity):
    """
    Calculate what a customer actually pays for one item on the receipt.

    The cafeteria runs a standing promotion: BUY 4, GET THE 5TH FREE. For every
    complete group of five items, the customer is charged for only four. Items
    left over after the complete groups are all charged normally.

        quantity 4  -> pays for 4      quantity 9  -> pays for 8
        quantity 5  -> pays for 4      quantity 10 -> pays for 8
        quantity 6  -> pays for 5      quantity 11 -> pays for 9

    This function demonstrates integer arithmetic operators and precedence.

    Parameters:
        unit_cents (int): Price of ONE item, in whole cents (0 or more)
        quantity (int): How many were ordered (0 or more, no upper limit)

    Returns:
        int: Total charge for this line, in whole cents

    Example:
        >>> line_total(199, 4)
        796
        >>> line_total(199, 5)
        796
        >>> line_total(250, 10)
        2000
        >>> line_total(500, 0)
        0

    Hint: Floor division (//) counts how many complete groups of five there
    are, and each complete group means one free item. Work out the number of
    items the customer PAYS for first, then multiply.

    Note: Keep everything as int. Never use / here -- / always produces a
    float, and a float total will reintroduce exactly the rounding problem
    Student A worked to eliminate.
    """
    pass  # TODO: Student C implements this function


# =============================================================================
# FUNCTION 4 - owner: Student D
# =============================================================================

def format_money(total_cents):
    """
    Turn a whole number of cents back into a dollar string for the receipt.

    The result always has a dollar sign, at least one digit for the dollars,
    a decimal point, and EXACTLY two digits for the cents.

    This function demonstrates arithmetic operators, casting, and string
    concatenation. Build the text out of arithmetic -- you do not need (and
    should not use) any string formatting tools for this.

    Parameters:
        total_cents (int): An amount in whole cents, 0 or more. A large order
                           can easily run past $100, so do not assume the
                           dollar part is a single digit.

    Returns:
        str: The amount as a dollar string, e.g. "$4.99"

    Example:
        >>> format_money(499)
        '$4.99'
        >>> format_money(7)
        '$0.07'
        >>> format_money(1200)
        '$12.00'
        >>> format_money(0)
        '$0.00'
        >>> format_money(123456)
        '$1234.56'

    THE TRAP:
        str(705 % 100) is "5", not "05", so gluing the dollars and the cents
        together directly gives you "$7.5" for what should be "$7.05". Any
        amount whose cents part is under 10 breaks this way -- that is one
        price in every ten.

    THE FIX:
        Pull out the cents TENS digit and the cents ONES digit as two separate
        numbers using // and %, then convert each one on its own. Two digits
        converted separately are always two characters long, so the format is
        correct for every amount, large or small.
    """
    pass  # TODO: Student D implements this function


# =============================================================================
# FUNCTION 5 - owned by the WHOLE GROUP
# =============================================================================

def print_receipt_line(item_name, price_string, quantity_code):
    """
    Print one complete receipt line and return the same text.

    This is the function that ties the project together. It must NOT do any
    arithmetic or string building of its own beyond joining the pieces -- it
    calls to_cents(), read_quantity(), line_total(), and format_money() and
    uses whatever they hand back.

    The receipt line has three fields separated by " | " (space, pipe, space):

        ITEM NAME | xQUANTITY | $TOTAL

    Print it with a SINGLE print() call that passes the three fields as three
    separate arguments and uses the sep= and end= keyword parameters. Write
    end="\\n" explicitly even though that is the default, so it is clear you
    know the parameter is there. Then return the same line as one string, with
    no trailing newline.

    This function demonstrates print() with sep= and end=, and shows how small
    functions combine into a program.

    Parameters:
        item_name (str): Name of the menu item, e.g. "Taco"
        price_string (str): Price of one item as text, e.g. "1.99"
        quantity_code (str): Scanned quantity code, e.g. "0b101"

    Returns:
        str: The receipt line, e.g. "Taco | x5 | $7.96"

    Example:
        >>> print_receipt_line("Taco", "1.99", "0b101")
        Taco | x5 | $7.96
        'Taco | x5 | $7.96'
        >>> print_receipt_line("Nachos", "2.50", "0x0A")
        Nachos | x10 | $20.00
        'Nachos | x10 | $20.00'

    Hint: Build the quantity field with "x" + str(quantity). The returned
    string and the printed output must match exactly, so build the return
    value out of the same three fields joined by " | ".
    """
    pass  # TODO: The whole group implements this function together


# =============================================================================
# TEST SECTION - DO NOT EDIT ANYTHING BELOW THIS LINE
#
# This section only CHECKS your work. It contains no worked solution, so
# reading it will not tell you how to write any of the five functions.
# =============================================================================

if __name__ == "__main__":
    import io
    import contextlib

    # ------------------------------------------------------------------ #
    # Grader plumbing                                                     #
    # ------------------------------------------------------------------ #

    # A lookup table of two-digit strings: "00", "01", ... "99". This is plain
    # data used to build test PRICES. It is not a hint about format_money().
    TWO_DIGIT = ("000102030405060708091011121314151617181920212223242526272829"
                 "303132333435363738394041424344454647484950515253545556575859"
                 "606162636465666768697071727374757677787980818283848586878889"
                 "90919293949596979899")

    def price_at(cents):
        """Build the price string for a given number of cents."""
        return str(cents // 100) + "." + TWO_DIGIT[2 * (cents % 100):2 * (cents % 100) + 2]

    def all_codes(n):
        """Every way a scanner might encode the quantity n."""
        return (str(n), bin(n), oct(n), hex(n), hex(n).upper().replace("0X", "0x"))

    def compose(name, price_string, quantity_code):
        """The receipt line built from YOUR OWN four functions.

        Checks 1-6 pin those four functions down against fixed expected values,
        so once they pass, this is a trustworthy expectation for check 7.
        """
        quantity = read_quantity(quantity_code)
        return (name + " | x" + str(quantity) + " | "
                + format_money(line_total(to_cents(price_string), quantity)))

    def run(check):
        """Run a check, swallowing its output. Returns None or a failure string."""
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                return check()
        except Exception as exc:
            return "raised " + type(exc).__name__ + ": " + str(exc)

    def describe(label, got, want):
        return label + " -> got " + repr(got) + ", expected " + repr(want)

    def money_problem(text, total_cents):
        """Check a money string is well formed and worth exactly total_cents.

        This VERIFIES a result. It does not build one, so it is not a hint.
        """
        if type(text) is not str:
            return "expected a string, got " + repr(text)
        if not text.startswith("$"):
            return repr(text) + " does not start with a dollar sign"
        whole, dot, frac = text[1:].partition(".")
        if dot != "." or len(frac) != 2:
            return repr(text) + " needs exactly two digits after the decimal point"
        if not whole.isdigit() or not frac.isdigit():
            return repr(text) + " contains something that is not a digit"
        if int(whole) * 100 + int(frac) != total_cents:
            return repr(text) + " is not " + str(total_cents) + " cents"
        return None

    # ------------------------------------------------------------------ #
    # DIAGNOSTICS - worth 0 points, for finding your own bugs             #
    # ------------------------------------------------------------------ #

    def diag_a():
        for cents in list(range(0, 10000)) + list(range(0, 1000000, 997)):
            price = price_at(cents)
            got = to_cents(price)
            if got != cents or type(got) is not int:
                return describe('to_cents("' + price + '")', got, cents)
        return None

    def diag_b():
        for n in range(0, 256):
            for code in all_codes(n):
                got = read_quantity(code)
                if got != n or type(got) is not int:
                    return describe('read_quantity("' + code + '")', got, n)
        return None

    def diag_c():
        for unit in (0, 1, 7, 199, 250, 1099):
            got = line_total(unit, 0)
            if got != 0:
                return describe("line_total(" + str(unit) + ", 0)", got, 0)
            for n in range(1, 201):
                previous = line_total(unit, n - 1)
                got = line_total(unit, n)
                # Every 5th item is free; every other item costs full price.
                want = previous if n % 5 == 0 else previous + unit
                if got != want or type(got) is not int:
                    return describe("line_total(" + str(unit) + ", " + str(n) + ")",
                                    got, want)
        return None

    def diag_d():
        for cents in list(range(0, 10000)) + list(range(10000, 1000000, 991)):
            problem = money_problem(format_money(cents), cents)
            if problem is not None:
                return "format_money(" + str(cents) + ") " + problem
        return None

    print("=" * 68)
    print("DIAGNOSTICS (0 points - each member checks their own function)")
    print("=" * 68)

    for owner, check in (("Student A  to_cents      ", diag_a),
                         ("Student B  read_quantity ", diag_b),
                         ("Student C  line_total    ", diag_c),
                         ("Student D  format_money  ", diag_d)):
        problem = run(check)
        if problem is None:
            print("  [   OK   ] " + owner)
        else:
            print("  [ NOT YET ] " + owner + "  " + problem)

    # ------------------------------------------------------------------ #
    # GRADED CHECKS - 100 points, every check spans multiple functions    #
    # ------------------------------------------------------------------ #

    print()
    print("=" * 68)
    print("GRADED CHECKS (100 points)")
    print("=" * 68)

    score = 0
    possible = 0

    def grade(label, uses, points, check):
        """Award points only if the whole chain of functions is correct."""
        global score, possible
        possible += points
        problem = run(check)
        if problem is None:
            score += points
            print("  [+" + str(points).rjust(3) + "] " + label + "   (uses " + uses + ")")
        else:
            print("  [   0] " + label + "   (uses " + uses + ")")
            print("         " + problem)

    # 1. EVERY price from $0.00 to $99.99 survives the trip out and back.
    def check_round_trip():
        for cents in range(0, 10000):
            price = price_at(cents)
            got = format_money(to_cents(price))
            if got != "$" + price:
                return describe("price " + price, got, "$" + price)
        return None

    grade("Every price $0.00-$99.99 round-trips (10,000 prices)", "A+D", 10,
          check_round_trip)

    # 2. The same, sampled all the way up to $9,999.99.
    def check_large_prices():
        for cents in range(0, 1000000, 499):
            price = price_at(cents)
            got = format_money(to_cents(price))
            if got != "$" + price:
                return describe("price " + price, got, "$" + price)
        return None

    grade("Prices up to $9,999.99 round-trip (2,005 prices)", "A+D", 10,
          check_large_prices)

    # 3. Anchors: the exact values promised in the docstrings.
    def check_anchors():
        pairs = ((to_cents("4.99"), 499),
                 (to_cents("0.07"), 7),
                 (read_quantity("0xC"), 12),
                 (read_quantity("0b0"), 0),
                 (line_total(199, 4), 796),
                 (line_total(199, 5), 796),
                 (line_total(250, 10), 2000),
                 (format_money(499), "$4.99"),
                 (format_money(7), "$0.07"),
                 (format_money(0), "$0.00"),
                 (format_money(123456), "$1234.56"),
                 (format_money(line_total(to_cents("2.50"), read_quantity("0x0A"))),
                  "$20.00"))
        for got, want in pairs:
            if got != want:
                return describe("docstring example", got, want)
        return None

    grade("Docstring examples produce the promised values", "A+B+C+D", 10,
          check_anchors)

    # 4. Every quantity 0-255, in all four numeral systems, drives the same total.
    def check_numeral_systems():
        for price in ("0.99", "1.15", "2.05", "13.37"):
            unit = to_cents(price)
            if type(unit) is not int or unit <= 0:
                return describe('to_cents("' + price + '")', unit, "a positive int")
            if line_total(unit, 1) != unit:
                return describe("one item at $" + price, line_total(unit, 1), unit)
            for n in range(0, 256):
                totals = [line_total(unit, read_quantity(code)) for code in all_codes(n)]
                if len(set(totals)) != 1:
                    return ("quantity " + str(n) + " at $" + price
                            + " gave different totals per numeral system: " + repr(totals))
        return None

    grade("All four numeral systems agree (256 quantities)", "A+B+C", 10,
          check_numeral_systems)

    # 5. The buy-4-get-1-free rule, for every quantity, fed by the parsers.
    def check_free_item_rule():
        for price in ("0.29", "1.99", "10.10", "99.99"):
            unit = to_cents(price)
            if line_total(unit, read_quantity("0")) != 0:
                return "$" + price + " x0 should cost nothing"
            for n in range(1, 201):
                got = line_total(unit, read_quantity(str(n)))
                previous = line_total(unit, read_quantity(str(n - 1)))
                want = previous if n % 5 == 0 else previous + unit
                if got != want:
                    return describe("$" + price + " x" + str(n), got, want)
        return None

    grade("Free-item rule holds for every quantity 0-200", "A+B+C", 10,
          check_free_item_rule)

    # 6. Every real order total is formatted as valid, exact money.
    def check_formatted_totals():
        for cents in range(0, 10000, 37):
            price = price_at(cents)
            for n in (0, 1, 4, 5, 9, 10, 31, 255):
                total = line_total(to_cents(price), read_quantity(hex(n)))
                problem = money_problem(format_money(total), total)
                if problem is not None:
                    return "$" + price + " x" + str(n) + ": " + problem
        return None

    grade("Totals format correctly across a 2,160-order grid", "A+B+C+D", 10,
          check_formatted_totals)

    # 7. The full pipeline agrees with your own four functions, everywhere.
    def check_receipt_returned():
        for cents in range(0, 10000, 53):
            price = price_at(cents)
            for n in (0, 1, 4, 5, 6, 9, 10, 12, 31, 100, 255):
                code = all_codes(n)[n % 5]
                got = print_receipt_line("Taco", price, code)
                want = compose("Taco", price, code)
                if got != want:
                    return describe("Taco $" + price + " " + code, got, want)
        return None

    grade("Receipt line returned correctly (2,079 orders)", "A+B+C+D+E", 10,
          check_receipt_returned)

    # 8. The full pipeline's printed output, including sep= and end=.
    def check_receipt_printed():
        for cents in range(0, 10000, 613):
            price = price_at(cents)
            for n in (0, 5, 7, 10, 31):
                code = all_codes(n)[n % 5]
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    print_receipt_line("Nachos", price, code)
                got = buffer.getvalue()
                want = compose("Nachos", price, code) + "\n"
                if got != want:
                    return describe("printed line for $" + price + " x" + str(n),
                                    got, want)
        return None

    grade("Receipt line printed correctly (sep= and end=)", "A+B+C+D+E", 10,
          check_receipt_printed)

    # 9. Printed text and returned text must always be the same line.
    def check_printed_matches_returned():
        for cents in range(0, 10000, 421):
            price = price_at(cents)
            for n in (0, 3, 5, 17, 64):
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    returned = print_receipt_line("Sub", price, oct(n))
                printed = buffer.getvalue()
                if type(returned) is not str or printed != returned + "\n":
                    return ("for Sub $" + price + " x" + str(n)
                            + " printed " + repr(printed)
                            + " but returned " + repr(returned))
        return None

    grade("Printed text always matches returned text", "A+B+C+D+E", 10,
          check_printed_matches_returned)

    # 10. Anchors for the whole pipeline: the two lines promised in the docstring.
    def check_receipt_anchors():
        pairs = ((print_receipt_line("Taco", "1.99", "0b101"), "Taco | x5 | $7.96"),
                 (print_receipt_line("Nachos", "2.50", "0x0A"), "Nachos | x10 | $20.00"))
        for got, want in pairs:
            if got != want:
                return describe("docstring receipt line", got, want)
        return None

    grade("Docstring receipt lines are exactly right", "A+B+C+D+E", 10,
          check_receipt_anchors)

    # ------------------------------------------------------------------ #
    print()
    print("=" * 68)
    print("GROUP SCORE: " + str(score) + " / " + str(possible))
    if score == possible:
        print("All five functions work together, for every price. Ready to submit.")
    else:
        print("Not a perfect score yet - every check above needs several")
        print("functions to be correct, so start with the DIAGNOSTICS.")
    print("=" * 68)

    # ------------------------------------------------------------------ #
    # OPTIONAL DEMO - remove the # from each line below to run your register
    # live at the keyboard. Remember: input() always hands you a string.
    # ------------------------------------------------------------------ #
    # print()
    # item = input("Item name: ")
    # price = input("Price in dollars (e.g. 1.99): ")
    # code = input("Quantity code (e.g. 7, 0b101, 0o17, 0x1F): ")
    # print_receipt_line(item, price, code)
