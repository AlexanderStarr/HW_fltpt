#Alexander Starr
#22C:016:A01
#00567613

import random
import math
# fastPowerMod was programmed by Sriram Pemmaraju
# It very quickly finds a**(d) mod n
# a will be a random integer in the range [1,num_to_test-1]
# d will be num_to_test-1
# n will be num_to_test
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

# This will run the FLTP Test 10 times on the num_to_test
# It differs from FLPTTest1.py, it returns False/True instead of composite/prime, respectively
def fltpTest(num_to_test):
    counter = 0
    while counter < 10:
        a = random.randint(1,(num_to_test-1))
        if fastPowerMod(a, (num_to_test-1), num_to_test) != 1:
            return False
        counter = counter + 1
    return True

def exactPrimalityTest(n):
    factor = 2
    upper_bound = math.sqrt(n)
    while (factor <= upper_bound):
        if (n % factor == 0):
            return False
        factor = factor + 1
    return True

# Below, the function findIncorrectPrimes is defined
# First it finds the result of the fltpTest on the current number n in the range
# The fltpTest does not report false composites
# If fltpTest says it is composite, then the exactPrimalityTest does not run
# Only if fltpTest returns True, indicating a prime, does exactPrimalityTest run
# This saves time for large ranges
# If fltpTest returns True, but then exactPrimalityTest returns False,
# then n is an incorrectly classified prime and is printed to the console
# n is then incremented to check the next number
def findIncorrectPrimes(n,upper_bound):
    print "In the range",n,"-",upper_bound,"fltpTest incorrectly classified:"
    while n <= upper_bound:
        fltp_primality = fltpTest(n)
        if fltp_primality:
            real_primality = exactPrimalityTest(n)
            if real_primality == False:
                print n
        n = n + 1

findIncorrectPrimes(500,100000)