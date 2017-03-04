import math

n = int(input())
for _ in range(n):
    grade = int(input())
    nextMult = math.ceil(grade/5)*5
    if grade >= 38:
        if  nextMult-grade < 3 :
            grade = nextMult
    print (grade)


