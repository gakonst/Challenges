import sys

if __name__ == '__main__':
    n, k, q = list(map(int, sys.stdin.readline().split()))
    a = map(int, sys.stdin.readline().split())

    for i in range(q):
        x = int(raw_input().strip())
        print(a[(x - k) % n])