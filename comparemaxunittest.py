import unittest
def maxcompare(n):
         lis = map(int, n.split(','))
         threeans = []
         for i in range(3):
             maxnum = lis[0]
             for j in lis[1:]:
                 if int(j)>maxnum:
                     maxnum = j
             lis.remove(maxnum)
             threeans.append(maxnum)
         return threeans

class maxcomp(unittest.TestCase):
    def test1(self):
        self.assertEqual(maxcompare('2134,3421,6421,8723,9239,1234,2345'), [9239,8723,6421])

        self.assertEqual(maxcompare('23,45,43,67,98,143,5,3'), [143,98,67])

if __name__ == '__main__':
     unittest.main()
