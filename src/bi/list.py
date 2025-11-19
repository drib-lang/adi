def list_(*args):
    return list(args)


def get(arr, idx):
    return arr[int(idx)]


def set_(arr, idx, value):
    arr[int(idx)] = value


def size(arr):
    return str(len(arr))
