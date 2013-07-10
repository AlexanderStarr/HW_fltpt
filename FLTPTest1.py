#Alexander Starr
#22C:016:A01
#00567613

import random
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
def fltpTest(num_to_test):
    counter = 0
    while counter < 10:
        a = random.randint(1,num_to_test-1)
        #print a    # Used for debugging, to see the values being tested
        if fastPowerMod(a, num_to_test-1, num_to_test) != 1:
            return "composite"
        counter = counter + 1
    return "prime"

print fltpTest(int(raw_input("Enter a positive integer: ")))