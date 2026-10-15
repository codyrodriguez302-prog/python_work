"""
DEBUG RELAY
PCEP-30-02 Review (all sections)

Every function in this file has exactly ONE bug. The docstring under each
function name tells you what the function is SUPPOSED to do. Trust the
docstring, not the code.

HOW TO PLAY
  1. Type your team name on the TEAM_NAME line below.
  2. Split the 50 bugs among your team however you like.
  3. Find each bug and fix it. Most fixes change only 1-3 lines.
  4. Run this file to check your work:      python3 debug_relay.py
     See the full test for one bug:         python3 debug_relay.py 12
  5. Do not edit the docstrings or anything below the TEST CASES line.
     Your instructor grades with an untouched copy of the tests.

SCORING
  Bugs 1-10 are worth 1 point each, 11-20 are 2 points, 21-30 are 3,
  31-40 are 4, and 41-50 are 5 (150 points total). The team with the most
  points wins.
"""

TEAM_NAME = "Team ???"


# =====================================================================
# BUG 1                                                       1 point
# =====================================================================

def receipt_total(prices, tax_rate):
    """
    Add up every price in the list, skipping any negative price (those are
    scanner errors). Then add sales tax and round to 2 decimal places.

    Parameters:
        prices (list of float): item prices
        tax_rate (float): tax as a decimal, e.g. 0.0725 means 7.25%

    Returns:
        float: subtotal plus tax, rounded to 2 decimals

    Example:
        >>> receipt_total([10.00, 5.50, -3.00], 0.0725)
        16.62
        >>> receipt_total([100], 0.10)
        110.0
    """
    subtotal = 0
    for price in prices:
        if price >= 0:
            subtotal += price
    total = subtotal * (1 + tax_rate)
    return round(total, 2)


# =====================================================================
# BUG 2                                                       1 point
# =====================================================================

def count_vowels(text):
    """
    Count how many vowels (a, e, i, o, u) are in text. Uppercase and
    lowercase vowels both count.

    Parameters:
        text (str): any text

    Returns:
        int: number of vowels

    Example:
        >>> count_vowels("Bad Robots")
        3
        >>> count_vowels("")
        0
    """
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


# =====================================================================
# BUG 3                                                       1 point
# =====================================================================

def format_scoreboard(team, wins, losses):
    """
    Build a scoreboard line with the team name, wins-losses, and the win
    percentage rounded to 1 decimal place. A team with no games has 0.0%.

    Parameters:
        team (str): team name
        wins (int): games won
        losses (int): games lost

    Returns:
        str: the scoreboard line

    Example:
        >>> format_scoreboard("Team 1014", 8, 2)
        'Team 1014: 8-2 (80.0%)'
        >>> format_scoreboard("Team 42", 0, 0)
        'Team 42: 0-0 (0.0%)'
    """
    games = wins + losses
    if games == 0:
        percent = 0.0
    else:
        percent = round(wins / games * 100, 1)
    return team + ": " + str(wins) + "-" + str(losses) + " (" + str(percent) + "%)"


# =====================================================================
# BUG 4                                                       1 point
# =====================================================================

def is_strong_password(password):
    """
    A strong password has AT LEAST 8 characters, at least one digit, and
    at least one uppercase letter.

    Parameters:
        password (str)

    Returns:
        bool: True if the password is strong

    Example:
        >>> is_strong_password("Robot101")
        True
        >>> is_strong_password("robot101")
        False
    """
    if len(password) < 8:
        return False
    has_digit = False
    has_upper = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True
    return has_digit and has_upper


# =====================================================================
# BUG 5                                                       1 point
# =====================================================================

def class_average(grades):
    """
    Return the average of the grades rounded to 1 decimal place. Any grade
    above 100 counts as 100. Return 0.0 for an empty list.

    Parameters:
        grades (list of int)

    Returns:
        float: the average

    Example:
        >>> class_average([88, 92, 79])
        86.3
        >>> class_average([105, 95])
        97.5
    """
    if len(grades) == 0:
        return 0.0
    total = 0
    for g in grades:
        if g > 100:
            g = 100
        total += g
    return round(total / len(grades), 1)


# =====================================================================
# BUG 6                                                       1 point
# =====================================================================

def make_username(first, last, grad_year):
    """
    Build a school username: first initial + full last name + the last two
    digits of the graduation year. Spaces are removed and the whole
    username is lowercase.

    Parameters:
        first (str): first name
        last (str): last name (may contain spaces)
        grad_year (int): four-digit graduation year

    Returns:
        str: the username

    Example:
        >>> make_username("Ada", "Lovelace", 2027)
        'alovelace27'
        >>> make_username("Mary Kate", "Van Dyke", 2028)
        'mvandyke28'
    """
    initial = first[0]
    year_part = str(grad_year)[2:]
    username = (initial + last.replace(" ", "") + year_part).lower()
    return username


# =====================================================================
# BUG 7                                                       1 point
# =====================================================================

def find_highest_score(scores):
    """
    Return the highest score in the list WITHOUT using max().
    Return None if the list is empty.

    Parameters:
        scores (list of int): the scores

    Returns:
        int or None: the highest score

    Example:
        >>> find_highest_score([70, 95, 88])
        95
    """
    if len(scores) == 0:
        return None
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest


# =====================================================================
# BUG 8                                                       1 point
# =====================================================================

def countdown(start):
    """
    Return a list counting down from start to 1, followed by "Liftoff!".
    If start is less than 1, return ["Scrubbed"].

    Parameters:
        start (int): the first number

    Returns:
        list: the countdown

    Example:
        >>> countdown(3)
        [3, 2, 1, 'Liftoff!']
        >>> countdown(0)
        ['Scrubbed']
    """
    if start < 1:
        return ["Scrubbed"]
    result = []
    for n in range(start ,0, -1):
        result.append(n)
    result.append("Liftoff!")
    return result


# =====================================================================
# BUG 9                                                       1 point
# =====================================================================

def inventory_value(inventory):
    """
    inventory is a dictionary: item name -> (quantity, price each).
    Return the total value of everything in stock, rounded to 2 decimals.

    Parameters:
        inventory (dict): str -> (int, float)

    Returns:
        float: total value

    Example:
        >>> inventory_value({"bolt": (100, 0.25), "nut": (50, 0.10)})
        30.0
    """
    total = 0
    for item in inventory:
        quantity, price = inventory[item]
        total += quantity * price
    return round(total, 2)


# =====================================================================
# BUG 10                                                      1 point
# =====================================================================

def grade_letter(score):
    """
    Convert a numeric score to a letter grade:
        90-100 A    80-89 B    70-79 C    60-69 D    below 60 F
    Scores below 0 or above 100 return "Invalid".

    Parameters:
        score (float)

    Returns:
        str: "A", "B", "C", "D", "F", or "Invalid"

    Example:
        >>> grade_letter(85)
        'B'
        >>> grade_letter(101)
        'Invalid'
    """
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# =====================================================================
# BUG 11                                                     2 points
# =====================================================================

def total_minutes(durations):
    """
    Add up a list of time durations written as "H:MM" strings and return
    the total number of minutes.

    Parameters:
        durations (list of str): times like "1:30" (1 hour 30 minutes)

    Returns:
        int: total minutes

    Example:
        >>> total_minutes(["1:30", "0:45", "2:05"])
        260
        >>> total_minutes([])
        0
    """
    total = 0
    for d in durations:
        hours, minutes = d.split(":")
        total += int(hours) * 60 + int(minutes)
        continue
    return total


# =====================================================================
# BUG 12                                                     2 points
# =====================================================================

def sum_of_multiples(n, limit):
    """
    Add up every multiple of n from n up to AND INCLUDING limit.
    If n is 0 or negative, return 0.

    Parameters:
        n (int): the number to take multiples of
        limit (int): the largest number allowed

    Returns:
        int: the sum

    Example:
        >>> sum_of_multiples(5, 15)
        30
        >>> sum_of_multiples(3, 10)
        18
    """
    if n <= 0:
        return 0
    total = 0
    for i in range(n, limit + 1, n):
        total+= i
    return total


# =====================================================================
# BUG 13                                                     2 points
# =====================================================================

def row_totals(grid):
    """
    grid is a list of rows, and each row is a list of numbers.
    Return a list holding the total of each row.

    Parameters:
        grid (list of list of int)

    Returns:
        list of int: one total per row

    Example:
        >>> row_totals([[1, 2, 3], [4, 5], [10]])
        [6, 9, 10]
    """
    totals = []
    for row in grid:
        row_sum = 0
        for value in row:
            row_sum += value
        totals.append(row_sum)
    return totals


# =====================================================================
# BUG 14                                                     2 points
# =====================================================================

def make_change(cents):
    """
    Return the fewest coins for an amount of cents as a list:
    [quarters, dimes, nickels, pennies]. Every value must be a whole
    number (int).

    Parameters:
        cents (int): 0 or more

    Returns:
        list of int: [quarters, dimes, nickels, pennies]

    Example:
        >>> make_change(68)
        [2, 1, 1, 3]
    """
    quarters = cents // 25
    cents = cents % 25
    dimes = cents // 10
    cents = cents % 10
    nickels = cents // 5
    pennies = cents % 5
    return [quarters, dimes, nickels, pennies]


# =====================================================================
# BUG 15                                                     2 points
# =====================================================================

def combine_scores(score_lists):
    """
    score_lists is a list of lists of scores (one list per class period).
    Combine every score into ONE flat list, sorted from highest to lowest.

    Parameters:
        score_lists (list of list of int)

    Returns:
        list of int: every score, highest first

    Example:
        >>> combine_scores([[88, 92], [75], [99, 60]])
        [99, 92, 88, 75, 60]
    """
    all_scores = []
    for scores in score_lists:
        for num in scores:
            all_scores.append(num)
    all_scores.sort(reverse=True)
    return all_scores


# =====================================================================
# BUG 16                                                     2 points
# =====================================================================

def tally_votes(votes):
    """
    Count votes. Names count as the same vote no matter how they are
    capitalized or spaced ("  ada " and "Ada" are the same person).

    Parameters:
        votes (list of str): one name per vote

    Returns:
        dict: name in Title Case -> number of votes

    Example:
        >>> tally_votes(["ada", "Linus", " ADA ", "grace"])
        {'Ada': 2, 'Linus': 1, 'Grace': 1}
    """
    counts = {}
    for vote in votes:
        name = vote.strip().title()
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    return counts


# =====================================================================
# BUG 17                                                     2 points
# =====================================================================

def middle_three(word):
    """
    Return the middle three characters of a word. If the word is shorter
    than 3 characters or has an even length, return the word unchanged.

    Parameters:
        word (str): any word

    Returns:
        str: the middle three characters, or the original word

    Example:
        >>> middle_three("program")
        'ogr'
        >>> middle_three("robotics")
        'robotics'
    """
    if len(word) < 3 or len(word) % 2 == 0:
        return word
    middle = len(word) // 2
    return word[middle - 1:middle + 2]


# =====================================================================
# BUG 18                                                     2 points
# =====================================================================

def initials(full_name):
    """
    Return the initials of a name in uppercase, each followed by a period.
    Extra spaces between words are ignored.

    Parameters:
        full_name (str): a person's name

    Returns:
        str: the initials

    Example:
        >>> initials("grace brewster hopper")
        'G.B.H.'
        >>> initials("  alan   turing ")
        'A.T.'
    """
    result = ""
    for part in full_name.split():
        result += part[0].upper() + "."
    return result


# =====================================================================
# BUG 19                                                     2 points
# =====================================================================

def first_failure(results):
    """
    results is a list of "pass" / "fail" strings from a test run. Return
    the position (index) of the FIRST "fail". If nothing failed, return -1.

    Parameters:
        results (list of str)

    Returns:
        int: index of the first "fail", or -1

    Example:
        >>> first_failure(["pass", "fail", "pass", "fail"])
        1
        >>> first_failure(["pass", "pass"])
        -1
    """
    position = -1
    for i in range(len(results)):
        if results[i] == "fail":
            position = i
            break
    return position


# =====================================================================
# BUG 20                                                     2 points
# =====================================================================

def digit_sum(number):
    """
    Return the sum of the digits of a whole number. Negative numbers are
    treated as positive.

    Parameters:
        number (int)

    Returns:
        int: the sum of the digits

    Example:
        >>> digit_sum(1014)
        6
        >>> digit_sum(-25)
        7
    """
    if number < 0:
        number = -number
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


# =====================================================================
# BUG 21                                                     3 points
# =====================================================================

def bad_robots(n):
    """
    Build a list for the numbers 1 through n (including n):
      - multiples of BOTH 3 and 5 become "BadRobots"
      - other multiples of 3 become "Bad"
      - other multiples of 5 become "Robots"
      - every other number stays a number

    Parameters:
        n (int): the last number

    Returns:
        list: numbers and strings as described

    Example:
        >>> bad_robots(5)
        [1, 2, 'Bad', 4, 'Robots']
        >>> bad_robots(15)[-1]
        'BadRobots'
    """
    result = []
    for i in range(1, n +1):
        if i % 15 == 0:
            result.append("BadRobots")
        elif i % 5 == 0:
            result.append("Robots")
        elif i % 3 ==0:
            result.append("Bad")
        else:
            result.append(i)
    return result


# =====================================================================
# BUG 22                                                     3 points
# =====================================================================

def can_operate_machine(age, trained, supervisor_present):
    """
    Shop safety rule. A student can run the machine only if ALL are true:
      - they are at least 14 years old
      - they have finished safety training
      - they are 18 or older, OR a supervisor is present

    Parameters:
        age (int)
        trained (bool)
        supervisor_present (bool)

    Returns:
        bool: True if allowed

    Example:
        >>> can_operate_machine(16, True, True)
        True
        >>> can_operate_machine(16, False, True)
        False
    """
    if age < 14:
        return False
    if trained==False:
        return False
    if age >=14 and trained and age >= 18 or supervisor_present:
        return True
    return False


# =====================================================================
# BUG 23                                                     3 points
# =====================================================================

def largest_reading(readings):
    """
    readings is a list of sensor values stored as strings, e.g. "105".
    Entries equal to "ERR" must be skipped. Return the largest reading as
    an int, or None if there are no valid readings.

    Parameters:
        readings (list of str)

    Returns:
        int or None: the largest reading

    Example:
        >>> largest_reading(["12", "ERR", "9", "105"])
        105
    """
    largest = None
    for r in readings:
        if r == "ERR":
            continue
        value = int(r.strip())
        if largest is None or value > largest:
            largest = value
    if largest is None:
        return None
    return int(largest)


# =====================================================================
# BUG 24                                                     3 points
# =====================================================================

def find_row(rows, needed):
    """
    rows is a list where each number is how many empty seats are in that
    row. Return the index of the FIRST row with at least `needed` empty
    seats. If no row has enough, return "Sold out".

    Parameters:
        rows (list of int)
        needed (int)

    Returns:
        int or str: the row index, or "Sold out"

    Example:
        >>> find_row([2, 0, 5, 8], 4)
        2
        >>> find_row([1, 1], 3)
        'Sold out'
    """
    for i in range(len(rows)):
        if rows[i] >= needed:
            break
        else:
            return "Sold out"
    return i


# =====================================================================
# BUG 25                                                     3 points
# =====================================================================

def is_palindrome(phrase):
    """
    Return True if phrase reads the same forward and backward, ignoring
    uppercase/lowercase and anything that is not a letter.

    Parameters:
        phrase (str)

    Returns:
        bool

    Example:
        >>> is_palindrome("Never odd or even")
        True
        >>> is_palindrome("Bad Robots")
        False
    """
    cleaned = ""
    for ch in phrase.lower():
        if ch.isalpha():
            cleaned += ch
    return cleaned == cleaned[::1]


# =====================================================================
# BUG 26                                                     3 points
# =====================================================================

def get_domain(email):
    """
    Return the domain part of an email address (everything after the "@"),
    in lowercase with spaces at the ends removed. If there is no "@",
    return an empty string.

    Parameters:
        email (str): an email address

    Returns:
        str: the domain, or "" if there is no "@"

    Example:
        >>> get_domain("  Nat@Tolles.ORG ")
        'tolles.org'
        >>> get_domain("not-an-email")
        ''
    """
    email = email.strip().lower()
    at = email.find("@")
    if at == 0:
        return ""
    return email[at + 1:]


# =====================================================================
# BUG 27                                                     3 points
# =====================================================================

def closest_robot(robots):
    """
    robots is a list of (name, distance) tuples. Return the NAME of the
    robot with the smallest distance. Return None if the list is empty.

    Parameters:
        robots (list of tuple): each tuple is (name, distance)

    Returns:
        str or None: name of the closest robot

    Example:
        >>> closest_robot([("Atlas", 12.5), ("Bolt", 3.0), ("Cog", 7.2)])
        'Bolt'
    """
    best_name = None
    best_distance = None
    for distance, name in robots:
        if best_distance is None or distance < best_distance:
            best_distance = distance
            best_name = name
    return best_name


# =====================================================================
# BUG 28                                                     3 points
# =====================================================================

def find_owner(lockers, item):
    """
    lockers is a dictionary: locker number -> list of items inside.
    Return the locker number that contains item, or None if no locker has
    it. Matching ignores uppercase/lowercase.

    Parameters:
        lockers (dict): int -> list of str
        item (str): the item to find

    Returns:
        int or None: the locker number

    Example:
        >>> find_owner({101: ["laptop", "hoodie"], 102: ["Calculator"]}, "calculator")
        102
    """
    target = item.lower()
    for number in lockers:
        contents = []
        for thing in lockers[number]:
            contents.append(thing.lower())
        if target in lockers:
            return number
    return None


# =====================================================================
# BUG 29                                                     3 points
# =====================================================================

def print_launch(n):
    """
    PRINT (not return) a countdown from n down to 1 on ONE line, with
    " - " between the numbers, followed by "GO!".

    Parameters:
        n (int)

    Returns:
        None

    Example:
        >>> print_launch(3)
        3 - 2 - 1 - GO!
    """
    for i in range(n, 0, -1):
        print(i, sep=" - ")
    print("GO!")


# =====================================================================
# BUG 30                                                     3 points
# =====================================================================

def longest_streak(results):
    """
    results is a list of "W" (win) and "L" (loss). Return the length of
    the longest run of wins in a row.

    Parameters:
        results (list of str)

    Returns:
        int: the longest winning streak

    Example:
        >>> longest_streak(["W", "W", "L", "W", "W", "W"])
        3
        >>> longest_streak(["L", "L"])
        0
    """
    longest = 0
    current = 0
    for r in results:
        if r == "W":
            current += 1
        else:
            if current > longest:
                longest = current
            current = 0
    return longest


# =====================================================================
# BUG 31                                                     4 points
# =====================================================================

def apply_curve(scores, bonus):
    """
    Return a NEW list where every score has the bonus added. No score can
    go above 100. The original list must NOT be changed.

    Parameters:
        scores (list of int): original scores
        bonus (int): points to add

    Returns:
        list of int: the curved scores

    Example:
        >>> apply_curve([70, 95, 88], 10)
        [80, 100, 98]
    """
    curved = scores
    for i in range(len(curved)):
        curved[i] = curved[i] + bonus
        if curved[i] > 100:
            curved[i] = 100
    return curved


# =====================================================================
# BUG 32                                                     4 points
# =====================================================================

def move_robot(position, commands):
    """
    position is an (x, y) tuple. commands is a string of letters:
        N = y + 1,  S = y - 1,  E = x + 1,  W = x - 1
    Any other character is ignored. Return the final position as an
    (x, y) tuple.

    Parameters:
        position (tuple): starting (x, y)
        commands (str): movement letters

    Returns:
        tuple: final (x, y)

    Example:
        >>> move_robot((0, 0), "NNE")
        (1, 2)
        >>> move_robot((5, 5), "W?SS")
        (4, 3)
    """
    current = position
    for c in commands:
        if c == "N":
            current[1] += 1
        elif c == "S":
            current[1] -= 1
        elif c == "E":
            current[0] += 1
        elif c == "W":
            current[0] -= 1
    return (current[0], current[1])


# =====================================================================
# BUG 33                                                     4 points
# =====================================================================

def clean_tag(tag):
    """
    Turn a messy hashtag into a clean tag: remove spaces at both ends,
    make it lowercase, remove every "#", and replace the spaces left
    inside with "-".

    Parameters:
        tag (str): the messy tag

    Returns:
        str: the clean tag

    Example:
        >>> clean_tag("  #Bad Robots ")
        'bad-robots'
    """
    tag = tag.strip()
    tag.lower()
    tag = tag.replace("#", "")
    tag = tag.replace(" ", "-")
    return tag


# =====================================================================
# BUG 34                                                     4 points
# =====================================================================

def compound_interest(principal, rate, years):
    """
    Return how much money you will have after `years` years if
    `principal` grows by `rate` (a decimal) each year:
        amount = principal times (1 + rate) to the power of years
    Round to 2 decimals. If any input is negative, return None.

    Parameters:
        principal (float), rate (float), years (int)

    Returns:
        float or None

    Example:
        >>> compound_interest(1000, 0.05, 2)
        1102.5
    """
    if principal < 0 or rate < 0 or years < 0:
        return None
    amount = principal * 1 + rate ** years
    return round(amount, 2)


# =====================================================================
# BUG 35                                                     4 points
# =====================================================================

visitor_count = 0


def log_visitor(name):
    """
    Add 1 to the GLOBAL variable visitor_count (defined above this
    function), then return a welcome message using the new count.

    Parameters:
        name (str)

    Returns:
        str: the welcome message

    Example:
        >>> log_visitor("Nat")
        'Welcome, Nat! You are visitor #1'
        >>> log_visitor("Sam")
        'Welcome, Sam! You are visitor #2'
    """
    visitor_count += 1
    return "Welcome, " + name + "! You are visitor #" + str(visitor_count)


# =====================================================================
# BUG 36                                                     4 points
# =====================================================================

def permissions_text(flags):
    """
    Show Linux-style permissions. flags is a number from 0 to 7 where each
    binary bit means:
        4 (0b100) = read "r"    2 (0b010) = write "w"    1 (0b001) = execute "x"
    A missing permission is shown as "-".

    Parameters:
        flags (int): 0 through 7

    Returns:
        str: three characters such as "rw-"

    Example:
        >>> permissions_text(6)
        'rw-'
        >>> permissions_text(0b101)
        'r-x'
    """
    text = ""
    if flags & 4:
        text += "r"
    else:
        text += "-"
    if flags & 2:
        text += "w"
    else:
        text += "-"
    if flags and 1:
        text += "x"
    else:
        text += "-"
    return text


# =====================================================================
# BUG 37                                                     4 points
# =====================================================================

def safe_divide_all(pairs):
    """
    pairs is a list of (a, b) tuples. Divide a by b for each pair and
    return a list of the answers. If a division fails:
      - dividing by zero adds the string "div by zero"
      - any other error adds the string "error"

    Parameters:
        pairs (list of tuple): (a, b) pairs

    Returns:
        list: answers and/or error strings

    Example:
        >>> safe_divide_all([(10, 4), (5, 0), (3, "a")])
        [2.5, 'div by zero', 'error']
    """
    results = []
    for a, b in pairs:
        try:
            results.append(a / b)
        except Exception:
            results.append("error")
        except ZeroDivisionError:
            results.append("div by zero")
    return results


# =====================================================================
# BUG 38                                                     4 points
# =====================================================================

def top_three(scores):
    """
    Return a list of the three highest scores, highest first. Negative
    scores are invalid and are ignored. If there are fewer than three
    valid scores, return all of them, highest first.

    Parameters:
        scores (list of int)

    Returns:
        list of int: up to three scores

    Example:
        >>> top_three([72, 99, 85, 91, 60])
        [99, 91, 85]
    """
    valid = []
    for s in scores:
        if s >= 0:
            valid.append(s)
    ranked = valid.sort(reverse=True)
    return ranked[:3]


# =====================================================================
# BUG 39                                                     4 points
# =====================================================================

def count_digit(number, digit):
    """
    RECURSIVE: return how many times `digit` (0-9) appears in the
    non-negative whole number `number`.

    Parameters:
        number (int), digit (int)

    Returns:
        int: how many times digit appears

    Example:
        >>> count_digit(1014, 1)
        2
        >>> count_digit(7, 3)
        0
    """
    if number < 10:
        if number == digit:
            return 1
        return 0
    last = number % 10
    rest = number // 10
    if last == digit:
        return 1 + count_digit(rest, digit)
    count_digit(rest, digit)


# =====================================================================
# BUG 40                                                     4 points
# =====================================================================

def remove_out_of_stock(inventory):
    """
    inventory is a dictionary: item name -> quantity. Remove every item
    whose quantity is 0 or less, then return the dictionary.

    Parameters:
        inventory (dict): str -> int

    Returns:
        dict: the same dictionary with empty items removed

    Example:
        >>> remove_out_of_stock({"bolt": 40, "nut": 0, "gear": 3})
        {'bolt': 40, 'gear': 3}
    """
    for item in inventory:
        if inventory[item] <= 0:
            del inventory[item]
    return inventory


# =====================================================================
# BUG 41                                                     5 points
# =====================================================================

def fibonacci_up_to(limit):
    """
    GENERATOR: yield every Fibonacci number that is less than or equal to
    limit. The sequence starts 0, 1, 1, 2, 3, 5, 8, ... where each number
    is the sum of the two numbers before it.

    Parameters:
        limit (int): the largest value allowed

    Yields:
        int: the next Fibonacci number

    Example:
        >>> list(fibonacci_up_to(10))
        [0, 1, 1, 2, 3, 5, 8]
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a = b
        b = a + b


# =====================================================================
# BUG 42                                                     5 points
# =====================================================================

def add_to_queue(student, queue=[]):
    """
    Add a student's name to the end of a help queue and return the queue.
    A name already in the queue is not added again. If no queue is passed
    in, a brand-new empty queue is started EVERY time.

    Parameters:
        student (str): the name to add
        queue (list): an existing queue (optional)

    Returns:
        list: the queue

    Example:
        >>> add_to_queue("Ben", ["Ann"])
        ['Ann', 'Ben']
        >>> add_to_queue("Cal")
        ['Cal']
        >>> add_to_queue("Dee")
        ['Dee']
    """
    if student not in queue:
        queue.append(student)
    return queue


# =====================================================================
# BUG 43                                                     5 points
# =====================================================================

def reserve_seats(rows, cols, reserved):
    """
    Build a seating chart with the given number of rows and columns where
    every seat starts as "open". Then mark each (row, col) in reserved as
    "taken". Return the chart as a list of row lists.

    Parameters:
        rows (int), cols (int)
        reserved (list of tuple): (row, col) seats to mark taken

    Returns:
        list of list of str: the seating chart

    Example:
        >>> reserve_seats(2, 3, [(0, 1)])
        [['open', 'taken', 'open'], ['open', 'open', 'open']]
    """
    chart = [["open"] * cols] * rows
    for r, c in reserved:
        chart[r][c] = "taken"
    return chart


# =====================================================================
# BUG 44                                                     5 points
# =====================================================================

def check_payment(paid, prices):
    """
    Compare the amount paid with the total of the prices. Money is only
    measured to the cent. Return:
      - "exact"       if paid equals the total
      - "short X"     if paid is less  (X = amount still owed)
      - "change X"    if paid is more  (X = change to give back)
    X is rounded to 2 decimals.

    Parameters:
        paid (float)
        prices (list of float)

    Returns:
        str

    Example:
        >>> check_payment(0.30, [0.10, 0.20])
        'exact'
        >>> check_payment(5, [1.25, 1.25])
        'change 2.5'
    """
    total = 0
    for p in prices:
        total += p
    if paid == total:
        return "exact"
    elif paid < total:
        return "short " + str(round(total - paid, 2))
    else:
        return "change " + str(round(paid - total, 2))


# =====================================================================
# BUG 45                                                     5 points
# =====================================================================

def bucket_temperatures(temps, size):
    """
    Sort temperatures into buckets of width `size`. A bucket is named by
    its LOWEST value, which is always a multiple of size. With size 10:
    -3 goes in bucket -10, 4 goes in bucket 0, 15 goes in bucket 10.
    Return a dictionary: bucket -> how many temperatures are in it.

    Parameters:
        temps (list of int)
        size (int): bucket width, greater than 0

    Returns:
        dict: int -> int

    Example:
        >>> bucket_temperatures([-3, 4, 15, 18], 10)
        {-10: 1, 0: 1, 10: 2}
    """
    buckets = {}
    for t in temps:
        start = int(t / size) * size
        if start in buckets:
            buckets[start] += 1
        else:
            buckets[start] = 1
    return buckets


# =====================================================================
# BUG 46                                                     5 points
# =====================================================================

def resolve_settings(user, defaults):
    """
    Build the final settings for a program. For every key in defaults, use
    the user's value if the user dictionary has that key -- EVEN IF the
    user's value is 0, False, or "" -- otherwise use the default value.

    Parameters:
        user (dict): settings the user chose
        defaults (dict): every setting with its default value

    Returns:
        dict: one value for every key in defaults

    Example:
        >>> resolve_settings({"volume": 0}, {"volume": 50, "theme": "dark"})
        {'volume': 0, 'theme': 'dark'}
    """
    final = {}
    for key in defaults:
        final[key] = user.get(key) or defaults[key]
    return final


# =====================================================================
# BUG 47                                                     5 points
# =====================================================================

def round_scores(scores):
    """
    Round every score to the nearest whole number, where .5 ALWAYS rounds
    UP (89.5 -> 90, 72.5 -> 73). Scores are never negative. A score of
    None means the student was absent and becomes the string "ABS".

    Parameters:
        scores (list): floats and/or None

    Returns:
        list: ints and/or "ABS"

    Example:
        >>> round_scores([89.5, 90.4, 72.5])
        [90, 90, 73]
        >>> round_scores([None, 84.5])
        ['ABS', 85]
    """
    rounded = []
    for s in scores:
        if s is None:
            rounded.append("ABS")
        else:
            rounded.append(round(s))
    return rounded


# =====================================================================
# BUG 48                                                     5 points
# =====================================================================

def parse_ages(entries):
    """
    entries is a list of strings typed in by users. Convert each one to an
    int. Entries that cannot be converted are skipped and counted as
    errors. Return a tuple: (list of valid ages, number of errors).

    Parameters:
        entries (list of str)

    Returns:
        tuple: (list of int, int)

    Example:
        >>> parse_ages(["15", "abc", "17"])
        ([15, 17], 1)
        >>> parse_ages(["x", "16"])
        ([16], 1)
    """
    valid = []
    errors = 0
    for entry in entries:
        try:
            age = int(entry)
        except ValueError:
            errors += 1
        valid.append(age)
    return (valid, errors)


# =====================================================================
# BUG 49                                                     5 points
# =====================================================================

def binary_string(n):
    """
    RECURSIVE: convert a non-negative whole number to its binary string
    without using bin().

    Parameters:
        n (int): 0 or more

    Returns:
        str: the binary digits

    Example:
        >>> binary_string(5)
        '101'
        >>> binary_string(0)
        '0'
    """
    if n == 0:
        return "0"
    return binary_string(n // 2) + str(n % 2)


# =====================================================================
# BUG 50                                                     5 points
# =====================================================================

def reset_scores(scoreboard):
    """
    scoreboard is a list of [name, score] lists. Return a NEW scoreboard
    with every score set to 0. The original scoreboard must NOT change.

    Parameters:
        scoreboard (list of list)

    Returns:
        list of list: the reset scoreboard

    Example:
        >>> reset_scores([["Ann", 12], ["Ben", 30]])
        [['Ann', 0], ['Ben', 0]]
    """
    new_board = scoreboard[:]
    for entry in new_board:
        entry[1] = 0
    return new_board


# =====================================================================
#  TEST CASES  -  DO NOT EDIT ANYTHING BELOW THIS LINE
# =====================================================================

import io
import sys

TESTS = [
    # (bug number, function name, points, [(test, expected answer), ...])
    (1, 'receipt_total', 1, [
        ('receipt_total([10.00, 5.50, -3.00], 0.0725)', 16.62),
        ('receipt_total([100], 0.10)', 110.0),
        ('receipt_total([-5, -1], 0.07)', 0),
        ('receipt_total([19.99, 5.01], 0.06)', 26.5),
    ]),
    (2, 'count_vowels', 1, [
        ("count_vowels('Bad Robots')", 3),
        ("count_vowels('')", 0),
        ("count_vowels('AEIOU xyz')", 5),
        ("count_vowels('rhythm')", 0),
    ]),
    (3, 'format_scoreboard', 1, [
        ("format_scoreboard('Team 1014', 8, 2)", 'Team 1014: 8-2 (80.0%)'),
        ("format_scoreboard('Team 42', 0, 0)", 'Team 42: 0-0 (0.0%)'),
        ("format_scoreboard('Bots', 1, 2)", 'Bots: 1-2 (33.3%)'),
    ]),
    (4, 'is_strong_password', 1, [
        ("is_strong_password('Robot101')", True),
        ("is_strong_password('robot101')", False),
        ("is_strong_password('Short1A')", False),
        ("is_strong_password('BadRobots1014')", True),
        ("is_strong_password('NODIGITSHERE')", False),
    ]),
    (5, 'class_average', 1, [
        ('class_average([88, 92, 79])', 86.3),
        ('class_average([105, 95])', 97.5),
        ('class_average([])', 0.0),
        ('class_average([70, 75])', 72.5),
    ]),
    (6, 'make_username', 1, [
        ("make_username('Ada', 'Lovelace', 2027)", 'alovelace27'),
        ("make_username('Mary Kate', 'Van Dyke', 2028)", 'mvandyke28'),
        ("make_username('grace', 'HOPPER', 2030)", 'ghopper30'),
    ]),
    (7, 'find_highest_score', 1, [
        ('find_highest_score([70, 95, 88])', 95),
        ('find_highest_score([])', None),
        ('find_highest_score([-5, -2, -9])', -2),
        ('find_highest_score([42])', 42),
    ]),
    (8, 'countdown', 1, [
        ('countdown(3)', [3, 2, 1, 'Liftoff!']),
        ('countdown(1)', [1, 'Liftoff!']),
        ('countdown(0)', ['Scrubbed']),
        ('countdown(-4)', ['Scrubbed']),
    ]),
    (9, 'inventory_value', 1, [
        ("inventory_value({'bolt': (100, 0.25), 'nut': (50, 0.10)})", 30.0),
        ('inventory_value({})', 0),
        ("inventory_value({'motor': (2, 49.99)})", 99.98),
        ("inventory_value({'gear': (0, 12.0), 'belt': (3, 4.5)})", 13.5),
    ]),
    (10, 'grade_letter', 1, [
        ('grade_letter(85)', 'B'),
        ('grade_letter(101)', 'Invalid'),
        ('grade_letter(75)', 'C'),
        ('grade_letter(60)', 'D'),
        ('grade_letter(59.9)', 'F'),
        ('grade_letter(-1)', 'Invalid'),
    ]),
    (11, 'total_minutes', 2, [
        ("total_minutes(['1:30', '0:45', '2:05'])", 260),
        ('total_minutes([])', 0),
        ("total_minutes(['0:59', '0:01'])", 60),
        ("total_minutes(['3:00'])", 180),
    ]),
    (12, 'sum_of_multiples', 2, [
        ('sum_of_multiples(5, 15)', 30),
        ('sum_of_multiples(3, 10)', 18),
        ('sum_of_multiples(7, 7)', 7),
        ('sum_of_multiples(0, 10)', 0),
    ]),
    (13, 'row_totals', 2, [
        ('row_totals([[1, 2, 3], [4, 5], [10]])', [6, 9, 10]),
        ('row_totals([])', []),
        ('row_totals([[5]])', [5]),
        ('row_totals([[1, 1], [2, 2], []])', [2, 4, 0]),
    ]),
    (14, 'make_change', 2, [
        ('make_change(68)', [2, 1, 1, 3]),
        ('make_change(99)', [3, 2, 0, 4]),
        ('make_change(0)', [0, 0, 0, 0]),
        ('make_change(41)', [1, 1, 1, 1]),
    ]),
    (15, 'combine_scores', 2, [
        ('combine_scores([[88, 92], [75], [99, 60]])', [99, 92, 88, 75, 60]),
        ('combine_scores([])', []),
        ('combine_scores([[5], []])', [5]),
        ('combine_scores([[1, 2, 3]])', [3, 2, 1]),
    ]),
    (16, 'tally_votes', 2, [
        ("tally_votes(['ada', 'Linus', ' ADA ', 'grace'])", {'Ada': 2, 'Linus': 1, 'Grace': 1}),
        ('tally_votes([])', {}),
        ("tally_votes(['bo', 'BO', 'Bo', 'bO'])", {'Bo': 4}),
    ]),
    (17, 'middle_three', 2, [
        ("middle_three('program')", 'ogr'),
        ("middle_three('robotics')", 'robotics'),
        ("middle_three('cat')", 'cat'),
        ("middle_three('hi')", 'hi'),
    ]),
    (18, 'initials', 2, [
        ("initials('grace brewster hopper')", 'G.B.H.'),
        ("initials('  alan   turing ')", 'A.T.'),
        ("initials('Ada')", 'A.'),
        ("initials('J R R Tolkien')", 'J.R.R.T.'),
    ]),
    (19, 'first_failure', 2, [
        ("first_failure(['pass', 'fail', 'pass', 'fail'])", 1),
        ("first_failure(['pass', 'pass'])", -1),
        ("first_failure(['fail', 'fail'])", 0),
        ('first_failure([])', -1),
    ]),
    (20, 'digit_sum', 2, [
        ('digit_sum(1014)', 6),
        ('digit_sum(-25)', 7),
        ('digit_sum(0)', 0),
        ('digit_sum(9)', 9),
        ('digit_sum(99999)', 45),
    ]),
    (21, 'bad_robots', 3, [
        ('bad_robots(5)', [1, 2, 'Bad', 4, 'Robots']),
        ('bad_robots(15)[-1]', 'BadRobots'),
        ("bad_robots(30).count('BadRobots')", 2),
        ('bad_robots(0)', []),
    ]),
    (22, 'can_operate_machine', 3, [
        ('can_operate_machine(16, True, True)', True),
        ('can_operate_machine(16, False, True)', False),
        ('can_operate_machine(19, True, False)', True),
        ('can_operate_machine(13, True, True)', False),
        ('can_operate_machine(17, True, False)', False),
    ]),
    (23, 'largest_reading', 3, [
        ("largest_reading(['12', 'ERR', '9', '105'])", 105),
        ("largest_reading(['ERR'])", None),
        ("largest_reading([' 7 ', '40', '300'])", 300),
        ("largest_reading(['55'])", 55),
    ]),
    (24, 'find_row', 3, [
        ('find_row([2, 0, 5, 8], 4)', 2),
        ('find_row([1, 1], 3)', 'Sold out'),
        ('find_row([], 1)', 'Sold out'),
        ('find_row([9], 9)', 0),
    ]),
    (25, 'is_palindrome', 3, [
        ("is_palindrome('Never odd or even')", True),
        ("is_palindrome('Bad Robots')", False),
        ("is_palindrome('A man, a plan, a canal: Panama!')", True),
        ("is_palindrome('robot')", False),
    ]),
    (26, 'get_domain', 3, [
        ("get_domain('  Nat@Tolles.ORG ')", 'tolles.org'),
        ("get_domain('not-an-email')", ''),
        ("get_domain('@robots.com')", 'robots.com'),
        ("get_domain('a@b.co')", 'b.co'),
    ]),
    (27, 'closest_robot', 3, [
        ("closest_robot([('Atlas', 12.5), ('Bolt', 3.0), ('Cog', 7.2)])", 'Bolt'),
        ('closest_robot([])', None),
        ("closest_robot([('Zip', 1), ('Amp', 9)])", 'Zip'),
    ]),
    (28, 'find_owner', 3, [
        ("find_owner({101: ['laptop', 'hoodie'], 102: ['Calculator']}, 'calculator')", 102),
        ("find_owner({1: ['Wrench']}, 'wrench')", 1),
        ("find_owner({}, 'pen')", None),
        ("find_owner({5: ['pen'], 6: ['Laptop']}, 'LAPTOP')", 6),
    ]),
    (29, 'print_launch', 3, [
        ('printed(print_launch, 3)', '3 - 2 - 1 - GO!\n'),
        ('printed(print_launch, 1)', '1 - GO!\n'),
        ('printed(print_launch, 0)', 'GO!\n'),
    ]),
    (30, 'longest_streak', 3, [
        ("longest_streak(['W', 'W', 'L', 'W', 'W', 'W'])", 3),
        ("longest_streak(['L', 'L'])", 0),
        ("longest_streak(['W'])", 1),
        ("longest_streak(['W', 'W', 'W', 'L', 'W'])", 3),
        ('longest_streak([])', 0),
    ]),
    (31, 'apply_curve', 4, [
        ('apply_curve([70, 95, 88], 10)', [80, 100, 98]),
        ('apply_curve([], 5)', []),
        ('_apply_curve_original()', [70, 95, 88]),
    ]),
    (32, 'move_robot', 4, [
        ("move_robot((0, 0), 'NNE')", (1, 2)),
        ("move_robot((5, 5), 'W?SS')", (4, 3)),
        ("move_robot((2, -1), '')", (2, -1)),
        ("move_robot((0, 0), 'NESW')", (0, 0)),
    ]),
    (33, 'clean_tag', 4, [
        ("clean_tag('  #Bad Robots ')", 'bad-robots'),
        ("clean_tag('##FIRST Robotics Competition')", 'first-robotics-competition'),
        ("clean_tag('team1014')", 'team1014'),
    ]),
    (34, 'compound_interest', 4, [
        ('compound_interest(1000, 0.05, 2)', 1102.5),
        ('compound_interest(500, 0.1, 0)', 500.0),
        ('compound_interest(200, 0.0, 5)', 200.0),
        ('compound_interest(100, -0.1, 1)', None),
    ]),
    (35, 'log_visitor', 4, [
        ("_visitor_test(['Nat'])", ['Welcome, Nat! You are visitor #1']),
        ("_visitor_test(['Ann', 'Ben', 'Cal'])[-1]", 'Welcome, Cal! You are visitor #3'),
    ]),
    (36, 'permissions_text', 4, [
        ('permissions_text(6)', 'rw-'),
        ('permissions_text(0b101)', 'r-x'),
        ('permissions_text(7)', 'rwx'),
        ('permissions_text(0)', '---'),
        ('permissions_text(0o4)', 'r--'),
    ]),
    (37, 'safe_divide_all', 4, [
        ("safe_divide_all([(10, 4), (5, 0), (3, 'a')])", [2.5, 'div by zero', 'error']),
        ('safe_divide_all([(9, 3)])', [3.0]),
        ('safe_divide_all([(0, 0), (None, 2)])', ['div by zero', 'error']),
    ]),
    (38, 'top_three', 4, [
        ('top_three([72, 99, 85, 91, 60])', [99, 91, 85]),
        ('top_three([50, -1, 70])', [70, 50]),
        ('top_three([])', []),
    ]),
    (39, 'count_digit', 4, [
        ('count_digit(1014, 1)', 2),
        ('count_digit(7, 3)', 0),
        ('count_digit(7, 7)', 1),
        ('count_digit(5555, 5)', 4),
        ('count_digit(90210, 0)', 2),
    ]),
    (40, 'remove_out_of_stock', 4, [
        ("remove_out_of_stock({'bolt': 40, 'nut': 0, 'gear': 3})", {'bolt': 40, 'gear': 3}),
        ('remove_out_of_stock({})', {}),
        ("remove_out_of_stock({'a': 5})", {'a': 5}),
        ("remove_out_of_stock({'x': -1, 'y': 0})", {}),
    ]),
    (41, 'fibonacci_up_to', 5, [
        ('list(fibonacci_up_to(10))', [0, 1, 1, 2, 3, 5, 8]),
        ('list(fibonacci_up_to(0))', [0]),
        ('list(fibonacci_up_to(1))', [0, 1, 1]),
        ('list(fibonacci_up_to(50))', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ]),
    (42, 'add_to_queue', 5, [
        ("add_to_queue('Ben', ['Ann'])", ['Ann', 'Ben']),
        ("add_to_queue('Ann', ['Ann'])", ['Ann']),
        ("add_to_queue('Cal')", ['Cal']),
        ("add_to_queue('Dee')", ['Dee']),
    ]),
    (43, 'reserve_seats', 5, [
        ('reserve_seats(2, 3, [(0, 1)])', [['open', 'taken', 'open'], ['open', 'open', 'open']]),
        ('reserve_seats(1, 2, [])', [['open', 'open']]),
        ('reserve_seats(3, 1, [(2, 0)])', [['open'], ['open'], ['taken']]),
    ]),
    (44, 'check_payment', 5, [
        ('check_payment(0.30, [0.10, 0.20])', 'exact'),
        ('check_payment(5, [1.25, 1.25])', 'change 2.5'),
        ('check_payment(1.00, [0.70, 0.20, 0.10])', 'exact'),
        ('check_payment(2, [1.5, 1])', 'short 0.5'),
    ]),
    (45, 'bucket_temperatures', 5, [
        ('bucket_temperatures([-3, 4, 15, 18], 10)', {-10: 1, 0: 1, 10: 2}),
        ('bucket_temperatures([], 10)', {}),
        ('bucket_temperatures([-12, -20, 7], 5)', {-15: 1, -20: 1, 5: 1}),
        ('bucket_temperatures([25, 31, 39], 10)', {20: 1, 30: 2}),
    ]),
    (46, 'resolve_settings', 5, [
        ("resolve_settings({'volume': 0}, {'volume': 50, 'theme': 'dark'})", {'volume': 0, 'theme': 'dark'}),
        ("resolve_settings({'theme': 'light'}, {'volume': 50, 'theme': 'dark'})", {'volume': 50, 'theme': 'light'}),
        ("resolve_settings({'autosave': False, 'name': ''}, {'autosave': True, 'name': 'Player', 'fps': 60})", {'autosave': False, 'name': '', 'fps': 60}),
    ]),
    (47, 'round_scores', 5, [
        ('round_scores([89.5, 90.4, 72.5])', [90, 90, 73]),
        ('round_scores([None, 84.5])', ['ABS', 85]),
        ('round_scores([0.5, 99.49])', [1, 99]),
        ('round_scores([])', []),
    ]),
    (48, 'parse_ages', 5, [
        ("parse_ages(['15', 'abc', '17'])", ([15, 17], 1)),
        ("parse_ages(['x', '16'])", ([16], 1)),
        ('parse_ages([])', ([], 0)),
        ("parse_ages(['1.5', '18', ' 20 '])", ([18, 20], 1)),
    ]),
    (49, 'binary_string', 5, [
        ('binary_string(5)', '101'),
        ('binary_string(0)', '0'),
        ('binary_string(1)', '1'),
        ('binary_string(1014)', '1111110110'),
    ]),
    (50, 'reset_scores', 5, [
        ("reset_scores([['Ann', 12], ['Ben', 30]])", [['Ann', 0], ['Ben', 0]]),
        ('reset_scores([])', []),
        ('_reset_scores_original()', [['Ann', 12], ['Ben', 30]]),
    ]),
]


def _apply_curve_original():
    original = [70, 95, 88]
    apply_curve(original, 10)
    return original


def _visitor_test(names):
    global visitor_count
    visitor_count = 0
    messages = []
    for n in names:
        messages.append(log_visitor(n))
    return messages


def _reset_scores_original():
    board = [["Ann", 12], ["Ben", 30]]
    reset_scores(board)
    return board


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


def check_bug(cases):
    """Return None if every test passes, otherwise (test, expected, got)."""
    for expression, expected in cases:
        try:
            result = eval(expression)
            if result == expected:
                continue
            got = repr(result)
        except Exception as error:
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
    print("  DEBUG RELAY  -  " + TEAM_NAME)
    print("=" * 70)
    for number, name, value, cases in TESTS:
        possible += value
        failure = check_bug(cases)
        if failure is None:
            fixed += 1
            points += value
        if only and number not in only:
            continue
        label = "Bug " + str(number).rjust(2) + "  " + name.ljust(22)
        label += (str(value) + (" pt" if value == 1 else " pts")).ljust(7)
        if failure is None:
            print(label + "FIXED")
        elif only:
            print(label + "not fixed")
            print("         test:      " + failure[0])
            print("         expected:  " + failure[1])
            print("         got:       " + failure[2])
        else:
            print(label + "not fixed")
            print("         expected " + short(failure[1], 24) +
                  "   got " + short(failure[2], 30))
    print("-" * 70)
    print("  Bugs fixed: " + str(fixed) + " / " + str(len(TESTS)) +
          "        Points: " + str(points) + " / " + str(possible))
    print("-" * 70)
    if not only:
        print("  To see the full test for one bug, put its number after the")
        print("  file name, e.g.   python3 debug_relay.py 12")


if __name__ == "__main__":
    chosen = []
    for arg in sys.argv[1:]:
        if arg.isdigit():
            chosen.append(int(arg))
    run_tests(chosen)
