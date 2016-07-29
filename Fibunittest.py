import unittest

def F():
    f1, f2 = 0, 1
    while True:

        f1, f2 = f2, f1 + f2
        yield f2



class testfib(unittest.TestCase):
    def test1(self):
        b = F()
        self.assertEqual(b.next(), 1)
        self.assertEqual(b.next(), 2)
        self.assertEqual(b.next(), 3)
        self.assertEqual(b.next(), 5)
        self.assertEqual(b.next(), 8)


if __name__ == '__main__':
    unittest.main()
