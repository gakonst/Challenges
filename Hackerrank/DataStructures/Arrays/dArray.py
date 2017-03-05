def getIndex(x,lastAns,N):
    return (x ^ lastAns) % N


N, Q = map(int,input().split())
queries = []
seqList = [[] for _ in range(N)]
lastAns = 0
# Get queries
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        seqList[getIndex(query[1],lastAns, N)].append(query[2])
    else:
        lastAns = seqList[getIndex(query[1],lastAns,  N)][query[2] % len(seqList[getIndex(query[1],lastAns,  N)])]
        print(lastAns)

