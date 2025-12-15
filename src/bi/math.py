from math import sqrt, isinf, isnan


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


def _format_result(result, is_float):
    """Format number results to JS-like strings for Infinity/NaN."""
    if isinstance(result, float):
        if isinf(result):
            return "Infinity" if result > 0 else "-Infinity"
        if isnan(result):
            return "NaN"
    if is_float:
        return str(float(result))
    return str(int(result))


def add(a, b):
    """Return the sum of two numbers as a string (int if both ints, else float)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        result = a_num + b_num
        return _format_result(result, is_float)
    except Exception as e:
        return f"add error: {e}"


def sub(a, b):
    """Return the difference of two numbers as a string (int if both ints, else float)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        result = a_num - b_num
        return _format_result(result, is_float)
    except Exception as e:
        return f"sub error: {e}"


def mul(a, b):
    """Return the product of two numbers as a string (int if both ints, else float)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        result = a_num * b_num
        return _format_result(result, is_float)
    except Exception as e:
        return f"mul error: {e}"


def div(a, b):
    """Return the division of two numbers as a string (float if either is float, else int division)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        if b_num == 0:
            try:
                a_val = float(a_num)
            except Exception:
                return "div error: invalid numerator"
            if isnan(a_val) or a_val == 0:
                return "NaN"
            return "Infinity" if a_val > 0 else "-Infinity"
        if is_float:
            result = a_num / b_num
            return _format_result(result, True)
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
        return _format_result(result, is_float)
    except Exception as e:
        return f"pow error: {e}"


def mod(a, b):
    """Return the modulus of two numbers as a string (int if both ints, else float)."""
    try:
        a_num, b_num, is_float = parse_two_numbers(a, b)
        result = a_num % b_num
        return _format_result(result, is_float)
    except Exception as e:
        return f"mod error: {e}"


def sqrt_(a):
    try:
        res = sqrt(float(a))
        return _format_result(res, True)
    except Exception:
        return "NaN"


def int_(a):
    try:
        val = float(a)
        if isinf(val):
            return "Infinity" if val > 0 else "-Infinity"
        if isnan(val):
            return "NaN"
        return str(int(val))
    except Exception as e:
        return f"int error: {e}"


def abs_(a):
    try:
        return str(abs(int(a)))
    except Exception:
        try:
            v = float(a)
            if isinf(v):
                return "Infinity" if v > 0 else "Infinity"
            if isnan(v):
                return "NaN"
            return str(abs(v))
        except Exception as e:
            return f"abs error: {e}"
