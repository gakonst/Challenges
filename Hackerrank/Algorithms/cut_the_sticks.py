

def result(sticks):
    sticks.sort(reverse=True)
    while len(sticks) > 0:
        print len(sticks)
        stop = sticks.pop()
        while len(sticks)>0 and sticks[-1]<=stop:
            sticks.pop()


if __name__ == '__main__':
    n = int(raw_input())
    sticks = map(int,raw_input().split())
    result(sticks)
