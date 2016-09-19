def F():
    f1, f2 = 0, 1
    while True:
        f1, f2 = f1, f1 + f2
        yield b

c = F()







