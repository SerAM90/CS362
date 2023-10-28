import math

def contrived_func(val):

    a = val - math.sqrt(abs(val*2)) > 5
    b = val ** 2 % 2 == 0
    c = val * 5 < 100
    d = -val ** 3 > 0

    if a or b:
        if (a and b) or (b and c) and d:
            print("condition passed 1")
        else:
            print("condition passed 2")
    else:
        if (a or b) or (b or c):
            print("condition passed 3")
        else:
            print("condition passed 4")
    
    if a and b:
        print("condition passed 5")
    else:
        print("condition passed 6")
 