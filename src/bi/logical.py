def parse_number(s):
    """Parse a string as int or float. Raises ValueError if not a number."""
    try:
        if "." in s or "e" in s or "E" in s:
            return float(s)
        return int(s)
    except ValueError:
        return float(s)  # fallback for cases like '2.0'


def parse_two_numbers(a, b):
    """Parse two strings as int or float. Returns (a_num, b_num, is_float)."""
    a_num = parse_number(a)
    b_num = parse_number(b)
    is_float = isinstance(a_num, float) or isinstance(b_num, float)
    return a_num, b_num, is_float


def gt(a, b):
    """Return True if a > b, else False. Handles int/float."""
    try:
        a_num, b_num, _ = parse_two_numbers(a, b)
        return a_num > b_num
    except Exception as e:
        return f"gt error: {e}"


def lt(a, b):
    """Return True if a < b, else False. Handles int/float."""
    try:
        a_num, b_num, _ = parse_two_numbers(a, b)
        return a_num < b_num
    except Exception as e:
        return f"lt error: {e}"


def geq(a, b):
    """Return True if a >= b, else False. Handles int/float."""
    try:
        a_num, b_num, _ = parse_two_numbers(a, b)
        return a_num >= b_num
    except Exception as e:
        return f"geq error: {e}"


def leq(a, b):
    """Return True if a <= b, else False. Handles int/float."""
    try:
        a_num, b_num, _ = parse_two_numbers(a, b)
        return a_num <= b_num
    except Exception as e:
        return f"leq error: {e}"


def eqs(a, b):
    """Return True if a == b, else False. Numeric if possible, else string."""
    try:
        a_num, b_num, _ = parse_two_numbers(a, b)
        return a_num == b_num
    except Exception:
        return a == b


def not_(x):
    """Return logical NOT of x."""
    return not x


def et(a, b):
    return a and b


def aut(a, b):
    return a or b
