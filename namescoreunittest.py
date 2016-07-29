import unittest

def namescore(name_string):
    lines = name_string.split(',')
    lines.sort()
    sums = [sum([ord(letter) - 64 for letter in line]) for line in lines]
    products = [x * (sums.index(x) + 1) for x in sums]
    total = sum(products)
    return total


class namescore(unittest.TestCase):


    def test1(self):
        self.assertEqual(namescore("ABC,CFE,DSA"), 106)


if __name__ == '__main__':
    unittest.main()
