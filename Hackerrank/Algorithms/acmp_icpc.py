n,m = map(int,input().split())
teams = []
for _ in range(n):
    teams.append(int(input(),2))

topics = [bin(teams[i] | teams[j]).count('1') for i in range(n-1) for j in range(i+1, n)]


'''
Follow pythonic solution ^
topics = []
for i in range(n-1):
    for j in range(i+1,n):
        ored = bin(teams[i] | teams[j])
        topics.append(ored.count('1')) #count 1 magic

'''

print (max(topics))
print (topics.count(max(topics)))



