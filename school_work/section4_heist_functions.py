"""
Operation: Midnight Vault — A Functions Heist
PCEP Objective: PCEP-30-02 4.1 & 4.2
Difficulty: Intermediate

DESCRIPTION:
Your crew is breaking into the Obsidian Bank vault, and every stage of the
plan is a function. You'll recruit a crew, outsmart the alarm system, crack
the keypad, plant a decoy, review security footage, track guard patrols with
a generator, pack the loot, and pull it all together in one final run.

LEARNING OBJECTIVES:
- Define and invoke user-defined functions and generator functions (yield)
- Use return to send results back to the caller, and use None on purpose
- Tell parameters apart from arguments, and pass arguments by position,
  by keyword, and in a mix of both
- Give parameters default values, including the None default for a list
- Explain local vs. global scope, name hiding (shadowing), and use the
  global keyword to change a global variable from inside a function

EXPECTED OUTCOMES:
After completing this assignment, students will be able to:
- Break a larger program into small functions that call each other
- Predict what a function returns (including None) and what happens to
  global variables after a function runs
- Write a generator and consume it with a for loop or next()
- Call the same function correctly with positional, keyword, and mixed
  arguments

TOPIC MAP (where each exam topic shows up):
  Defining & invoking functions .... every stage
  Generators (yield) ............... Stages 6, 8
  return / returning results ....... Stages 1, 2, 3, 4, 6, 7, 8
  None keyword ..................... Stages 3, 5, 7, 8
  Parameters vs. arguments ......... Stage 1 (and every call you write)
  Positional / keyword / mixed ..... Stages 1, 7, 8
  Default parameter values ......... Stages 1, 2, 6, 7, 8
  Name scopes ...................... Stages 3, 4, 5
  Name hiding (shadowing) .......... Stages 4, 5
  global keyword ................... Stages 2, 5, 8

VOCAB CHECK:
  A PARAMETER is the name in the function definition:  def f(parameter):
  An ARGUMENT is the value you pass when calling it:   f(argument)

INSTRUCTIONS:
1. Read each function's docstring carefully. The docstring is the spec.
2. Replace each "pass" with your code. Do not change function names or
   parameter lists.
3. Work the stages in order. Later stages call earlier ones.
4. Run this file. The tests at the bottom print a check or an X for each
   stage, so you can see your progress.
5. Every stage must show a check before you submit.
6. Do NOT edit the global variables or the SECURITY FOOTAGE section.
"""

# ===========================================================================
# GLOBAL VARIABLES (heist intel). Do not change these lines.
# ===========================================================================
vault_code = "7319"     # The real vault code
alarm_level = 0         # Goes up every time the crew messes up
MAX_ALARM = 3           # At this level the building locks down


# ===========================================================================
# STAGE 1: Recruit the Crew
# ===========================================================================
def recruit_crew_member(name, role, skill=5):
    """
    Build a crew member's ID badge as a string.

    Demonstrates: defining a function, return, parameters vs. arguments,
    default parameter values, and positional / keyword / mixed calls.

    Parameters:
        name (str): The crew member's codename
        role (str): Their job on the crew (e.g., "Hacker", "Driver")
        skill (int): Skill rating from 1-10. Defaults to 5.

    Returns:
        str: A badge in the format "<name> the <role> [skill <skill>]"

    Example:
        >>> recruit_crew_member("Nova", "Hacker")              # positional
        'Nova the Hacker [skill 5]'
        >>> recruit_crew_member(role="Driver", name="Ace", skill=9)  # keyword
        'Ace the Driver [skill 9]'
        >>> recruit_crew_member("Ghost", "Lookout", skill=7)   # mixed
        'Ghost the Lookout [skill 7]'

    Think about it: In the last call, which are the PARAMETERS and which
    are the ARGUMENTS? Why would recruit_crew_member(skill=7, "Ghost",
    "Lookout") cause a SyntaxError?
    """
    return f"{name} the {role} [skill {skill}]"


# ===========================================================================
# STAGE 2: The Alarm System
# ===========================================================================
def trip_alarm(amount=1):
    """
    Raise the GLOBAL alarm_level by amount and return the new level.

    Demonstrates: the global keyword and default parameter values.

    Without the global keyword, the line alarm_level = alarm_level + amount
    inside this function would try to make a brand-new LOCAL variable and
    crash with an UnboundLocalError. You have to tell Python you mean the
    global one.

    Parameters:
        amount (int): How much to raise the alarm. Defaults to 1.

    Returns:
        int: The updated global alarm_level

    Example:
        >>> alarm_level = 0      # (at the start)
        >>> trip_alarm()
        1
        >>> trip_alarm(amount=2)
        3
        >>> alarm_level          # the global really changed
        3
    """
    global alarm_level
    alarm_level += amount
    return alarm_level


# ===========================================================================
# STAGE 3: Crack the Keypad
# ===========================================================================
def crack_keypad(guess):
    """
    Check a guess against the global vault_code.

    Demonstrates: reading a global variable (no global keyword needed just
    to READ it), invoking another function, and returning None to mean
    "it didn't work."

    - If guess matches vault_code, return the string "VAULT OPEN".
    - Otherwise, call trip_alarm() once (default amount) and return None.

    Parameters:
        guess (str): The code the crew types in

    Returns:
        str or None: "VAULT OPEN" if correct, otherwise None

    Example:
        >>> crack_keypad("7319")
        'VAULT OPEN'
        >>> print(crack_keypad("0000"))
        None
        >>> alarm_level          # the wrong guess tripped the alarm
        1

    Hint: Check for None with "is None", not "== None".
    """
    if guess == vault_code:
        return "VAULT OPEN"
    else:
        trip_alarm()
        return None


# ===========================================================================
# STAGE 4: Plant a Decoy
# ===========================================================================
def plant_decoy(digits):
    """
    Build a fake vault code to leave behind for the guards.

    Demonstrates: name hiding (shadowing).

    Inside this function you MUST create a LOCAL variable named vault_code,
    the same name as the global one. Set it to the digits reversed with
    "X" stuck on the end, then return it. Do NOT use the global keyword.

    Because the local vault_code hides (shadows) the global vault_code,
    the real code stays safe. After this function runs, the global
    vault_code must still be "7319".

    Parameters:
        digits (str): A string of digits, e.g. "1234"

    Returns:
        str: The decoy code (digits reversed + "X")

    Example:
        >>> plant_decoy("1234")
        '4321X'
        >>> vault_code           # global is untouched
        '7319'

    Hint: Slicing with [::-1] reverses a string.
    """
    vault_code = digits[::-1] + "X"
    return vault_code


# ===========================================================================
# SECURITY FOOTAGE (do not edit; used in Stage 5)
# ===========================================================================
camera_mode = "recording"
motion_count = 0


def guard_shift(minutes):
    camera_mode = "paused"
    global motion_count
    motion_count = motion_count + minutes
    return camera_mode + " for " + str(minutes)


def night_watch():
    report = guard_shift(5)
    report = guard_shift(minutes=10)
    return report


def log_noise():
    noise = "creak"


# ===========================================================================
# STAGE 5: Review the Security Footage
# ===========================================================================
def review_security_footage():
    """
    Trace the SECURITY FOOTAGE code above BY HAND and predict the results.

    Demonstrates: local vs. global scope, shadowing, the global keyword,
    and functions that return None.

    Assume camera_mode starts as "recording" and motion_count starts as 0.
    Then this code runs:

        final_report = night_watch()
        noise = log_noise()

    Predict these four values:
        1. final_report          (what night_watch() returns)
        2. camera_mode           (the GLOBAL value after it all runs)
        3. motion_count          (the GLOBAL value after it all runs)
        4. noise                 (what log_noise() returns)

    Returns:
        tuple: (final_report, camera_mode, motion_count, noise)

    Example (format only, NOT the answer):
        >>> review_security_footage()
        ('paused for 99', 'off', 42, 'bang')

    Rules: Trace it on paper first. Just type your predictions as a tuple.
    Do NOT call the footage functions here. The test will tell you if
    you're right, but it won't tell you the answer.
    """
    return ("paused for 10", "recording", 15, None)


# ===========================================================================
# STAGE 6: Track the Guard Patrol
# ===========================================================================
def guard_patrol(route, laps=1):
    """
    A GENERATOR that yields each checkpoint a guard visits, one at a time.

    Demonstrates: generator functions (yield) and default parameter values.

    The guard walks the whole route once per lap. For each checkpoint,
    yield a string in the format "Lap <lap>: <checkpoint>". Laps are
    numbered starting at 1.

    Parameters:
        route (list): Checkpoint names in order, e.g. ["Lobby", "Vault"]
        laps (int): How many times the guard walks the route. Defaults to 1.

    Yields:
        str: "Lap <lap>: <checkpoint>" for each stop

    Example:
        >>> patrol = guard_patrol(["Lobby", "Vault"], laps=2)
        >>> next(patrol)
        'Lap 1: Lobby'
        >>> next(patrol)
        'Lap 1: Vault'
        >>> list(patrol)                 # whatever is left
        ['Lap 2: Lobby', 'Lap 2: Vault']

    Note: Use yield, NOT return. Don't build a list. A generator hands
    back one value at a time, only when asked.
    """
    for lap in range(1, laps + 1):
        for checkpoint in route:
            yield f"Lap {lap}: {checkpoint}"


# ===========================================================================
# STAGE 7: Pack the Loot
# ===========================================================================
def pack_loot(item, value, bag=None):
    """
    Add an (item, value) tuple to a loot bag and return the bag.

    Demonstrates: None as a default value, and keyword / mixed arguments.

    - If no bag is passed in (bag is None), start a NEW empty list.
    - Append the tuple (item, value) to the bag.
    - Return the bag.

    Why not just write bag=[] as the default? A default value is created
    ONE time, when the def line runs, so every call would share the SAME
    list and loot would leak between heists. Using None and making a new
    list inside the function avoids that trap.

    Parameters:
        item (str): Name of the loot
        value (int): Its value in dollars
        bag (list or None): An existing bag to add to. Defaults to None.

    Returns:
        list: The bag, with the new (item, value) tuple at the end

    Example:
        >>> my_bag = pack_loot("Ruby", 500)
        >>> my_bag
        [('Ruby', 500)]
        >>> pack_loot("Crown", 2500, bag=my_bag)          # mixed
        [('Ruby', 500), ('Crown', 2500)]
        >>> pack_loot(value=50, item="Coin")               # keyword, new bag
        [('Coin', 50)]
    """
    if bag is None:
        bag = []

    bag.append((item, value))
    return bag


# ===========================================================================
# STAGE 8: Run the Heist (final integration)
# ===========================================================================
def run_heist(guess, route, loot, laps=1):
    """
    Run the whole heist using your earlier stages. Return the total value
    of the loot, or None if the crew gets caught.

    Demonstrates: decomposing a big job into function calls, consuming a
    generator, the global alarm_level, keyword arguments, and None.

    Do these steps in order:
      1. Wait out the guards: loop over guard_patrol(route, laps=laps) and
         count how many checkpoints the guard visits.
      2. If the count is MORE than 6, the crew waited too long. Call
         trip_alarm with amount=2 (as a keyword argument).
      3. If the global alarm_level is now at or above MAX_ALARM, the
         building locks down. Return None.
      4. Try the keypad with crack_keypad(guess). If it returns None,
         the crew is caught. Return None.
      5. Pack every (item, value) in loot with pack_loot. Start with
         bag = None and pass bag=bag each time so it all goes in ONE bag.
      6. Return the total dollar value of everything in the bag. If loot
         was empty, return 0.

    Parameters:
        guess (str): The keypad code to try
        route (list): The guard's patrol route
        loot (list): A list of (item, value) tuples to steal
        laps (int): Laps the guard walks. Defaults to 1.

    Returns:
        int or None: Total loot value, or None if the heist fails

    Example (each line starts with alarm_level = 0):
        >>> run_heist("7319", ["Lobby", "Vault"], [("Ruby", 500), ("Crown", 2500)])
        3000
        >>> print(run_heist("1111", ["Lobby"], [("Ruby", 500)]))
        None
        >>> run_heist("7319", ["Lobby", "Hall", "Vault", "Roof"], [("Ruby", 500)], laps=2)
        500
        >>> alarm_level      # 8 checkpoints > 6, so the alarm went up by 2
        2
    """
    count = 0


    for checkpoint in guard_patrol(route, laps=laps):
        count += 1


    if count > 6:
        trip_alarm(amount=2)
    if alarm_level >= MAX_ALARM:
        return None

    if crack_keypad(guess) is None:
        return None

    bag = None

    for item, value in loot:
        bag = pack_loot(item, value, bag=bag)
    total = 0

    if bag is not None:
        for item, value in bag:
            total += value

    return total


# ===========================================================================
# TESTS. Run this file to check your work. (You don't need to understand
# how this testing code works. Just read the output.)
# ===========================================================================
def _play_footage():
    global camera_mode, motion_count
    camera_mode = "recording"
    motion_count = 0
    final_report = night_watch()
    noise = log_noise()
    return (final_report, camera_mode, motion_count, noise)


def _test_stage_1():
    assert recruit_crew_member("Nova", "Hacker") == "Nova the Hacker [skill 5]", \
        "positional call with default skill"
    assert recruit_crew_member(role="Driver", name="Ace", skill=9) == "Ace the Driver [skill 9]", \
        "keyword call in a different order"
    assert recruit_crew_member("Ghost", "Lookout", skill=7) == "Ghost the Lookout [skill 7]", \
        "mixed call"
    assert recruit_crew_member("Rook", "Muscle", 2) == "Rook the Muscle [skill 2]", \
        "all positional"


def _test_stage_2():
    global alarm_level
    alarm_level = 0
    assert trip_alarm() == 1, "trip_alarm() should return 1 when starting from 0"
    assert trip_alarm(amount=2) == 3, "trip_alarm(amount=2) should return 3"
    assert alarm_level == 3, "the GLOBAL alarm_level should be 3 (did you use global?)"
    alarm_level = 0


def _test_stage_3():
    global alarm_level
    alarm_level = 0
    assert crack_keypad("7319") == "VAULT OPEN", "correct code should open the vault"
    assert alarm_level == 0, "a correct guess should NOT trip the alarm"
    assert crack_keypad("0000") is None, "a wrong guess should return None"
    assert alarm_level == 1, "a wrong guess should call trip_alarm() once"
    alarm_level = 0


def _test_stage_4():
    assert plant_decoy("1234") == "4321X", "plant_decoy('1234') should return '4321X'"
    assert plant_decoy("90") == "09X", "plant_decoy('90') should return '09X'"
    assert vault_code == "7319", "the GLOBAL vault_code changed! Don't use global here"
    assert "vault_code" in plant_decoy.__code__.co_varnames, \
        "create a LOCAL variable named vault_code inside plant_decoy"


def _test_stage_5():
    prediction = review_security_footage()
    actual = _play_footage()
    assert isinstance(prediction, tuple) and len(prediction) == 4, \
        "return a tuple of exactly 4 predictions"
    labels = ["final_report", "camera_mode", "motion_count", "noise"]
    for i in range(4):
        assert prediction[i] == actual[i], \
            "prediction #" + str(i + 1) + " (" + labels[i] + ") is wrong, so trace it again"


def _test_stage_6():
    patrol = guard_patrol(["Lobby", "Vault"], laps=2)
    assert patrol is not None, "guard_patrol returned None, so use yield"
    assert not isinstance(patrol, list), "guard_patrol should be a generator (use yield)"
    assert next(patrol) == "Lap 1: Lobby", "first checkpoint should be 'Lap 1: Lobby'"
    assert next(patrol) == "Lap 1: Vault", "second checkpoint should be 'Lap 1: Vault'"
    assert list(patrol) == ["Lap 2: Lobby", "Lap 2: Vault"], "lap 2 is wrong"
    assert list(guard_patrol(["Roof"])) == ["Lap 1: Roof"], "default laps should be 1"
    assert list(guard_patrol([], laps=3)) == [], "an empty route yields nothing"


def _test_stage_7():
    bag1 = pack_loot("Ruby", 500)
    assert bag1 == [("Ruby", 500)], "first call should make a new bag"
    bag2 = pack_loot("Watch", 200)
    assert bag2 == [("Watch", 200)], "loot leaked between bags! Use None as the default"
    assert pack_loot("Crown", 2500, bag=bag1) == [("Ruby", 500), ("Crown", 2500)], \
        "passing bag= should add to the existing bag"
    assert bag1 == [("Ruby", 500), ("Crown", 2500)], "the original bag should be updated"
    assert pack_loot(value=50, item="Coin") == [("Coin", 50)], "keyword call should work"


def _test_stage_8():
    global alarm_level
    alarm_level = 0
    assert run_heist("7319", ["Lobby", "Vault"], [("Ruby", 500), ("Crown", 2500)]) == 3000, \
        "a clean heist should return the total loot value"
    assert alarm_level == 0, "a clean heist should not raise the alarm"

    alarm_level = 0
    assert run_heist("1111", ["Lobby"], [("Ruby", 500)]) is None, \
        "a wrong code should return None"
    assert alarm_level == 1, "a wrong code should raise the alarm by 1"

    alarm_level = 0
    assert run_heist("7319", ["Lobby", "Hall", "Vault", "Roof"], [("Ruby", 500)], laps=2) == 500, \
        "8 checkpoints: alarm goes to 2, but the heist should still succeed"
    assert alarm_level == 2, "more than 6 checkpoints should raise the alarm by 2"

    alarm_level = 1
    assert run_heist("7319", ["A", "B", "C", "D"], [("Ruby", 500)], laps=2) is None, \
        "alarm 1 + 2 = 3 means lockdown, so return None"

    alarm_level = 0
    assert run_heist("7319", ["Lobby"], []) == 0, "no loot should return 0"
    alarm_level = 0


if __name__ == "__main__":
    print("=" * 50)
    print(" OPERATION: MIDNIGHT VAULT - Mission Check")
    print("=" * 50)

    stages = [
        ("Stage 1: Recruit the Crew", _test_stage_1),
        ("Stage 2: The Alarm System", _test_stage_2),
        ("Stage 3: Crack the Keypad", _test_stage_3),
        ("Stage 4: Plant a Decoy", _test_stage_4),
        ("Stage 5: Review the Footage", _test_stage_5),
        ("Stage 6: Track the Patrol", _test_stage_6),
        ("Stage 7: Pack the Loot", _test_stage_7),
        ("Stage 8: Run the Heist", _test_stage_8),
    ]

    passed = 0
    for title, test in stages:
        try:
            test()
            print("[✓] " + title)
            passed += 1
        except AssertionError as error:
            print("[X] " + title + " -> " + str(error))
        except Exception as error:
            print("[X] " + title + " -> crashed: " + type(error).__name__ + ": " + str(error))

    print("-" * 50)
    print(str(passed) + " / " + str(len(stages)) + " stages complete")
    if passed == len(stages):
        print("The vault is yours. Clean getaway!")
