#26 points. Still haven't figured out why
def solve(highway_length,cows):
    cow = [[0 for i in range(0,4)] for j in range(0,highway_length)]
    #cow[1][0]=1
    #cow[2][1]=1
    #USED ZEROES = [0,0,0,0]. The all have the same address. If i change the value of car[1][1], \
                    # it innately changes the value of zeroes through memory, but each column of the car list \
                    # is referred from zeroes so it gets the same value. MOST EPIC BUG EVER
    car = [[1, 0, 0,0]]
    for j in range(1, highway_length):
        car.append([0,0,0,0])
    for i in range(0,cows):
        # 0<coxy<ighway_length
        # 0<cowx<4
        cow_x,cow_y= map(int,raw_input().split())
        cow_y-=1
        if cow_x == 1:
            cow[cow_y][0] = 1
        elif cow_x == 2:
            cow[cow_y][1] = 1
        if cow_x == 3:
            cow[cow_y][2] = 1
        if cow_x == 4:
            cow[cow_y][3] = 1
            # If 4 cows appear in the same line in the road, car has 0 ways to pass
            # so we exit
            road_blocked = 0
            for j in range(0, 4):
                if cow[cow_y][j] == 1:
                    road_blocked += 1
            if road_blocked == 4:
                print "0"
                exit(0)
    for i in range(1,highway_length):
        for j in range(0,4):
            if cow[i][j] == 1:
                car[i][j] = 0
                #print "[*] DEBUG:"+str(i),str(j) +"cow found, deleting"
                #print car
            if cow[i][j]!=1:
                for k in range(j-1,j+2):
                    if k<0 or k>3:
                        continue
                    if car[i-1][k] !=0:
                       # print "[*}DEBUG: CAR before:",str(i),str(j),str(k)
                       # print car[i+1][j]
                        car[i][j]= car[i][j]+car[i-1][k]
                     #   print "[*}DEBUG: CAR after:",str(i),str(j),str(k)
                     #   print car[i+1][j]
          #  if i==highway_length-1:break
    print car
    return car[highway_length-1][0]


if __name__ == '__main__':
  highway_length, cows = map(int,raw_input().split())
  print solve(highway_length,cows)
