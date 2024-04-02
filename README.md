#  حل مسائل و تمرینات دوره برنامه نویسی پایتون کوئرا کالج
# Solving problems of Quera College's Python programming course


- In this repository, I tried to solve problems of **Quera College's Python programming course** in **my own way**, but you can solve the problems according to **your own point of view**. <br>


<br>

<h1>Link to my valid certification at Quera College:<br>
<a href="https://quera.org/certificate/wnC1vy5y/"> View Certification  </a>
</h1><br>



# مربع جادویی_Magic Square

<h4>A magic square is an n×n matrix in which the numbers m to m + n^2 - 1 are located and the sum of the numbers of each row, each column and each diagonal is equal. The figure below shows a 3x3 magic square where the numbers 1 to 9 are placed and the sum of the numbers of each row, column and diameter is equal to 15.

A solution to make a magic square of odd order (when n is odd), put the minimum of m numbers in the house number (n + 1)/2 of the first row and then start putting numbers from number k=m+1 according to the algorithm is below
  It should be noted that the highest row is number one, the lowest row is number n, the leftmost column is number one, and the rightmost column is number n.</h4>

<div align="center"><img src="https://bayanbox.ir/view/4979329822923064904/10.png" alt="magic square"></div>

<h4>
move right-up; So if the current house is row i and column j, the next house will be row i-1 and column j+1.

If the row number and column number of the house are from one to n, go to step number 3. Otherwise, if the row number is zero, change the row number to n, and if the column number is n+1, change it to one.

If the house is already filled by a number, increase the row number by one (go down one row); Otherwise, go to step 4.

Put the number k in the house. If all the houses are full, the magic square is made; Otherwise, increase the number by one and repeat step one.

In the figure below, m is equal to or one and n is equal to three. The steps of this algorithm are observed in order. As you can see, the output of the algorithm is a magic square, the sum of each row, column or diameter is equal to 15. Now write a program that first receives the number n and then the number m mentioned above and produces the magic square according to the mentioned algorithm.</h4>
<div align="center"><img src="https://bayanbox.ir/view/5703298927176223485/11.png" alt="magic square algorithm"> </div>

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


# مزرعه سماق_Sumac Farm

<h4>Arya wants to buy a terraced farm and cultivate sumac in it. He goes to Bajnaq to offer him a piece of land. Asghar shows Aria a picture of a land. Now Aria wants to see if he can turn this land into a sumac farm or not?

Since sumac is a sensitive plant, it can only be cultivated under certain conditions. Sumac can only be planted in land that has a peak or valley. Each floor is a sequence of n steps, each of which has a certain height, and we denote the height of the i-th step with a_i.
A land has peaks or valleys if i exists. For the existence of i, one of the following two conditions is sufficient.


a_1 <= a_2 <= ... <= a_i > ... > a_n

a_1 >= a_2 >= ... >= a_i < ... < a_n

Note that i can be equal to n.</h4>

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


# شماره رند_Catchy Number

<h4>Uncle Scrooge has decided to order a catchy phone number at the end of the year. Uncle Scrooge's number must be 8 digits long and not start with a zero (for example, the phone number 01234567 is not valid).
  
Uncle Scrooge believes a phone number is catchy if it has at least one of the following conditions:
  
1. There must be a digit that is repeated at least 4 times.
2. Three consecutive digits in this number are equal.
3. Be a mirror number. That is, if we write the number from the right, it will be equal to itself.

Uncle Scrooge is picking catchy numbers and asks you to help him figure out catchy numbers. So it gives you t phone numbers and asks you to check which of these t phone numbers are catchy.
</h4>
<h6> </h6>

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





# رشته‌های وارواژه_Vocabulary strings

<h4>In complete disbelief, Muhammad also said this famous sentence and proved to everyone that the strange method they took to close the distance between their minds worked! Now the distance between Muhammad and Irfan's mind tends to zero and they are very happy! Before finally starting to develop the project, they decided to code together a little to warm up, but unfortunately, they still don't have enough command of Python coding.

Since none of Mohammad and Irfan's work was normal, learning Python is no exception to this rule! They asked you to help them solve a question so that they can fully master Python!

A string S is a synonym for a string T if it is possible to get the string T by permuting the letters of the string S.
  For example, aba is a wildcard for the string aab, but not a wildcard for the string aaa.

The S string is a string that contains English lowercase letters and a number of characters ? Is. Also, the P string is a string that only contains English lowercase letters. A substring of S is called a good substring if it is possible to obtain a substring of P by placing arbitrary letters instead of ?.</h4>

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



# رشته بلند_Long string

<h4>Ali, who was able to design a system to simulate the football league the other day, has become somewhat proud and boasts of his abilities. Now he wants to implement another system for validating strings, but because of the fatigue of the previous project, he doesn't want his system to be too complicated!

This system initially has a number as a good amount, whose value is equal to zero.

Also, to get started, a string consisting of English uppercase and lowercase letters and the characters # and ! And ? And . It is given to a maximum length of 1000.
  Also note that the string does not contain spaces. We call this string a suspicious string.

Now, there are operations that are applied on this string and with it the degree of validity of the string can be recognized.</h4>


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
    print("Great!")

else:
    print("Oh,No!")
```


<br> <br>


# کشف معادله_Discover the equation

<h4>Write a program that takes n and the coordinates of n points (x and y respectively) and declares which of the graphs these points belong to and prints the number of the graph and if it does not belong to any of them, prints the statement No ones .

  In order for a group of points to belong to a graph, it is enough for each of the n points that the difference between the y point and the y graph at that point is less than or equal to 0.2.

  Define a separate function for each of the following equations.</h4>

```python
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

```


# آلفا قنطورس_Alpha Centauri

<h4>In one of the planets of the Alpha Centauri system (Alpha Centauri - the closest star system to the solar system), strange creatures live and each of them has a different number of fingers.
  Some of them, like us, have ten fingers on their two hands, and some have 16 fingers, some have 2 fingers, some have 6 fingers, etc., for this reason, there are different schools for different beings on this planet, and in each school, numbers are Children are taught on a different basis.

Kianush, who is one of the inhabitants of this planet and has 10 fingers, is very interested in programming, he wants to write a program that takes a number in base 10 and moves it to the desired base.

Help him solve this programming problem.</h4>

```python
def NumberToChar(number):
    if 0 <= number <= 9:
        return chr(ord('0') + number)

    else:
        return chr(ord('A') + number - 10)


def baseConverter(keeper, number, base):
    if base == 10:
        return str(number)

    else:
        while True:
            if number > 0:
                keeper += NumberToChar(number % base)
                number = int(number / base)
            else:
                break

        return keeper[::-1]


n, b = input().split(" ")
print(baseConverter(keeper="", number=int(n), base=int(b)))
```


# اتل متل توتوله_Atal Matal Tutule

<h4>After Mohammad and Irfan realized that their minds were far apart in a strange way, they tried to fix the distance between their minds with an even stranger way!

Together with n−2 of their friends, they play the game Ettelmoteltotole. (Note that there are n people in total) Now Irfan, who thinks this game is very ridiculous, wants you to write a program that tells the result of the game at each stage.

More precisely, in each stage of the game, a poem with k words is read, and after saying each word, we go from one leg to the next, and if we reach the last leg, we start again from the beginning. At the end of each step, the foot on which the last word was read is removed. Note that each person has two legs and the first leg is the leg of person number 1.

Now your program should print the progress of each step in 2n−1 lines (the number of game steps it takes until only one leg remains) (see the examples for a better understanding). Finally, determine the winner of the game.

Note that in the case that at the end there is only one person left on both legs, you should not print the last step and the winner will be determined.</h4>


```python
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
```



# باغچه رز_Rose garden

<h4>Wald has a row of roses, each of which wilts and blooms again at the end of each month, and each time you go again it can be white or black.
  Wold, who knows his flowers well, knows that if after the end of the period (meaning the period of a number of months in a row), the number of times the white flower has given is even, that rose is unlucky and should be picked.

In this case, the first flower was white twice, which is an even number, so the first flower is unblessed and should be picked, but the second flower was white only once, which is an odd number, so it is a good flower.

Now, you will be given the number of months of the period and the color of each flower in each month; You have to say at the end of the period that each flower is blessed or not.
</h4>

```python
n,m = input().split()
n,m = int(n),int(m)

w_counter = [0 for k in range(n)]
for i in range(m):
    colors = input()
    for j in range(n):
        if colors[j]=="W":
            w_counter[j]+=1

output_list = ["F" if x%2!=0 else "B" for x in w_counter]
print("".join(output_list))
```

# در جستجوی پدر_In search of father

<h4>We define the function D(x) as: x + the sum of the digits of x + the sum of the prime factors of x.
  We call x the parent of D(x).

  Write a program that reads a t from the input in the first line, then takes a number from the input in the next line, if that number has a father, it prints Yes in one line and No otherwise.

  For example, number 12 is the father of number 20:

20 = (2+3) + (1+2) + 12

It is preferable to write a function for adding the digits of a number, finding the prime factors of a number, and for calculating D(x).

Note that if you perform many operations, you may face a time limit.</h4>

```python
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
        
```



# اول بینی_Find prime

<h4>Write a program that takes the two ends of an interval from the user, such as (a, b) and prints the prime numbers inside that interval. 
  Output numbers must be separated by commas (,). 
  
  The start and end of the interval should not be considered.</h4>
```python
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
```


# تست بینایی_Vision test

<h4>Mohammad Rezas, who passed his entrance exam, wants to participate in all Quora programming competitions; But now it is involved in taking vision test from students applying for driver's license.

Mohammad Rezas places a word of English letters at a distance of two meters from the student, and the student must write exactly on it. Then Mohammad Rezas should tell him the number of wrongly written letters as the amount of blindness of this person.

Mohammad Rezas is in a hurry to give the Quora competition and wants to do the vision test on a computer, so he requested that you write a program that outputs the number of mistakes by the student by taking the input of the word placed in front of the student and the word written by the student.</h4>
```python
letters = int(input())
original = input()
student = input()

number = 0

for i in range(letters):
    if original[i] != student[i]:
        number += 1

print(number)
```


# دیتابیس خیلی بزرگ_Very large database

<h4> The database manager has his own strictures, and to make sure Behrouz is right for the job, he made the challenge even more complicated. This time, he has the same request as before, but he has made the list of numbers and the number of queries so large that if he wants to solve the question by linear search, it will take many years! And the bad news is that Behrouz's manager is very impatient. So this time help him to solve the question by binary search method.

Input
In the first input line, the numbers n and q are given.

In the next line, the a_i's are arranged.

then q line as ? x is given, which means whether the number x is in the sequence or not.

1 <= n,  q <= 100000, 1 <= a[i], x <= 10^9
 

output
In q output line, 1 is output in each line if the corresponding number is in the list and 0 otherwise. </h4>

```python
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
```


# مرتبسازی خفن_Sorting out

<h4>Suppose you are a sorter and you want to sort the students of a school.

A student is better than b if the correct part of a's grade point average is greater than the correct part of b's grade point average. And if this value is equal in both, then a student is better if the number of sports he knows is more.

The correct component of a positive number such as x, which we denote by ⌊x⌋, is the number obtained by removing the digits after the decimal point of x.

You are required to provide a list of student names in sorted order. In this list, the first student is the best. </h4>

```python
n = int(input())
names = []
averages = []
sports = []
perm = []


for i in range(0, n):
    perm.append(i)
    name = input()
    names.append(name)
    data = input().split(" ")
    count = int(data[0])
    sum = 0
    for j in range(0, count):
        sum += float(data[j + 1])

    averages.append(sum / count)

    data = input().split(" ")
    count = int(data[0])

    sports.append(count)


def better(id1, id2):
    if int(averages[id1]) != int(averages[id2]):
        if averages[id1] > averages[id2]:
            return True
        return False
    if sports[id1] != sports[id2] :
        if(sports[id1] > sports[id2]):
            return True
        return False
    if id1 < id2:
        return True
    return False

for i in range(0, n - 1):
    for j in range(1, n):
        if(better(perm[j], perm[j - 1])):
            temp = perm[j]
            perm[j] = perm[j - 1]
            perm[j - 1] = temp

for i in range(0, n):
    print (names[perm[i]])

```


# مثلث خیام پاسکال_Pascal's triangle

<h4> Write a program that takes the number n from the input and displays the first n rows of Pascal's triangle.

Khayyam Pascal's triangle is such that there is only one number 1 in the first row. Then, in line i, there are i numbers whose first and last numbers are 1, and each of the other numbers is the sum of the two upper numbers. The picture below is the first six lines of Khayyam Pascal's triangle.

<div align="center"><img src="https://s8.uupload.ir/files/pascaltriangleanimated2_6pe.gif" alt="pascals triangle"></div>
</h4>

```python
def printPascal(n):
    for line in range(0, n):
        for i in range(0, line + 1):
            print(binomialCoeff(line, i),
                  " ", end="")
        print()


def binomialCoeff(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


n = int(input())
printPascal(n)
```


# تغییرات آرایوی_Arrays change

<h4>
In this question, we want to create a simple database using an array. Suppose all our information is in the form of numbers that are placed in an array.

 We can add a number to the array, or remove a number from it. More precisely, assume that the numbers a[1], a[2], ..., a[n] are in the array, at each step we either add a number such as x in the i position or the number in the i position We delete By adding a new number in position i,
 
  all the numbers that were previously in positions i to n move forward by one unit.
</h4>

```python
ls = []
chr_inpt = []

q = int(input())

for n in range(q):
    chr_inpt = list(input().split())
    
    if chr_inpt[0] == '+': 
        ls.insert(int(chr_inpt[1])-1,int(chr_inpt[2]))
        print(*ls, sep=' ')

    elif chr_inpt[0] == '-':
        ls.pop(int(chr_inpt[1])-1)
        print(*ls, sep=' ')
        if ls == []:
            print('EMPTY')
            pass
```
