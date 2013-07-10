# Programmer: Sriram Pemmaraju
# Date: Feb 13, 2013

import random

# Given numbers a and n and a nonnegative integer d, this function 
# computes a^d mod n, i.e., the remainder one gets when a^d is divided by n.

# The function uses recursion to speedup computation. The function performs
# about log(d) multiplications, rather than d-1 multipications. So it should
# have no trouble handling d with 100s or even 1000s of digits. Also, in order
# to keep intermediate values small, performs the modulo operation as soon
# as possible, rather than wait for a^d to be computed.
def fastPowerMod(a, d, n):
    # Base cases of the recursion
    if(d == 0):
        return 1 % n
    elif(d == 1):
        return a % n
    # Recursive case
    else:
        temp = fastPowerMod(a, d/2, n)
        if(d%2 == 0): # if d is even  
            return (temp*temp) % n
        else: # d is odd
            return (((temp*temp)%n)*a)%n
