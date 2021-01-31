class ProfileNotFoundError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return f"{self.message}: {self.expression}"

    def print(self):
        print(self)


if __name__ == "__main__":
    try:
        raise ProfileNotFoundError("test", "test")
    except ProfileNotFoundError as e:
        e.print()
    print("l")
