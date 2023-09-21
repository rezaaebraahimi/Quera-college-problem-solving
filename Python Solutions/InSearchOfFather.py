def digits_sum(x):
    sum = 0
    while x > 0:
        sum += (x % 10)
        x //= 10
    return sum

def is_prime(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def prim_div_sum(x):
    sum = 0
    for i in range(2, x + 1):
        if x % i == 0 and is_prime(i):
            sum += i
    return sum

def d(x):
    return x + digits_sum(x) + prim_div_sum(x)

t = int(input())
for q in range(t):
    n = int(input())
    found = False
    for x in range(n):
        if d(x) == n:
            print("Yes")
            found = True
            break
    if found == False:
        print("No")
        
