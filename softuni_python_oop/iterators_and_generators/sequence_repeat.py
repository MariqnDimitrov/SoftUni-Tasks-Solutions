class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.increment_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.increment_number < self.number:
            index = self.increment_number % len(self.sequence)
            returning_string = self.sequence[index]
            self.increment_number += 1
            return returning_string
        else:
            raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')


