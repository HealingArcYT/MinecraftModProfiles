import sys


class InputError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return f"{self.message}: {self.expression}"

    def print(self):
        print(self)

if __name__ == "__main__":
    try:
        raise InputError("test", "test")
    except InputError as e:
        e.print()
        print(sys.exc_info()[2])
    print("l")