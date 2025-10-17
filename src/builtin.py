def print_(*args):
    print(*args, end="")
    return None


def println(*args):
    print(*args)
    return None


def size(obj):
    return f"{len(obj)}"


def add(a, b):
    try:
        a = float(a)
        b = float(b)

        if a.is_integer() and b.is_integer():
            a = int(a)
            b = int(b)
    except ValueError:
        raise ValueError("Both inputs must be numbers")

    return f"{a + b}"


def sub(a, b):
    try:
        a = float(a)
        b = float(b)

        if a.is_integer() and b.is_integer():
            a = int(a)
            b = int(b)
    except ValueError:
        raise ValueError("Both inputs must be numbers")

    return f"{a - b}"


def mul(a, b):
    try:
        a = float(a)
        b = float(b)

        if a.is_integer() and b.is_integer():
            a = int(a)
            b = int(b)
    except ValueError:
        raise ValueError("Both inputs must be numbers")

    return f"{a * b}"


def div(a, b):
    try:
        a = float(a)
        b = float(b)

        if a.is_integer() and b.is_integer():
            a = int(a)
            b = int(b)
    except ValueError:
        raise ValueError("Both inputs must be numbers")

    if b == 0:
        raise ValueError("Division by zero is not allowed")

    return f"{a / b}"


def mod(a, b):
    try:
        a = float(a)
        b = float(b)

        if a.is_integer() and b.is_integer():
            a = int(a)
            b = int(b)
    except ValueError:
        raise ValueError("Both inputs must be numbers")

    if b == 0:
        raise ValueError("Division by zero is not allowed")

    return f"{a % b}"


def pow(a, b):
    try:
        a = float(a)
        b = float(b)

        if a.is_integer() and b.is_integer():
            a = int(a)
            b = int(b)
    except ValueError:
        raise ValueError("Both inputs must be numbers")

    return f"{a ** b}"
