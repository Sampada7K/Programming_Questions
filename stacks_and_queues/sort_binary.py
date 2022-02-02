def countBits(a):
    count = 0
    while (a):
        if (a & 1 ):
            count += 1
        a = a>>1
    return count

print(countBits(7))