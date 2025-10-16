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
