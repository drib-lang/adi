"""
Environment functions for the Drib REPL.
"""


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


def add(a, b):
    """Return the sum of two numbers as a string (int if both ints, else float)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        result = a_num + b_num
        if is_float:
            return str(float(result))
        return str(int(result))
    except Exception as e:
        return f"add error: {e}"


def sub(a, b):
    """Return the difference of two numbers as a string (int if both ints, else float)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        result = a_num - b_num
        if is_float:
            return str(float(result))
        return str(int(result))
    except Exception as e:
        return f"sub error: {e}"


def mul(a, b):
    """Return the product of two numbers as a string (int if both ints, else float)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        result = a_num * b_num
        if is_float:
            return str(float(result))
        return str(int(result))
    except Exception as e:
        return f"mul error: {e}"


def div(a, b):
    """Return the division of two numbers as a string (float if either is float, else int division)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        if is_float:
            result = a_num / b_num
            return str(float(result))
        else:
            result = a_num // b_num
            return str(int(result))
    except Exception as e:
        return f"div error: {e}"


def pow_(a, b):
    """Return a raised to the power of b as a string (int if both ints, else float)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        result = a_num**b_num
        if is_float:
            return str(float(result))
        return str(int(result))
    except Exception as e:
        return f"pow error: {e}"


def mod(a, b):
    """Return the modulus of two numbers as a string (int if both ints, else float)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        result = a_num % b_num
        if is_float:
            return str(float(result))
        return str(int(result))
    except Exception as e:
        return f"mod error: {e}"


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


def println(*args):
    """Print args* to the console."""
    print(*args)


def print_(*args):
    """Print args* to the console."""
    print(*args, end="")


# Environment dictionary
env = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "pow": pow_,
    "mod": mod,
    "gt": gt,
    "lt": lt,
    "geq": geq,
    "leq": leq,
    "eqs": eqs,
    "not": not_,
    "print": print_,
    "println": println,
    "E": "3.141592653589793",
    "PI": "2.718281828459045",
}
