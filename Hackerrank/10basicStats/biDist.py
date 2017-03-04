# Factorial
def fact(n):
    return 1 if n < 2 else n * fact(n-1)

# Combinations | neuton dionym
def comb(n,x):
    return fact(n) / (fact(x) * fact(n-x))

# Binomial Dist formula
def b(x,n,p):
    return comb(n,x) * p**x * (1-p)**(n-x)


x,y = map(float,input().split())
ratio = x/y
p = ratio / (1 + ratio)


prob = sum([b(i, 6, p)) for i in range(3,7)])

print (round(prob,3))
