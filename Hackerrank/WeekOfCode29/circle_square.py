import math

def dist(x1,y1,x2,y2):
    return (x2-x1)**2 + (y2-y1)**2

def insquare(p1,p3,x,y):
    '''Calculates the square made from points p1 p3. Then checks
    if x,y are inside that square
    https://www.quora.com/Given-two-diagonally-opposite-points-of-a-square-how-can-I-find-out-the-other-two-points-in-terms-of-the-coordinates-of-the-known-points
    '''

    p2 = ((p1[0]+p3[0]+p3[1]-p1[1])/2,(p1[1]+p3[1]+p1[0]-p3[0])/2)
    p4 = ((p1[0]+p3[0]+p1[1]-p3[1])/2,(p1[1]+p3[1]+p3[0]-p1[0])/2)
    # print ('Rectangle at {} {} {} {}'.format(p1,p2,p3,p4))

    # Calculate if the point is at the left side of the edge
    # Edge line: A*x+B*y + C =0
    # A = -(y2-y1) B=x2-x1 C=(-A*x1+B*y1)
    # D = A * xp + B * yp + C
    p = [p1,p2,p3,p4]
    for i in range(4): # 4 edges - square
        x1,y1 = p[i]
        x2,y2 = p[(i+1)%4]
        A = -(y2-y1)
        B = x2-x1
        C = -(A*x1 + B*y1)
        D = A*x + B*y + C
        if D<0:
            return False
    return True


w, h = list(map(int,input().split()))
yc,xc,r = list(map(int,input().split()))
x1,y1,x3,y3 = list(map(int,input().split()))
p1 = (x1,y1)
p3 = (x3,y3)
# print ('h x w : {} x {}'.format(h,w))
# print('[+] Checking for Circle: {} {} {}'.format(xc,yc,r))
for i in range(h):
    for j in range(w):
        if dist(xc,yc,i,j)<=r**2:
            print ('#', end='')
        elif insquare(p1,p3,j,i):
            print('#', end='')
        else:
            print ('.', end='')
    print()


