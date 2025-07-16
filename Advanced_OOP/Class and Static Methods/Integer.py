from math import floor


class Integer:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(floor(float_value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value: str):
        total = prev = 0
        for char in reversed(value.upper()):
            current = cls.roman_map.get(char, 0)
            if current < prev:
                total -= current
            else:
                total += current
            prev = current
        return cls(total)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            try:
                return cls(int(value))
            except ValueError:
                return "wrong type"
        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
