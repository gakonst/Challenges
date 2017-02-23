input = raw_input().split()
n = int(input[0])
k = int(input[1].strip())
numbers = map(int, raw_input().split())
sort = sorted(numbers)
count = 0
i = 0
for i in range(0,len(numbers)):
    x = numbers[i]
    for j in range(i+1, len(numbers)):
        y = numbers[j]
        if (x + y) % k == 0:
            count += 1
print count
