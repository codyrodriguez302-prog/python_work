# ============================================================
#  BUG SCAVENGER HUNT
#  Name: ______________________
# ============================================================
#
#  This file has 3 functions. Each function has exactly ONE bug.
#  The program runs without crashing, but some answers are wrong.
#
#  Your mission:
#    1. Run the file (F5) and look for FAIL lines in the terminal.
#    2. Read the function's description. It tells you what the
#       function is SUPPOSED to do. Use it as your clue.
#    3. Set a breakpoint inside the function, run with F5, and
#       step through (F10 / F11). Watch the Variables panel.
#    4. When you find the bug, fix it.
#    5. Fill in your bug report at the bottom of this file.
#
#  Rules:
#    - Each fix is small: one or two lines.
#    - Do NOT change anything below the "TESTS" line.
#    - You are done when every test says PASS.
# ============================================================


# ------------------------------------------------------------
#  Function 1: Movie Night
# ------------------------------------------------------------
def movie_ticket_price(age, is_matinee):
    """
    The theater charges:
      - Kids 12 and under: $8
      - Everyone else:     $12
    Matinee (daytime) shows take $3 off any ticket.
    """
    if age <= 12:
        price = 8
    else:
        price = 12

    if is_matinee:
        price = price - 3

    return price


# ------------------------------------------------------------
#  Function 2: Late Homework
# ------------------------------------------------------------
def late_work_score(score, days_late):
    """
    Your teacher's late work policy:
      - On time (0 days late): you keep your score.
      - 1 to 3 days late: you lose 10 points for each day late.
      - More than 3 days late: the score is 0.
      - A score can never go below 0.
    """
    if days_late == 0:
        return score
    elif days_late > 3:
        return 0
    else:
        penalty = days_late * 10
        new_score = score - penalty
        if new_score < 0:
            new_score = 0
        return new_score


# ------------------------------------------------------------
#  Function 3: Phone Battery
# ------------------------------------------------------------
def battery_status(percent, is_charging):
    """
    Your phone shows a battery message:
      - 80% or higher:  "Full"
      - 20% to 79%:     "OK"
      - Below 20%:      "Low"
    If the battery is Low and NOT charging, it adds a warning.
    If the phone is charging, "(charging)" goes on the end.
    """
    def build_message(percent, level, is_charging):
        message = "Battery " + str(percent) + "% - " + level
        if is_charging:
            message = message + " (charging)"
        return message

    if percent >= 80:
        level = "Full"
    elif percent >= 20:
        level = "OK"
    else:
        if is_charging:
            level = "Low"
        else:
            level = "Low - plug in soon!"

    return build_message(percent, level, is_charging)


# ============================================================
#  TESTS - do not change anything below this line
# ============================================================
def check(test_name, expected, actual):
    if expected == actual:
        print("PASS  " + test_name)
    else:
        print("FAIL  " + test_name)
        print("        expected: " + str(expected))
        print("        got:      " + str(actual))


print("--- Movie Night ---")
check("10-year-old, evening show", 8, movie_ticket_price(10, False))
check("12-year-old, evening show", 8, movie_ticket_price(12, False))
check("16-year-old, matinee", 9, movie_ticket_price(16, True))

print("--- Late Homework ---")
check("95, turned in on time", 95, late_work_score(95, 0))
check("90, 2 days late", 70, late_work_score(90, 2))
check("15, 2 days late", 0, late_work_score(15, 2))
check("100, 5 days late", 0, late_work_score(100, 5))

print("--- Phone Battery ---")
check("95%, not charging", "Battery 95% - Full", battery_status(95, False))
check("50%, charging", "Battery 50% - OK (charging)", battery_status(50, True))
check("10%, not charging", "Battery 10% - Low - plug in soon!", battery_status(10, False))
check("10%, charging", "Battery 10% - Low (charging)", battery_status(10, True))


# ============================================================
#  BUG REPORT - fill this in as you find each bug
# ============================================================
#
#  Bug 1 (Movie Night)
#    Line number:
#    What was wrong:
#    How the debugger helped you find it:
#
#  Bug 2 (Late Homework)
#    Line number:
#    What was wrong:
#    How the debugger helped you find it:
#
#  Bug 3 (Phone Battery)
#    Line number:
#    What was wrong:
#    How the debugger helped you find it:
#
