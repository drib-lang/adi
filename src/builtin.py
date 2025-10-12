class Builtin:
    @staticmethod
    def println(*args):
        print(*args)

    @staticmethod
    def size(obj):
        return len(obj)
