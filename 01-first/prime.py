from math import floor, sqrt

def is_prime(num):
    if num <= 3:
        return True
    for i in range(2, floor(sqrt(num)) ):
        if num%i == 0:
            return False
    return True

print( is_prime(43) )
