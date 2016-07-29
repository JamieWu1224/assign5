import unittest

class listcomperhension:
     def lis(self,num1, num2):
         listone = sum([i**2 for i in range(num1, num2+1) if i%2==0])
         listtwo = sum([i**2 for i in range(num1, num2+1) if i%2!=0])
         return listtwo-listone

class listcomperhensiontest(unittest.TestCase):

    def test1(self):
        a= listcomperhension()
        self.assertEqual(a.lis(1, 10), -55)
        self.assertEqual(a.lis(1, 50), -1275)
        self.assertEqual(a.lis(1, 123), 7626)

if __name__== '__main__':
    unittest.main()
