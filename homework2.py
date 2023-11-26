class Counter:
    def __init__(self, initial_value):
        self.value = initial_value

    def dec(self):
        self.value -= 1
        return self.value

    def inc(self):
        self.value += 1
        return self.value


class ReverseCounter(Counter):
    def dec(self):
        self.value += 1
        return self.value

    def inc(self):
        self.value -= 1
        return self.value


def get_counter(number):
    if number >= 0:
        return Counter(number)
    else:
        return ReverseCounter(number)
