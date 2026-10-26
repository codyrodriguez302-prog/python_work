"""
Pixel Quest: Choose Your Collection
PCEP Objectives: PCEP-30-02 3.1 (Lists), 3.2 (Tuples), 3.3 (Dictionaries)
Difficulty: Intermediate

DESCRIPTION:
You are writing the data code for a small adventure game called Pixel Quest.
Each function describes WHAT the returned data needs to do, but not WHAT TYPE
it should be. Your job is to decide whether a list, a tuple, a dictionary, or
a combination of them is the right tool, and then write the code.

LEARNING OBJECTIVES:
- Choose between lists, tuples, and dictionaries based on how data will be used
- Build, index, slice, and iterate through lists, tuples, and dictionaries
- Combine collections (tuples inside lists, lists inside dictionaries, etc.)
- Avoid accidentally changing data you were only supposed to read

EXPECTED OUTCOMES:
After completing this assignment, you will be able to:
- Explain why a collection type is a good (or bad) fit for a job
- Use list methods, tuple packing/unpacking, and dictionary methods confidently
- Read a set of requirements and turn them into working code

HOW TO DECIDE - ask these questions about the data you are returning:
- Will I look things up by NAME (a key) or by POSITION (an index)?
- Does the data need to CHANGE later (grow, shrink, be edited)?
- Must the data be LOCKED so nobody can change it by accident?
- Will this value be used as a DICTIONARY KEY? (Keys must be immutable.)

INSTRUCTIONS:

1. Read each function's docstring, especially the REQUIREMENTS section.
2. On the "MY CHOICE" line, write which structure you picked and why.
3. Replace "pass" with your code.
4. Run this file. The tests at the bottom tell you which requirements
   your code meets. A FAIL message tells you which requirement to revisit.
5. Keep going until every test shows PASS.
"""


# =============================================================================
# FUNCTION 1: Count the loot
# =============================================================================
def count_loot(pickups):
    """
    Count how many of each item the player picked up during a level.

    Parameters:
        pickups (list): Item names in the order they were picked up.
                        The same item can appear more than once.

    Returns:
        A collection that holds a count for each item name.

    REQUIREMENTS for what you return:
        - The game must be able to look up an item's count by the item's
          NAME, like this:  loot["potion"]
        - Items the player never picked up must NOT be in the collection,
          so  "shield" in loot  is False.

    Example:
        >>> loot = count_loot(["potion", "sword", "potion", "gem", "potion"])
        >>> loot["potion"]
        3
        >>> loot["gem"]
        1
        >>> "shield" in loot
        False

    Hint: Loop through pickups. Before you add 1 to an item's count, check
          whether the item is already there.
    """
    # MY CHOICE: ____________ because ____________________________________
    print(pickups)
    object ={}
    for item in pickups:
        if item in object:
            object[item]+=1
        else:
            object[item]=1
    return object
# =============================================================================
# FUNCTION 2: Post the leaderboard
# =============================================================================
def leaderboard(scores, n):
    """
    Build a leaderboard of the n highest scores, highest first.

    Parameters:
        scores (list): Integer scores in no particular order.
        n (int): How many top scores to include. If n is larger than the
                 number of scores, include all of them.

    Returns:
        A collection of the top n scores, highest to lowest.

    REQUIREMENTS for what you return:
        - Spots are found by POSITION: board[0] is 1st place, board[1] is
          2nd place, and so on.
        - Once posted, the leaderboard is FINAL. Any attempt to change a
          spot (for example  board[0] = 0 ) must cause an error.
        - The original scores list must NOT be changed by your function.

    Example:
        >>> board = leaderboard([70, 98, 85, 90, 95], 3)
        >>> board[0]
        98
        >>> board[2]
        90
        >>> len(board)
        3

    Hint: One built-in function sorts without touching the original.
          Slicing can grab just the first n items.
    """
    # MY CHOICE: ____________ because ____________________________________
    if n> len(scores):
        return tuple(sorted(scores, reverse=True ))
    else:
        pl=sorted(scores, reverse=True )
        return tuple(pl[:n])
        
    


# =============================================================================
# FUNCTION 3: Trace the player's path
# =============================================================================
def trace_path(moves):
    """
    Record every position the player stands on while following a list of
    moves on a grid. The player always starts at x = 0, y = 0.

        "N" adds 1 to y      "S" subtracts 1 from y
        "E" adds 1 to x      "W" subtracts 1 from x

    Parameters:
        moves (list): Strings, each one "N", "S", "E", or "W".

    Returns:
        A collection of positions in the order they were visited, starting
        with the start position. Each position holds an x and a y.

    REQUIREMENTS for what you return:
        - Positions are in visit order: path[0] is the start and path[-1]
          is where the player ended up.
        - Other parts of the game will ADD more positions to the end of the
          path later, so the overall path must be able to grow.
        - Each single position will be used as a DICTIONARY KEY later, and
          a position must never be changed once it is recorded.

    Example:
        >>> path = trace_path(["N", "E", "E"])
        >>> len(path)
        4
        >>> path[0][0], path[0][1]       # x and y of the start
        (0, 0)
        >>> path[-1][0], path[-1][1]     # x and y of the final position
        (2, 1)

    Hint: Keep x and y in two plain variables while you loop. Each time the
          player moves, pack the current x and y together and record them.
    """
    # MY CHOICE: ____________ because ____________________________________
    x=0
    y=0
    path=[(x,y)]
    for move in moves:
        if move=="N":
            y+=1
        elif move=="E":
            x+=1
        elif move=="S":
            y-=1
        else:
            x-=1
        path.append((x,y))
    return path

# =============================================================================
# FUNCTION 4: Find the treasure
# =============================================================================
def find_treasure(grid):
    """
    Scan a map and report where every treasure is located.

    The map is a list of rows. Each row is a list of one-character strings:
        "T" = treasure     "." = open floor     "#" = wall

    Parameters:
        grid (list): A list of lists of strings (a matrix).

    Returns:
        A collection of (row, column) locations, one for each "T", ordered
        top row to bottom row, and left to right within a row.

    REQUIREMENTS for what you return:
        - The treasure map is PERMANENT. The overall collection must not be
          changeable, and no single location may be changed either.
        - Each location must be usable as a DICTIONARY KEY.
        - A map with no treasure returns an empty collection.

    Example:
        >>> world = [[".", "T", "#"],
        ...          ["#", ".", "."],
        ...          ["T", ".", "T"]]
        >>> spots = find_treasure(world)
        >>> spots[0][0], spots[0][1]     # row and column of the first treasure
        (0, 1)
        >>> len(spots)
        3

    Hint: Use nested loops with range(len(...)) so you know the row and
          column numbers. It is fine to collect results in one structure
          while you work and convert them to another before you return.
    """
    # MY CHOICE: ____________ because ____________________________________
    spots=[]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]=="T":
                spots.append(tuple((row,col)))
    return tuple(spots)

# =============================================================================
# FUNCTION 5: Merge two loot bags
# =============================================================================
def merge_loot(bag_a, bag_b):
    """
    Two players combine their loot. Build the combined loot WITHOUT changing
    either player's original bag.

    Parameters:
        bag_a (dict): Item name -> count (the same format count_loot returns).
        bag_b (dict): Item name -> count.

    Returns:
        A collection holding the combined count for every item that appears
        in either bag.

    REQUIREMENTS for what you return:
        - Look up combined counts by item NAME:  combined["gem"]
        - If an item is in both bags, the counts are added together.
        - bag_a and bag_b must be exactly the same after your function runs.
          (Watch out: writing  combined = bag_a  does NOT make a copy!)

    Example:
        >>> a = {"gem": 2, "potion": 1}
        >>> b = {"gem": 3, "key": 1}
        >>> combined = merge_loot(a, b)
        >>> combined["gem"]
        5
        >>> combined["key"]
        1
        >>> a
        {'gem': 2, 'potion': 1}

    Hint: Start with a real copy of one bag, then loop through the other
          bag's items(). The get() method can help with missing keys.
    """
    # MY CHOICE: ____________ because ____________________________________
    pass  # TODO: Implement this function


# =============================================================================
# FUNCTION 6: Group the party by role
# =============================================================================
def group_party(party, min_level):
    """
    Organize the players in a party by their role (Mage, Knight, etc.),
    keeping only players at or above a minimum level.

    Parameters:
        party (list): A list of tuples. Each tuple is (name, role, level),
                      for example ("Rin", "Mage", 7).
        min_level (int): Players BELOW this level are left out.

    Returns:
        A collection that groups player names by role.

    REQUIREMENTS for what you return:
        - Look up a role by NAME to get that role's group:  groups["Mage"]
        - Each group lists player names in alphabetical order.
        - New recruits will be ADDED to a group later, so each group must
          be able to grow.
        - A role with no qualifying players must NOT appear at all.

    Example:
        >>> party = [("Rin", "Mage", 7), ("Ash", "Knight", 3),
        ...          ("Bo", "Mage", 9), ("Cy", "Knight", 5)]
        >>> groups = group_party(party, 4)
        >>> groups["Mage"][0]
        'Bo'
        >>> groups["Mage"][1]
        'Rin'
        >>> len(groups["Knight"])
        1

    Hint: Unpack each tuple in the for loop header:
              for name, role, level in party:
          Sort each group after everything has been added.
    """
    # MY CHOICE: ____________ because ____________________________________
    pass  # TODO: Implement this function


# =============================================================================
# TESTS - Run this file to check your work. Do not edit below this line.
# =============================================================================
if __name__ == "__main__":

    results = {"passed": 0, "failed": 0}

    def check(requirement, test):
        """Run one test. A crash counts as a FAIL instead of stopping the file."""
        try:
            ok = test()
        except Exception as error:
            ok = False
            requirement += "   (crashed: " + type(error).__name__ + ")"
        if ok:
            results["passed"] += 1
            print("  PASS -", requirement)
        else:
            results["failed"] += 1
            print("  FAIL -", requirement)

    def started(name, result, number_of_tests):
        """Skip a function's tests (and count them as FAIL) if it returned None."""
        if result is None:
            results["failed"] += number_of_tests
            print("  NOT DONE -", name, "returned None. Did you write the code and a return statement?")
            return False
        return True

    def blocks_changes(collection, spot):
        """True if  collection[spot] = ...  raises a TypeError."""
        try:
            collection[spot] = "changed"
        except TypeError:
            return True
        return False

    def can_grow(collection, new_item):
        """True if the collection has an append() method that works."""
        before = len(collection)
        collection.append(new_item)
        return len(collection) == before + 1

    # ---------------------------------------------------------------- 1
    print("\nFunction 1: count_loot")
    loot = count_loot(["potion", "sword", "potion", "gem", "potion"])
    if started("count_loot", loot, 5):
        check("look up counts by name: loot['potion'] is 3", lambda: loot["potion"] == 3)
        check("look up counts by name: loot['sword'] is 1", lambda: loot["sword"] == 1)
        check("exactly 3 different items are stored", lambda: len(loot) == 3)
        check("items never picked up are not stored", lambda: "shield" not in loot)
        check("an empty pickup list gives an empty collection", lambda: len(count_loot([])) == 0)

    # ---------------------------------------------------------------- 2
    print("\nFunction 2: leaderboard")
    original = [70, 98, 85, 90, 95]
    board = leaderboard(original, 3)
    if started("leaderboard", board, 5):
        check("top 3 are 98, 95, 90 in that order", lambda: list(board) == [98, 95, 90])
        check("board[0] is 1st place", lambda: board[0] == 98)
        check("changing a spot causes an error", lambda: blocks_changes(board, 0))
        check("original scores list is unchanged", lambda: original == [70, 98, 85, 90, 95])
        check("n larger than the list returns every score",
              lambda: list(leaderboard([5, 1, 3], 10)) == [5, 3, 1])

    # ---------------------------------------------------------------- 3
    print("\nFunction 3: trace_path")
    path = trace_path(["N", "E", "E", "S", "W"])
    if started("trace_path", path, 6):
        expected_path = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0)]
        check("one position for the start plus one per move", lambda: len(path) == 6)
        check("positions are correct and in visit order",
              lambda: [tuple(p) for p in path] == expected_path)
        check("each position can be used as a dictionary key",
              lambda: len({pos: True for pos in path}) == 6)
        check("a recorded position cannot be changed", lambda: blocks_changes(path[1], 0))
        check("the path can grow", lambda: can_grow(trace_path(["N"]), (0, 2)))
        check("no moves gives just the start position",
              lambda: [tuple(p) for p in trace_path([])] == [(0, 0)])

    # ---------------------------------------------------------------- 4
    print("\nFunction 4: find_treasure")
    world = [[".", "T", "#", "T"],
             ["#", ".", ".", "."],
             ["T", ".", "#", "T"]]
    spots = find_treasure(world)
    if started("find_treasure", spots, 6):
        check("finds all 4 treasures", lambda: len(spots) == 4)
        check("locations are correct and in row-by-row order",
              lambda: [tuple(s) for s in spots] == [(0, 1), (0, 3), (2, 0), (2, 3)])
        check("the overall collection cannot be changed", lambda: blocks_changes(spots, 0))
        check("a single location cannot be changed", lambda: blocks_changes(spots[0], 0))
        check("each location can be used as a dictionary key",
              lambda: len({spot: "gold" for spot in spots}) == 4)
        check("a map with no treasure gives an empty collection",
              lambda: len(find_treasure([[".", "#"], ["#", "."]])) == 0)

    # ---------------------------------------------------------------- 5
    print("\nFunction 5: merge_loot")
    bag_a = {"gem": 2, "potion": 1}
    bag_b = {"gem": 3, "key": 1}
    combined = merge_loot(bag_a, bag_b)
    if started("merge_loot", combined, 6):
        check("items in both bags are added: combined['gem'] is 5", lambda: combined["gem"] == 5)
        check("items in only one bag are kept",
              lambda: combined["potion"] == 1 and combined["key"] == 1)
        check("combined holds exactly 3 different items", lambda: len(combined) == 3)
        check("bag_a is unchanged", lambda: bag_a == {"gem": 2, "potion": 1})
        check("bag_b is unchanged", lambda: bag_b == {"gem": 3, "key": 1})
        check("combined is a new object, not bag_a or bag_b",
              lambda: combined is not bag_a and combined is not bag_b)

    # ---------------------------------------------------------------- 6
    print("\nFunction 6: group_party")
    party = [("Rin", "Mage", 7), ("Ash", "Knight", 3), ("Bo", "Mage", 9),
             ("Cy", "Knight", 5), ("Dee", "Healer", 2), ("Al", "Mage", 4)]
    groups = group_party(party, 4)
    if started("group_party", groups, 5):
        check("look up a role by name: groups['Mage']",
              lambda: list(groups["Mage"]) == ["Al", "Bo", "Rin"])
        check("players below min_level are left out",
              lambda: list(groups["Knight"]) == ["Cy"])
        check("a role with no qualifying players does not appear",
              lambda: "Healer" not in groups)
        check("exactly 2 roles are stored", lambda: len(groups) == 2)
        check("each group can grow", lambda: can_grow(groups["Knight"], "Zed"))

    # ---------------------------------------------------------------- summary
    total = results["passed"] + results["failed"]
    print("\n" + "=" * 60)
    print("Passed", results["passed"], "of", total, "tests")
    if results["failed"] == 0:
        print("Every requirement met. You're ready for the quiz!")
    else:
        print("Read the FAIL lines above, then reread that function's REQUIREMENTS.")
    print("=" * 60)
