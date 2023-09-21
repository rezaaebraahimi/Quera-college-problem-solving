def solve(n, m):
    magic = [[0 for i in range(n)] for j in range(n)]
    i = 0
    j = n // 2
    
    for k in range(n ** 2):
        magic[i][j] = m
        m += 1
        if magic[(i - 1) % n][(j + 1) % n]:
            i += 1
        else:
            i = (i - 1) % n
            j = (j + 1) % n
    
    return magic

n, m = map(int, input().split())
for row in solve(n, m):
    for item in row:
        print(item, end=' ')
    print()
