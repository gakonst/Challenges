T = int(input())


for _ in range(T):
    N = int(input())
    prev, cur = 0,1
    sum = 0
    while True:
        prev, cur = cur, prev+cur
        if cur >= N:
            break
        if cur % 2 == 0:
             sum += cur

    print(sum)
