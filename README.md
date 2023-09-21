#  حل مسائل و تمرینات دوره برنامه نویسی پایتون مقدماتی کوئرا کالج
# Solving problems of Quera College's fundamental Python programming course


- In this repository, I tried to solve problems of **Quera College's fundamental Python programming course**.

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


# Problem - 014

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```


# Problem - 015

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

```



# Problem - 016

<h4>Question</h4>
<h6> </h6>

<h6>Python Solution</h6>

```python

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
