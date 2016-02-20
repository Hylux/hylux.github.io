n = 1
a = 1
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        a *= n
        n += 1
print n
        
