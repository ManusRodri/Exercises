def divisible (n:int,d:int):
    if n % (d*2) == 0:
        return 2
    elif n % d == 0:
        return 1
    else:
        return 0
print (divisible(4,2))