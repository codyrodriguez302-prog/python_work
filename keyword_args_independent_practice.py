"""
Independent Practice: Clear Call Sites
PCEP Objective: PCEP-30-02 4.2 (positional, keyword, and mixed argument passing)
Difficulty: Intermediate

DESCRIPTION:
Part 1: refactor four opaque positional calls into keyword calls.
Part 2: design ONE function of your own (its inputs and its output), then
write three call sites for it that anyone can read without opening your code.

LEARNING OBJECTIVES:
- Refactor positional calls to keyword form without changing the result
- Design a function's inputs (parameters, defaults) and output (return value)
- Write call sites that read clearly

EXPECTED OUTCOMES:
After completing this practice, students will be able to:
- Choose when an argument should be passed by name
- Pick parameter names that make sense at the call site, not just in the def line
- Document a function's inputs and output in a docstring

INSTRUCTIONS:
1. Do NOT edit the four provided functions in the "PROVIDED FUNCTIONS" section.
2. Complete Part 1 (refactor_1 through refactor_4).
3. Complete Part 2 (your function, MY_FUNCTION, call_site_1-3, READ_ALOUD).
4. Run the file. The checks at the bottom print PASS or NOT YET.

HOW THIS IS GRADED: CLARITY AT THE CALL SITE
The automatic checks only catch rule-breaking. Mr. Sears will read your
call sites and grade them on clarity:
  [ ] A reader who has never seen your def line can tell what every argument
      means just by reading the call.
  [ ] Every True/False value is passed by name.
  [ ] The only positional argument (if any) is the obvious "thing" the
      function acts on.
  [ ] Parameter names read naturally at the call site:
      urgent=True, not u=True or flag2=True.
  [ ] The function name plus its arguments reads like a sentence, and your
      READ_ALOUD sentences match what the calls actually do.
  [ ] Inputs and output are documented: the docstring has Parameters and
      Returns sections, and the function returns a value instead of printing.
"""


# =============================================================================
# PROVIDED FUNCTIONS (do not edit)
# =============================================================================

def set_password_policy(min_length, require_upper, require_digit,
                        require_symbol, expire_days):
    """Return a summary of a password policy."""
    return (f"min_length={min_length} upper={require_upper} digit={require_digit} "
            f"symbol={require_symbol} expire_days={expire_days}")


def create_vm(name, cpus, ram_gb, disk_gb, start_now, enable_backups):
    """Return a summary of a new virtual machine."""
    return (f"vm {name} | cpus={cpus} ram={ram_gb}GB disk={disk_gb}GB "
            f"start_now={start_now} backups={enable_backups}")


def log_event(message, level, include_timestamp, write_to_file, echo_to_screen):
    """Return a summary of how one log event was recorded."""
    return (f"[{level}] {message} | timestamp={include_timestamp} "
            f"file={write_to_file} screen={echo_to_screen}")


def send_notification(recipient, message, urgent=False, email=True, sms=False):
    """Return a summary of a notification. Note the default values!"""
    return (f"to={recipient} msg={message!r} urgent={urgent} "
            f"email={email} sms={sms}")


# =============================================================================
# PART 1: REFACTOR POSITIONAL CALLS TO KEYWORD FORM
#
# Rule: keep ONLY the first argument positional. Pass every other argument
# by name. The result must not change.
# =============================================================================

def refactor_1():
    """
    Refactor this password-policy call.

    Example of the shape you are aiming for:
        >>> power(2, exp=3)
        8
    """
    return set_password_policy(
        12,
        require_upper=True,
        require_digit=True,
        require_symbol=False,
        expire_days=90
    )


def refactor_2():
    """
    Refactor this virtual-machine call.

    Watch out: cpus, ram_gb, and disk_gb are all numbers. In the original
    call it is easy to mix them up. Naming them makes a swap impossible to miss.
    """
    # TODO: rewrite as a keyword call
    return create_vm("web01",cpus=4,ram_gb=16,disk_gb=100,start_now= True,enable_backups= False)


def refactor_3():
    """
    Refactor this logging call.

    Hint: level is not a Boolean, but it still gets a name under the rule.
    """
    # TODO: rewrite as a keyword call
    return log_event("Login failed for admin",level="WARNING",include_timestamp= True,write_to_file= True,echo_to_screen= False)


def refactor_4():
    """
    Refactor this notification call.

    send_notification has DEFAULT values for urgent, email, and sms.
    Name every argument after the first one.

    Bonus: leave out any argument whose value already matches its default.
    The shortest clear call earns the bonus message in the checks.
    """
    # TODO: rewrite as a keyword call
    return send_notification("helpdesk", message="Server room is above 85F",urgent=True,email= True,sms= False)


# =============================================================================
# PART 2: DESIGN A FUNCTION WHOSE CALL SITES READ CLEARLY
#
# Pick ONE scenario. You decide the function name, the parameter names,
# their order, the defaults, and what it returns.
#
#   Scenario A: Help desk ticket
#     Inputs: who reported it, what is wrong, how serious it is, whether it
#     affects more than one person, whether to email the reporter.
#     Output: a one-line ticket summary (str).
#
#   Scenario B: Backup job
#     Inputs: what to back up, how many copies to keep, whether to compress,
#     whether to encrypt, whether to verify after copying.
#     Output: a one-line job description (str).
#
#   Scenario C: Guest Wi-Fi pass
#     Inputs: guest name, how many hours it lasts, whether streaming is
#     allowed, whether the guest must accept the terms, whether to print a QR code.
#     Output: a dict describing the pass.
#
# Requirements:
#   - The name is a verb phrase (create_..., schedule_..., issue_...).
#   - At least 3 parameters, including at least 2 True/False settings.
#   - At least 1 parameter has a default value.
#   - The docstring has a "Parameters:" section and a "Returns:" section.
#   - The function RETURNS its result (str or dict). It does not print.
# =============================================================================

def wifi_pass(guest_name, hours=10, allow_streaming=False,
              must_accept_terms=True, print_qr=False):
    """
    Create a guest Wi-Fi pass.

    Parameters:
        guest_name: Name of the guest.
        hours: How many hours the pass lasts.
        allow_streaming: Whether streaming is allowed.
        must_accept_terms: Whether the guest must accept terms.
        print_qr: Whether to print a QR code.

    Returns:
        A dictionary describing the Wi-Fi pass.
    """
    return {
        "guest": guest_name,
        "hours": hours,
        "streaming": allow_streaming,
        "terms": must_accept_terms,
        "qr_code": print_qr
    }


MY_FUNCTION = wifi_pass


def call_site_1():
    return wifi_pass(
        "John",
        hours=5,
        allow_streaming=True,
        must_accept_terms=True,
        print_qr=False
    )


def call_site_2():
    return wifi_pass(
        "Sarah",
        hours=24,
        allow_streaming=False,
        must_accept_terms=True,
        print_qr=True
    )


def call_site_3():
    return wifi_pass(
        "Mike",
        hours=3
    )


READ_ALOUD = [
    "Create a Wi-Fi pass for John lasting 5 hours, allowing streaming, requiring terms, and not printing a QR code.",
    "Create a Wi-Fi pass for Sarah lasting 24 hours, blocking streaming, requiring terms, and printing a QR code.",
    "Create a Wi-Fi pass for Mike lasting 3 hours, using the default settings."
]

# =============================================================================
# CHECKS (do not edit below this line)
# =============================================================================

import ast
import inspect
import textwrap


def _calls_in(func, target_name):
    """Return every ast.Call to target_name inside func."""
    tree = ast.parse(textwrap.dedent(inspect.getsource(func)))
    return [n for n in ast.walk(tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id == target_name]


def _check_refactor(label, func, target, expected, kw_count, bonus_kw=None):
    try:
        result = func()
    except Exception as err:
        print(f"  NOT YET  {label}: your call raised {type(err).__name__}: {err}")
        return False
    if result != expected:
        print(f"  NOT YET  {label}: the result changed. A value went to the wrong parameter.")
        print(f"           expected: {expected}")
        print(f"           got:      {result}")
        return False
    calls = _calls_in(func, target)
    if not calls:
        print(f"  NOT YET  {label}: could not find a call to {target}().")
        return False
    call = calls[0]
    if len(call.args) > 1 or len(call.keywords) < kw_count:
        print(f"  NOT YET  {label}: keep only the first argument positional; name the rest.")
        return False
    note = ""
    if bonus_kw is not None and len(call.keywords) == bonus_kw:
        note = "  (BONUS: shortest clear call, defaults left out)"
    print(f"  PASS     {label}{note}")
    return True


def _check_design():
    ok = True
    if MY_FUNCTION is None or not callable(MY_FUNCTION):
        print("  NOT YET  Design: set MY_FUNCTION to your function's name (no parentheses).")
        return False
    name = MY_FUNCTION.__name__
    params = inspect.signature(MY_FUNCTION).parameters
    if len(params) < 3:
        print("  NOT YET  Design: your function needs at least 3 parameters.")
        ok = False
    if not any(p.default is not inspect.Parameter.empty for p in params.values()):
        print("  NOT YET  Design: give at least one parameter a default value.")
        ok = False
    doc = inspect.getdoc(MY_FUNCTION) or ""
    if "Parameters" not in doc or "Returns" not in doc:
        print("  NOT YET  Design: the docstring needs a Parameters: section and a Returns: section.")
        ok = False
    if ok:
        print(f"  PASS     Design: {name}{inspect.signature(MY_FUNCTION)}")
    return ok


def _check_call_sites():
    if MY_FUNCTION is None or not callable(MY_FUNCTION):
        print("  NOT YET  Call sites: finish the design first.")
        return False
    name = MY_FUNCTION.__name__
    total_params = len(inspect.signature(MY_FUNCTION).parameters)
    ok = True
    dumps = []
    omitted_default = False
    for i, site in enumerate((call_site_1, call_site_2, call_site_3), start=1):
        calls = _calls_in(site, name)
        if not calls:
            print(f"  NOT YET  call_site_{i}: it must call {name}().")
            ok = False
            continue
        call = calls[0]
        dumps.append(ast.dump(call))
        try:
            result = site()
        except Exception as err:
            print(f"  NOT YET  call_site_{i}: raised {type(err).__name__}: {err}")
            ok = False
            continue
        if result is None:
            print(f"  NOT YET  call_site_{i}: returned None. Return the function's result,"
                  " and make sure your function returns (not prints).")
            ok = False
            continue
        if any(isinstance(a, ast.Constant) and isinstance(a.value, bool) for a in call.args):
            print(f"  NOT YET  call_site_{i}: a True/False is passed by position. Name it.")
            ok = False
            continue
        if len(call.args) > 1:
            print(f"  NOT YET  call_site_{i}: use at most ONE positional argument.")
            ok = False
            continue
        if i == 3 and len(call.args) + len(call.keywords) < total_params:
            omitted_default = True
        print(f"  PASS     call_site_{i}: {ast.unparse(call)}")
    if ok and len(set(dumps)) < 3:
        print("  NOT YET  Call sites: all three calls must be different.")
        ok = False
    if ok and not omitted_default:
        print("  NOT YET  call_site_3: leave out at least one argument so its default is used.")
        ok = False
    if any(len(s.strip()) < 10 for s in READ_ALOUD):
        print("  NOT YET  READ_ALOUD: write one full sentence for each call site.")
        ok = False
    return ok


if __name__ == "__main__":
    print("PART 1: REFACTORS")
    results = [
        _check_refactor("refactor_1", refactor_1, "set_password_policy",
                        set_password_policy(12, True, True, False, 90), 4),
        _check_refactor("refactor_2", refactor_2, "create_vm",
                        create_vm("web01", 4, 16, 100, True, False), 5),
        _check_refactor("refactor_3", refactor_3, "log_event",
                        log_event("Login failed for admin", "WARNING", True, True, False), 4),
        _check_refactor("refactor_4", refactor_4, "send_notification",
                        send_notification("helpdesk", "Server room is above 85F",
                                          True, True, False), 2, bonus_kw=2),
    ]
    print()
    print("PART 2: YOUR FUNCTION")
    results.append(_check_design())
    results.append(_check_call_sites())
    print()
    if all(results):
        print("All checks PASS. Now re-read your call sites as if you'd never seen")
        print("your def line. That is how they will be graded.")
    else:
        print(f"{results.count(True)} of {len(results)} checks PASS. Keep going!")
