##1
def check_even():
    n = int(raw_input("Enter number: "))
    if (n % 2) == 0:
        print n, " is even."
    else:
        print n, "is odd."

##2
def triangle():
    s1 = int(raw_input("Enter side 1: "))
    s2 = int(raw_input("Enter side 2: "))
    s3 = int(raw_input("Enter side 3: "))
    p = s1 + s2 + s3
    
    if s1 + s2 > s3 or s1 + s3 > s2 or s2 + s3 > s1:
        print "Perimeter = ", p
    else:
        print "Invalid triangle!"

##3
def determine_grade():
    n = int(raw_input("Enter score: "))
    if n > 69 and n < 101:
        print "A"
    elif n > 59:
        print "B"
    elif n > 54:
        print "C"
    elif n > 49:
        print "D"
    elif n > 44:
        print "E"
    elif n > 34:
        print "S"
    elif n > -1:
        print "U"
    else:
        print "Invalid! Score must be within 0 - 100."
    

def find_gcd(a,b):
    n = 0
    if a < b:
        n = a
    else:
        n = b

    while n > 0:
        x = a / n
        y = b / n
        if a%n == 0 and b%n == 0:
            print n
            break
        n -= 1
