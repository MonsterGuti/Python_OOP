class Stack:
    def __init__(self, *args):
        self.data = []
        for el in args:
            if isinstance(el, str):
                self.data.append(el)

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()
        return None

    def top(self):
        if self.data:
            return self.data[-1]
        return None

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        result = reversed(self.data)
        return f"[{', '.join(result)}]"
