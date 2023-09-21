def cond1(phone):
    for i in phone:
        cnt = 0
        for j in phone:
            if i == j:
                cnt += 1
        if cnt >= 4:
            return True
    return False

def cond2(phone):
    duplicated =  1
    for i in range(1, len(phone)):
        if phone[i] == phone[i - 1]:
            duplicated += 1
            if duplicated >= 3:
                return True
        else:
            duplicated = 1
    return False

def cond3(phone):
    for i in range(len(phone) // 2):
        if phone[i] != phone[len(phone) - 1 - i]:
            return False
    return True

t = int(input())
for q in range(t):
    phone = input()
    if cond1(phone) or cond2(phone) or cond3(phone):
        print("Ronde!")
    else:
        print("Rond Nist")
