"""
Tuples vs. Lists: Structure-Choice Lab
PCEP Objective: PCEP-30-02 3.2 (with 3.1)
Difficulty: Intermediate

DESCRIPTION:
Lists and tuples can hold the same data, but they are built for different
jobs. In Part A you choose a container for five real scenarios and defend
each choice in writing. In Part B you build structures that nest lists and
tuples inside each other, then index into them.

LEARNING OBJECTIVES:
- Choose between a list and a tuple based on mutability and intended use
- Justify a container choice in clear technical writing
- Build nested structures that mix lists and tuples
- Use multi-level indexing such as data[1][0] and data[0][1][2]
- Explain why a tuple that contains a list is not fully immutable

EXPECTED OUTCOMES:
After completing this assignment, students will be able to:
- Pick the right container for a situation and explain why
- Read and write nested index expressions from the outside in
- Predict which changes to a nested structure raise TypeError and which work

INSTRUCTIONS:
1. Part A: for each scenario, build the structure with the sample data and
   write your justification in the matching why_ string.
2. Part B: read each function's docstring and implement the function body.
3. Run this file. Part A prints your choices; Part B checks your functions.
4. Be ready to defend your Part A choices. Wrong choices get discussed in
   class, not just fixed, so your reasoning matters as much as your answer.
"""


# =====================================================================
# PART A: STRUCTURE CHOICE
# =====================================================================
#
# For each scenario:
#   1. Replace None with a list OR a tuple (or a mix) holding the sample data.
#   2. Write 2-4 sentences in the why_ string explaining your choice.
#
# A strong justification answers these questions:
#   - Will this data change after it's created? How?
#   - Does each position have a fixed meaning, or are the items all the same kind?
#   - Does a Python rule force the choice? (Hint: dictionary keys.)
#
# Use the vocabulary: mutable, immutable, slot, index.
# ---------------------------------------------------------------------


# SCENARIO 1: Lab seat map
# Mr. Sears is building a dictionary that maps each lab seat to the student
# sitting there. Each seat is identified by its row and seat number.
# Build the seat location for row 2, seat 5. This value will be used as a
# dictionary KEY.
scenario_1 = (2, 5)

why_1 = """
tuple cause sits likely wont move
"""


# SCENARIO 2: Help queue
# During lab, students add their name when they need help, and names are
# removed once they've been helped. Build the queue with three students
# waiting: "Jordan", "Priya", "Marcus".
scenario_2 = ["Jordan", "Priya", "Marcus"]

why_2 = """
list cause youll remove names
"""


# SCENARIO 3: Website theme color
# The course website stores its pine-green color as an RGB value:
# red 22, green 48, blue 42. Position 0 is always red, 1 is green, 2 is blue.
scenario_3 = (22, 48, 42)

why_3 = """
tuple cause you dont usualy change your webside colors
"""


# SCENARIO 4: Robotics match scores
# Team 1014 records its score after each qualification match on competition
# day. Build the structure with the first three scores: 87, 102, 95.
scenario_4 = [87, 102, 95]

why_4 = """
list cause scores are likely to change
"""


# SCENARIO 5: Gradebook entry
# Each gradebook entry holds a student's name, which never changes, and that
# student's quiz scores, which keep growing all year. Build the entry for
# "Ava", whose quiz scores so far are 92 and 85.
# (Think carefully: the best answer might not be just one container.)
scenario_5 = ("Ava", [92, 85])

why_5 = """
both cause you have names that dont change and scores which usually do
"""


# =====================================================================
# PART B: NESTED STRUCTURES
# =====================================================================


def get_stop_coordinate(route, stop, axis):
    """
    Return one coordinate from a route stored as a list of (x, y) tuples.

    This function demonstrates two-level indexing into tuples inside a list.
    The first index picks the stop (list slot); the second index picks
    x or y from that stop's tuple.

    Parameters:
        route (list): A list of (x, y) tuples, e.g. [(0, 0), (3, 4), (6, 8)]
        stop (int): Which stop to look at (0 is the first stop)
        axis (int): 0 for x, 1 for y

    Returns:
        int: The requested coordinate

    Example:
        >>> get_stop_coordinate([(0, 0), (3, 4), (6, 8)], 1, 0)
        3
        >>> get_stop_coordinate([(0, 0), (3, 4), (6, 8)], 2, 1)
        8
        >>> get_stop_coordinate([(0, 0), (3, 4), (6, 8)], -1, 0)
        6

    Hint: This can be done in one line with two sets of square brackets.
    """
    return route[stop][axis]


def move_stop(route, stop, new_x, new_y):
    """
    Move one stop on a route to a new location and return the route.

    The stops are tuples, so you cannot change a stop's x or y directly
    (route[stop][0] = new_x raises TypeError). The route itself is a list,
    so you CAN replace a whole stop with a brand-new tuple.

    Modify the original list in place and return it.

    Parameters:
        route (list): A list of (x, y) tuples
        stop (int): Index of the stop to move
        new_x (int): The stop's new x value
        new_y (int): The stop's new y value

    Returns:
        list: The same route list, with that stop replaced

    Example:
        >>> my_route = [(0, 0), (3, 4), (6, 8)]
        >>> move_stop(my_route, 1, 5, 5)
        [(0, 0), (5, 5), (6, 8)]
        >>> my_route
        [(0, 0), (5, 5), (6, 8)]

    Hint: Ask yourself which slot you are changing: a list slot or a tuple slot.
    """
    route[stop] = (new_x, new_y)
    return route


def make_team(name, member1, member2):
    """
    Build a team record: a tuple holding the team name and a list of members.

    The team name is fixed, so the outer container is a tuple. The roster
    can grow, so the members go in a list inside the tuple.

    Parameters:
        name (str): The team name
        member1 (str): The first team member
        member2 (str): The second team member

    Returns:
        tuple: (name, [member1, member2])

    Example:
        >>> make_team("Red", "Ava", "Ben")
        ('Red', ['Ava', 'Ben'])
        >>> make_team("Blue", "Cy", "Dee")
        ('Blue', ['Cy', 'Dee'])
    """
    return (name, [member1, member2])


def get_team_member(teams, team_index, member_index):
    """
    Return one member's name from a list of team records.

    This function demonstrates three-level indexing. Each team record is a
    tuple (name, [members]), and the records are stored in a list:

        teams = [("Red", ["Ava", "Ben"]), ("Blue", ["Cy", "Dee", "Eli"])]

    Work from the outside in: pick the team, then the roster, then the member.

    Parameters:
        teams (list): A list of (team_name, [member, ...]) tuples
        team_index (int): Which team to look at
        member_index (int): Which member of that team to return

    Returns:
        str: The member's name

    Example:
        >>> teams = [("Red", ["Ava", "Ben"]), ("Blue", ["Cy", "Dee", "Eli"])]
        >>> get_team_member(teams, 1, 2)
        'Eli'
        >>> get_team_member(teams, 0, 0)
        'Ava'
        >>> get_team_member(teams, -1, -1)
        'Eli'

    Hint: The roster is always in slot 1 of a team record.
    """
    return teams[team_index][1][member_index]


def add_quiz_score(entry, score):
    """
    Add a quiz score to a gradebook entry and return the SAME entry.

    The entry is a tuple: (student_name, [scores]). You cannot reassign
    either of the tuple's slots, but the list in slot 1 is still mutable.
    Add the score to that list without creating a new tuple.

    Parameters:
        entry (tuple): A (name, [scores]) gradebook entry
        score (int): The new quiz score

    Returns:
        tuple: The same entry object, now holding the new score

    Example:
        >>> ava = ("Ava", [92, 85])
        >>> add_quiz_score(ava, 78)
        ('Ava', [92, 85, 78])
        >>> ava
        ('Ava', [92, 85, 78])

    Hint: entry[1] = entry[1] + [score] raises TypeError. Why? What list
    method changes the list without touching the tuple's slot?
    """
    entry[1].append(score)
    return entry


# =====================================================================
# TESTS - run this file to check your work
# =====================================================================
if __name__ == "__main__":

    def describe(value):
        """Describe a structure's container type(s) in plain words."""
        if isinstance(value, tuple):
            inner = [type(v).__name__ for v in value if isinstance(v, (list, tuple))]
            return "tuple" + (" containing a " + " and a ".join(inner) if inner else "")
        if isinstance(value, list):
            inner = [type(v).__name__ for v in value if isinstance(v, (list, tuple))]
            return "list" + (" containing a " + " and a ".join(inner) if inner else "")
        return "nothing yet (still None)" if value is None else type(value).__name__

    print("=" * 60)
    print("PART A: Your structure choices")
    print("=" * 60)
    scenarios = [
        ("1 Lab seat map", scenario_1, why_1),
        ("2 Help queue", scenario_2, why_2),
        ("3 Theme color", scenario_3, why_3),
        ("4 Match scores", scenario_4, why_4),
        ("5 Gradebook entry", scenario_5, why_5),
    ]
    for label, value, why in scenarios:
        print(f"\nScenario {label}")
        print(f"  You built: {value!r}")
        print(f"  That is a: {describe(value)}")
        if "TODO" in why or len(why.split()) < 15:
            print("  Justification: not finished yet (aim for 2-4 sentences)")
        else:
            print("  Justification: written")
    print("\nPart A isn't auto-graded. Be ready to defend each choice in class.")

    print("\n" + "=" * 60)
    print("PART B: Nested structures")
    print("=" * 60)
    passed = 0
    total = 0

    def check(label, got, expected):
        global passed, total
        total += 1
        if got == expected:
            passed += 1
            print(f"  PASS  {label}")
        else:
            print(f"  FAIL  {label}: expected {expected!r}, got {got!r}")

    print("\nget_stop_coordinate")
    route = [(0, 0), (3, 4), (6, 8)]
    check("stop 1, x", get_stop_coordinate(route, 1, 0), 3)
    check("stop 2, y", get_stop_coordinate(route, 2, 1), 8)
    check("last stop, x", get_stop_coordinate(route, -1, 0), 6)

    print("\nmove_stop")
    route = [(0, 0), (3, 4), (6, 8)]
    result = move_stop(route, 1, 5, 5)
    check("returns the updated route", result, [(0, 0), (5, 5), (6, 8)])
    check("original list was changed", route, [(0, 0), (5, 5), (6, 8)])
    check("new stop is the tuple (5, 5)", route[1], (5, 5))

    print("\nmake_team")
    team = make_team("Red", "Ava", "Ben")
    check("builds the record", team, ("Red", ["Ava", "Ben"]))
    check("outer container is a tuple", isinstance(team, tuple), True)
    check("roster is a list", isinstance(team[1] if team else None, list), True)

    print("\nget_team_member")
    teams = [("Red", ["Ava", "Ben"]), ("Blue", ["Cy", "Dee", "Eli"])]
    check("team 1, member 2", get_team_member(teams, 1, 2), "Eli")
    check("team 0, member 0", get_team_member(teams, 0, 0), "Ava")
    check("last team, last member", get_team_member(teams, -1, -1), "Eli")

    print("\nadd_quiz_score")
    ava = ("Ava", [92, 85])
    result = add_quiz_score(ava, 78)
    check("returns the updated entry", result, ("Ava", [92, 85, 78]))
    check("returns the SAME tuple object", result is ava, True)
    check("original entry was changed", ava, ("Ava", [92, 85, 78]))

    print("\n" + "=" * 60)
    print(f"Part B: {passed} of {total} checks passed")
    if passed == total:
        print("All Part B checks passed!")
