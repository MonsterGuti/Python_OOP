class dictionary_iter():
     def __init__(self, dictionary: dict):
         self.dict_tuple = tuple(dictionary.items())
         self.i = 0

     def __iter__(self):
         return self

     def __next__(self):
        if self.i >= len(self.dict_tuple):
            raise StopIteration
        result = self.dict_tuple[self.i]
        self.i += 1
        return result


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
