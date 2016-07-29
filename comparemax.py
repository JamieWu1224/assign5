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
