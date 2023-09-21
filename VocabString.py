s = input()
s = list(s)

p = input()
p = list(p)

sLen = len(s)
pLen = len(p)

noSolutions = 0
convertedArray = 26 * [0]
for i in range(pLen):
    convertedArray[ord(p[i]) - ord('a')] += 1

for i in range(sLen - pLen + 1):
    tmpConvertedArray = convertedArray.copy()
    foundChars = pLen
    for j in range(pLen):
        if s[i + j] == '?':
            foundChars -= 1
        elif tmpConvertedArray[ord(s[i + j]) - ord('a')] > 0:
            foundChars -= 1
            tmpConvertedArray[ord(s[i + j]) - ord('a')] -= 1
        else:
            break

    if foundChars == 0:
        noSolutions += 1
print(noSolutions)