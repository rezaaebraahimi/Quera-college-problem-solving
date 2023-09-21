a, b = int(input()), int(input())

result = ""
for i in range(a + 1, b):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 2 and not result:
        result = str(i)
    elif count == 2:
        result += "," + str(i)

print(result)