""" Author: Christina Elmore
    Purpose: Create a program that always returns 1089 after operating on a given five digit number
"""
def reverse3(x):        #reverses the last three digits of a number
    ones = x%10
    tens = x%100/10
    hundreds = x%1000/100
    reversed_x3 = hundreds*1 + tens*10 + ones*100
    return reversed_x3

def reverse5(x):        #reverses a five digit number
    ones = x%10
    tens = x%100/10
    hundreds = x%1000/100
    thousands = x%10000/1000
    millions = x%100000/10000
    reversed_x5 = millions + thousands*10 + hundreds*100 + tens*1000 + ones*10000
    return reversed_x5

x5 = int(raw_input("Enter a value ==> "))
print x5
rev_x5 = reverse5(x5)
rev_x3 = reverse3(rev_x5)
x3 = reverse3(rev_x3)
y3 = max(rev_x3, x3) - min(rev_x3, x3)
rev_y3 = reverse3(y3)
z = rev_y3 + y3

print ""
print "Here is the computation:"
print "%d reversed is %d" %(x5, rev_x5)
print "%d - %d = %d" %(max(rev_x3, x3),min(rev_x3, x3), y3)
print "%d + %d = %d" %(y3, rev_y3, z)
if z == 1089:
    print "You see, I told you."
else:
    print "Are you sure your input is valid?"