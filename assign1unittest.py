import unittest

def perfectnum(n):
      sum = 0
      for i in range(1, n):
       if(n%i == 0):
        sum = sum + i
      return(sum == n)


class perfecttest(unittest.TestCase):

    def test1(self):
        self.assertEqual(perfectnum(7), False)
        self.assertEqual(perfectnum(28), True)
        self.assertEqual(perfectnum(0), True)


if __name__ == '__main__':
    unittest.main()
