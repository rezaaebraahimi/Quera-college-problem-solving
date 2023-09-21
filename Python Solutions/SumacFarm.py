n = int(input())
height = list(map(int, input().split()))
k = 0
t = 0
if n != 1 and height[k] <= height[k + 1]:
    for i in range(n - 1):
        if height[i] > height[i + 1]:
            for j in range(i, n - 1):
                if height[j] <= height[j + 1]:
                    t += 1
                    
elif n != 1 and height[k] >= height[k + 1]:
    for a in range(n - 1):
        if height[a] < height[a + 1]:
            for b in range(a, n - 1):
                if height[b] >= height[b + 1]:
                    t += 1
if t > 0:
    print("No")
else:
    print("Yes")