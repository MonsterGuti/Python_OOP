class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest

class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.ilist = IntegerList(1, 2, "a", 3.5, 4)

    def test_constructor_only_accepts_integers(self):
        self.assertEqual(self.ilist.get_data(), [1, 2, 4])

    def test_add_valid_integer(self):
        result = self.ilist.add(10)
        self.assertEqual(result, [1, 2, 4, 10])

    def test_add_invalid_element_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.ilist.add("string")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_remove_index_valid(self):
        removed = self.ilist.remove_index(1)
        self.assertEqual(removed, 2)
        self.assertEqual(self.ilist.get_data(), [1, 4])

    def test_remove_index_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.ilist.remove_index(10)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_valid_index(self):
        self.assertEqual(self.ilist.get(0), 1)

    def test_get_index_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.ilist.get(5)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_valid(self):
        self.ilist.insert(1, 100)
        self.assertEqual(self.ilist.get_data(), [1, 100, 2, 4])

    def test_insert_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.ilist.insert(10, 5)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.ilist.insert(0, "a")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_get_biggest_returns_max_integer(self):
        self.ilist.add(999)
        self.assertEqual(self.ilist.get_biggest(), 999)

    def test_get_index_returns_correct_index(self):
        searched_index = self.ilist.get_index(4)
        self.assertEqual(searched_index, 2)


if __name__ == "__main__":
    unittest.main()



