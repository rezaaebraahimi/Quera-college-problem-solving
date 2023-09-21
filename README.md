#  حل مسائل و تمرینات دوره برنامه نویسی پایتون کوئرا کالج
# Solving problems of Quera College's Python programming course


- In this repository, I tried to solve problems of **Quera College's Python programming course**.

+ I try to do this in **my own way**, but you can solve the problems according to **your own point of view**. <br>


<br> <br>


# رشته بلند | Long string

<h4>Ali, who was able to design a system to simulate the football league the other day, has become somewhat proud and boasts of his abilities. Now he wants to implement another system for validating strings, but because of the fatigue of the previous project, he doesn't want his system to be too complicated!

This system initially has a number as a good amount, whose value is equal to zero.

Also, to get started, a string consisting of English uppercase and lowercase letters and the characters # and ! And ? And . It is given to a maximum length of 1000.
  Also note that the string does not contain spaces. We call this string a suspicious string.

Now, there are operations that are applied on this string and with it the degree of validity of the string can be recognized.</h4>


<h6>Python Solution</h6>

```python
def copy(key, count):
    global suspiciousString
    text = key * count
    suspiciousString = text + suspiciousString[len(text):]


def compare(key):
    global suspiciousString
    global goodLevel
    if suspiciousString == key:
        goodLevel += 1


def substr(key, count):
    global suspiciousString
    global goodLevel
    if suspiciousString.count(key) == count:
        goodLevel += 1


def attach(key, count, str):
    global suspiciousString
    global goodLevel
    key += str
    if suspiciousString.count(key) == count:
        goodLevel += 1


def length(count):
    global suspiciousString
    global goodLevel
    if len(suspiciousString) == count:
        goodLevel += 1


def loop(inputer):
    global countCommand

    if inputer == "Is it right or not?":
        return

    inputer = inputer.split(" ")

    countCommand += 1

    if "copy" == inputer[0]:
        copy(key=inputer[1], count=int(inputer[2]))

    elif "compare" == inputer[0]:
        compare(key=inputer[1])

    elif "substr" == inputer[0]:
        substr(key=inputer[1], count=int(inputer[2]))

    elif "attach" == inputer[0]:
        attach(key=inputer[1], count=int(inputer[2]), str=inputer[3])

    elif "length" == inputer[0]:
        length(count=int(inputer[1]))

    loop(input())


goodLevel = 0
suspiciousString = input()
countCommand = 0

loop(input())

if goodLevel >= (countCommand // 2):
    print("Eyval")

else:
    print("HeifShod")
```


# رشته‌های وارواژه | Vocabulary strings

<h4>In complete disbelief, Muhammad also said this famous sentence and proved to everyone that the strange method they took to close the distance between their minds worked! Now the distance between Muhammad and Irfan's mind tends to zero and they are very happy! Before finally starting to develop the project, they decided to code together a little to warm up, but unfortunately, they still don't have enough command of Python coding.

Since none of Mohammad and Irfan's work was normal, learning Python is no exception to this rule! They asked you to help them solve a question so that they can fully master Python!

A string S is a synonym for a string T if it is possible to get the string T by permuting the letters of the string S.
  For example, aba is a wildcard for the string aab, but not a wildcard for the string aaa.

The S string is a string that contains English lowercase letters and a number of characters ? Is. Also, the P string is a string that only contains English lowercase letters. A substring of S is called a good substring if it is possible to obtain a substring of P by placing arbitrary letters instead of ?.</h4>


<h6>Python Solution</h6>

```python
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
```


# مربع جادویی | Magic Square

<h4>A magic square is an n×n matrix in which the numbers m to m + n^2 - 1 are located and the sum of the numbers of each row, each column and each diagonal is equal. The figure below shows a 3x3 magic square where the numbers 1 to 9 are placed and the sum of the numbers of each row, column and diameter is equal to 15.

A solution to make a magic square of odd order (when n is odd), put the minimum of m numbers in the house number (n + 1)/2 of the first row and then start putting numbers from number k=m+1 according to the algorithm is below
  It should be noted that the highest row is number one, the lowest row is number n, the leftmost column is number one, and the rightmost column is number n.</h4>

<img src="https://bayanbox.ir/view/4979329822923064904/10.png" alt="magic square">

<h4>
move right-up; So if the current house is row i and column j, the next house will be row i-1 and column j+1.

If the row number and column number of the house are from one to n, go to step number 3. Otherwise, if the row number is zero, change the row number to n, and if the column number is n+1, change it to one.

If the house is already filled by a number, increase the row number by one (go down one row); Otherwise, go to step 4.

Put the number k in the house. If all the houses are full, the magic square is made; Otherwise, increase the number by one and repeat step one.

In the figure below, m is equal to or one and n is equal to three. The steps of this algorithm are observed in order. As you can see, the output of the algorithm is a magic square, the sum of each row, column or diameter is equal to 15. Now write a program that first receives the number n and then the number m mentioned above and produces the magic square according to the mentioned algorithm.</h4>
<img src="https://bayanbox.ir/view/5703298927176223485/11.png" alt="magic square algorithm">

<h6>Python Solution</h6>

```python
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

```


# مزرعه سماق | Sumac Farm

<h4>Arya wants to buy a terraced farm and cultivate sumac in it. He goes to Bajnaq to offer him a piece of land. Asghar shows Aria a picture of a land. Now Aria wants to see if he can turn this land into a sumac farm or not?

Since sumac is a sensitive plant, it can only be cultivated under certain conditions. Sumac can only be planted in land that has a peak or valley. Each floor is a sequence of n steps, each of which has a certain height, and we denote the height of the i-th step with a_i.
A land has peaks or valleys if i exists. For the existence of i, one of the following two conditions is sufficient.


a_1 <= a_2 <= ... <= a_i > ... > a_n

a_1 >= a_2 >= ... >= a_i < ... < a_n

Note that i can be equal to n.</h4>


<h6>Python Solution</h6>

```python
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
```



# شماره رند | Catchy Number

<h4>Uncle Scrooge has decided to order a catchy phone number at the end of the year. Uncle Scrooge's number must be 8 digits long and not start with a zero (for example, the phone number 01234567 is not valid).
  
Uncle Scrooge believes a phone number is catchy if it has at least one of the following conditions:
  
1. There must be a digit that is repeated at least 4 times.
2. Three consecutive digits in this number are equal.
3. Be a mirror number. That is, if we write the number from the right, it will be equal to itself.

Uncle Scrooge is picking catchy numbers and asks you to help him figure out catchy numbers. So it gives you t phone numbers and asks you to check which of these t phone numbers are catchy.
</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python
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

```


# Problem - 017

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 018

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 019

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 020

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 021

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 022

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 023

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 024

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 025

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 026

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 027

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 028

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 029

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 030

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 031

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```




# Problem - 032

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 033

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 034

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 035

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 036

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 037

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 038

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 039

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 040

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 041

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 042

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 043

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 044

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 045

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 046

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 047

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 048

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 049

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 050

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 051

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 052

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 053

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 054

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 055

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 056

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 057

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 058

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 059

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 060

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 061

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 062

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 063

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 064

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 065

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 066

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 067

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 068

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 069

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 070

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 071

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 072

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 073

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 074

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 075

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 076

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 077

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 078

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 079

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 080

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 081

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 082

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 083

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 084

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 085

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 086

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 087

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 088

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 089

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 090

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 091

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 092

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 093

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 094

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 095

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 096

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 097

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```

# Problem - 098

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```
