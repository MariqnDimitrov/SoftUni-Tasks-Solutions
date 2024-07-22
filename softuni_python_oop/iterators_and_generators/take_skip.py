class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.increment_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.increment_number < self.count:
            number = self.increment_number * self.step
            self.increment_number += 1
            return number
        else:
            raise StopIteration

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
