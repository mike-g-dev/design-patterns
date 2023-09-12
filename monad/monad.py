class Maybe:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        self.value = func(self.value)
        return self

    def map(self, func):
        result = func(self.value)
        return Maybe(result)


def add_one(x):
    return x + 1


result = Maybe(1).bind(add_one).bind(
    add_one).bind(add_one).map(lambda x: x - 2)

print(result.value)
