class vowels:
    def __init__(self, string):
        self.string = string
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index == len(self.string):
            raise StopIteration
        if self.string[self.current_index].lower() in 'aeiouy':
            return self.string[self.current_index]
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
