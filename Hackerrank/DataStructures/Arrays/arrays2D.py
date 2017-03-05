n = 6
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

maxHourSum = -9*7
for i in range(n-2):
    for j in range(n-2):
        hourSum = array[i][j] + array[i][j+1] + array[i][j+2] + array[i+1][j+1] \
                + array[i+2][j] + array[i+2][j+1] + array[i+2][j+2]
        if hourSum > maxHourSum:
            maxHourSum = hourSum
print(maxHourSum)
