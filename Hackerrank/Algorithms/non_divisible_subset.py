def solve(k, S):
    # To have N1+N2%K == 0 <-> if N1%K == r then N2%K = k-r.
    # Calculate the set of numbers with remainder r/k-r and pick the larget set
    # http://cs.stackexchange.com/questions/57873/maximum-subset-pairwise-not-divisible-by-k
    r = k * [0]
    for x in S:
        r[x % k] += 1
    #Debug print r
    count = 0
    for i in range(1, (k + 1) // 2):
        count += max(r[i], r[k - i])
    if k % 2 == 0 and r[k // 2]:
        count += 1
    if r[0]:
        count += 1
    return count


if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    S = map(int, raw_input().split())
    print solve(k, S)
