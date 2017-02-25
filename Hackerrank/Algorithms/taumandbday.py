from operator import itemgetter

def incCost(boxes,cost,ind):
    return boxes[ind]*cost[ind]


T = int(input())
for _ in range(T):

    total = 0

    boxes  = list(map(int,input().split())) #B,W
    cost = list(map(int,input().split())) #X,Y,Z

    sortedIndexes = sorted(range(len(cost)), key = lambda k: cost[k])

    test0 = sortedIndexes[0]
    test1 = sortedIndexes[1]
    test2 = sortedIndexes[2]
    worthChanging1 = (cost[test0]+cost[test1])<cost[test2]
    worthChanging2 = (cost[test1]+cost[test2])<cost[test0]
    if test0 !=2:
        total += incCost(boxes,cost,test0)
        if test1 !=2:
            total += incCost(boxes,cost,test1)
        else:
            if worthChanging1:
                total += boxes[test2]*(cost[test0]+cost[test1])
            else:
                total += incCost(boxes,cost,test2)
    else:
        #test 0 = 2
        total+= boxes[test1]*cost[test1]
        if worthChanging1:
            total+= boxes[test2]*(cost[test1] + cost[test0])
       # if worthChanging2:
        #    total +=
        else:
            total += boxes[test2] * cost[test2]
    print(total)

'''
    The smart way:
for _ in range(input()):
    e, o = map(int, raw_input().split())
    x, y, z = map(int, raw_input().split())
    print min(e * x + o * y, x * (e + o) + o * z, y * (e + o) + e * z)'''


    #minIndex = min(enumerate(costs[:len(costs)-1]), key=itemgetter(1))[0]
#    index = 0 if cost[1] < cost[0] else 1
    # to generate a box from another you have to pay the other box's price + the conversion
    # B = W + BW

    # c1<c2<c3 -> buy c1 then buy c2
    # c2<c1<c3 -> buy c2 then c1
    # c3<c1<c2 -> buy c1 and convert
    # c3<c2<c1 -> buy c2 and conevrt
    # c1<c3<c2 -> buy c1 then buy c1 if c1+c3 < c2 else buy c2
    # c2<c3<c1 -> buy c2 then buy c2 if c2+c3 < c1 else buy c1


   # print (minIndex)




