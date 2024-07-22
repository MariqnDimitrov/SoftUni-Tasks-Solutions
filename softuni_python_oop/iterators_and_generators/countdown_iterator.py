class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.increment_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.increment_number <= self.count:
            number = self.count - self.increment_number
            self.increment_number += 1
            return number
        else:
            raise StopIteration

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")



