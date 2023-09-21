def one(x):
    return x - (x // 1)

def two(x):
    return x ** 2 + x

def three(x):
    return abs(-(x ** 3) + 1) + x ** 3


n = int(input())
cnt = [0, 0, 0]

for i in range(n):
    x,y = map(float,input().split())
    if abs(y - one(x)) <= 0.2:
        cnt[0] += 1
    if abs(y - two(x)) <= 0.2:
        cnt[1] += 1
    if abs(y - three(x)) <= 0.2:
        cnt[2] += 1

found = False
for i in range(3):
    if cnt[i] == n:
        print(i + 1)
        found = True
if found == False:
    print("No ones")

