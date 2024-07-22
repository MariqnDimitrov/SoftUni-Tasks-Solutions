class dictionary_iter:
    def __init__(self, dict_object: dict):
        self.dict_object = tuple(dict_object.items())
        self.increment_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.increment_number < len(self.dict_object):
            pair = self.dict_object[self.increment_number]
            self.increment_number += 1
            return pair

        else:
            raise StopIteration

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)






