def solve(n):
    lines = []
    sum_rows = [[0] for i in range(0, n)]
    sum_diag = 0
    sum_sec_diag = 0
    errors = []
    count = 0
    sum_collumns = [[0] for i in range(0, n)]
    for i in range(0, n):
        lines.append(map(int, raw_input().split()))
        sum_diag+=lines[i][i]
        sum_sec_diag+=lines[i][n-1-i]
        sum_rows[i]= sum(lines[i])
    if sum_sec_diag!=sum_diag:
        errors.append(0)
        count+=1
    for i in range(0,n):
        if sum_rows[i]!=sum_diag:
            errors.append(i+1)
            count+=1
        sum_collumns[i]=sum(row[i] for row in lines)
        if sum_collumns[i]!=sum_diag:
            errors.append(-1*(i+1))
            count+=1
    print count
    errors = sorted(errors)
    if errors:
        for e in errors:
            print e

if __name__ == '__main__':
    N = int(raw_input().strip())
    solve(N)
