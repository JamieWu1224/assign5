def namescore(name_string):
    lines = name_string.split('\n')
    lines.sort()
    sums = [sum([ord(letter.lower()) - 96 for letter in line]) for line in lines]
    products = [x * (sums.index(x) + 1) for x in sums]
    total = sum(products)
    return total
    
    
    
    
    
   
