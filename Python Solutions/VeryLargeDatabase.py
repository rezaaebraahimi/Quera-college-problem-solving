n, q = map(int, input().split())
numbers = input().split()
for i in range(q):
    question_mark,num = input().split()
    num = int(num)
    Min = 0
    Max = n
    while(Max - Min > 1):
        mid = int((Max + Min) / 2)
        if int(numbers[mid]) <= num:
            Min = mid
        elif int(numbers[mid]) > num:
            Max = mid
    if int(numbers[Min]) == num:
        print(1)
    else:
        print(0)