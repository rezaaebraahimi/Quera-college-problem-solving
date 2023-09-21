n, k = map(int, input().split())
foots = []

for i in range(1, n + 1):
    foots.append(i)
    foots.append(i)
foot_indx = 0
foot_cnt = 1

while True:
    print(foots[foot_indx],end = ' ')
    rmv = False
    if foot_cnt % k == 0:
        foots.pop(foot_indx)
        rmv = True
        print()           
    if len(foots) == 1 or (len(foots) == 2 and foots[0] == foots[1]):
        print('winner:%d'%foots[0])
        break
    foot_cnt += 1
    if rmv == False:
        foot_indx += 1
    foot_indx %= len(foots)