with open('test.txt', 'r') as file:
    lines = [x.replace('\n', '') for x in file.readlines()]
    print "lines: ", lines
    lines.sort()
    print "lines sorted: ", lines

    sums = [sum([ord(letter.lower()) - 96 for letter in line]) for line in lines]
    print "sums: ", sums

    products = [x * (sums.index(x) + 1) for x in sums]
    print "products: ", products

    total = sum(products)
    print "total: ", total
    
    
    
    
   test.txt
   CDEF
   ABC
   FIJK
