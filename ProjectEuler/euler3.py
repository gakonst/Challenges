# https://stackoverflow.com/questions/23287/largest-prime-factor-of-a-number

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors


pfs = prime_factors(600851475143)
largest_prime_factor = max(pfs) # The largest element in the prime factor list
print (largest_prime_factor)

