prev, cur = 0,1
sum = 0
while True:
    prev, cur = cur, prev+cur
    if cur >= 4000000:
        break
    if cur % 2 == 0:
         sum += cur

print(sum)
