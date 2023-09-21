letters = int(input())
original = input()
student = input()

number = 0

for i in range(letters):
    if original[i] != student[i]:
        number += 1

print(number)