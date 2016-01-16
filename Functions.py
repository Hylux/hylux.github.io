def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False

def is_int(n):
    if int(n) - n == 0:
        return True
    else:
        return False

def is_prime(n):
    if n > 1:
        x = n - 1
        while x > 1:
            if n % x == 0:
                return False
                break
            x -= 1
        else:
            return True
    else:
        return False

def digit_sum(n):
    x = str(n)
    y = 0
    for a in x:
        y += int(a)
    else:
        return y

def factorial(n):
    if n > 0:
        y = 1
        while n > 0:
            y *= n
            n -= 1
        else:
            return y
    else:
        print "Error"
