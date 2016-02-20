def e1(n):
    x = 0
    for y in range(1, n):
        if y % 3 == 0 or y % 5 == 0:
            x += y
    return x

def e2(n):
    w = 0
    x = 1
    y = 0
    z = 0
    while y < n:
        y = w + x
        if y % 2 == 0:
            z += y
        w = x
        x = y
    return z

def prime(num):
    limit = int(num ** 0.5) + 1
    odd = num
    for n in range(int(num / 2)):
        if odd % 2 == 0:
            odd /= 2
        else:
            break
    
    for n in range(limit):
        for div in range(3, limit, 2):
            
