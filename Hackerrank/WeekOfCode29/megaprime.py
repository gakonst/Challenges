import math
import sys
from random import randrange

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.

#def probably_prime(n, k):
#    """Return True if n passes k rounds of the Miller-Rabin primality
#    test (and is probably prime). Return False if n is proved to be
#    composite.
#
#    """
#    if n < 2: return False
#    for p in small_primes:
#        if n < p * p: return True
#        if n % p == 0: return False
#    r, s = 0, n - 1
#    while s % 2 == 0:
#        r += 1
#        s //= 2
#    for _ in range(k):
#        a = randrange(2, n - 1)
#        x = pow(a, s, n)
#        if x == 1 or x == n - 1:
#            continue
#        for _ in range(r - 1):
#            x = pow(x, 2, n)
#            if x == n - 1:
#                break
#        else:
#            return False
#    return True

#Inneficient
def is_prime(n):
    if (n % 2 == 0 and n > 2) or n==1:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.
# List of all primes up to n
#def primes(n):
#   """ Input n>=6, Returns a list of primes, 2 <= p < n """
#   n, correction = n-n%6+6, 2-(n%6>1)
#   sieve = [True] * (n/3)
#   for i in xrange(1,int(n**0.5)/3+1):
#     if sieve[i]:
#       k=3*i+1|1
#       sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
#       sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
#   return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

# Find which index
#def startIndex(start, numbers):
#    index = 0
#    for number in numbers:
#        if number > start:
#            index = numbers.index(number)
#            break
#    return index
#
#def megaprimes(start, primes):
#    index = startIndex(start, primes)
#    megaprime_list = []
#    for number in primes[index:]:
#        megaprime = True
#        for digit in str(number):
#            if not megaprime:
#                break
#            if int(digit) not in [2,3,5,7]:
#                megaprime = False
#        if megaprime:
#            megaprime_list.append(number)
#    return megaprime_list

count = 0
start,stop = list(map(int,raw_input().split()))
for num in xrange(start,stop):
    megaprime = True
    test = num
    # Check every digit. If any digit is found that is not prime, go to next number
    while test:
        if not megaprime:
            break
        digit = test % 10
        if digit not in [2,3,5,7]:
            megaprime = False
        test  //=10
    # If all digits are prime, check if the number is prime
    if megaprime:
        megaprime = probably_prime(num,10) # changes value of megaprime to false if it wasnt prime

    if megaprime:
        count+=1
print(count)

#numbers = primes(stop)
#mega = megaprimes(start, numbers)
#print (len(mega))






#for number in range(start,stop):
#    megaprime = True
#
#    if is_prime(number):
#       # print("Checking {}'s digits...".format(number))
#        for digit in str(number):
#         #   print("\tChecking {}".format(digit))
#            if not is_prime(int(digit)):
#                megaprime = False
#    else:
#         megaprime = False
#
#    if megaprime:
#        count+=1
#        #megaprimes.append(number)
#
#print (count)
##print(megaprimes)
