
Q1 Read two integers from STDIN and print three lines where:
● The first line contains the sum of the two numbers.
● The second line contains the difference between the two numbers (first -
second).
● The third line contains the product of the two numbers.
ANS     a=3
        b=2
        c=a+b
        d=a-b
        e=a*b
        print(c, d, e)


Q2 We add a Leap Day on February 29, almost every four years. The leap day is an extra,
or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap
years:
● The year can be evenly divided by 4, is a leap year, unless:
● The year can be evenly divided by 100, it is NOT a leap year, unless:
● The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
ANS:
a=int(input("put a year"))
if (a%4 == 0) and (a%400 == 0):
    print(True)
elif (a%100 == 0):
    print(False)



Q3 Little Robert likes mathematics. Today his teacher has given him two integers and
asked to find out how many integers can divide both the numbers. Would you like to
help him in completing his school assignment?
ANS:
a=int(input("put no"))
b=int(input("put no"))
l=[]
for i in range(1, a+1):
    if a%i == 0:
        l.append(i)
m=[]
for i in range (1, b+1):
    if b%i == 0:
        m.append(i)
k=print(len(list(set(l).intersection(m))



Q4 You have given a string. You need to remove all the duplicates from the string.
The final output string should contain each character only once. The respective order of
the characters inside the string should remain the same. You can only traverse the
string at once.
ANS:
def removeduplicate(str,n):
    index=0
    for i in range(0, n):
        for j in range (0, n+1):
             if (str[i] == str[j]):
                break
        if (j == i):
            str[index] = str[i]
            index += 1
    return "".join(str[:index])
str= "aabbbcccdd"
n = len(str)
print(removeduplicate(list(str), n))



Q5  Write a Python program to find the first appearance of the substring 'not' and 'poor' from
a given string, if 'not' follows the 'poor', replace the whole 'not'...' poor' substring with
'good'. Return the resulting string
ANS:
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        return  str1.replace(str1[snot:(spoor + 4)], 'good')
    else:
        return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))



Q6 Write a Python program to convert temperatures to and from celsius, Fahrenheit
ANS:
Celsius=int(input("Enter a temperature in celsius"))
Fahrenheit = 9.0/5.0 * Celsius + 32
print('%.2f Celsius is %0.2f in Fahrenheit' %(celsius, fahrenheit))



Q7 Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
(until n-x =< 0)
ANS:
def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)

print(sum_series(6))
print(sum_series(10))



Q8 Write a Python program to get a week number.
ANS:
import datetime
print(datetime.date(2015, 6, 16).isocalendar()[1])



Q9 Write a Python program to count the number of students of the individual class
ANS:
from collections import Counter
classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
students = Counter(class_name for class_name, no_students in classes)
print(students)



Q10 Write a Python program to sort a list of elements using the selection sort algorithm.
ANS:
def elementSort(nlist):
   for i in range(len(nlist)-1,0,-1):
       a=0
       for location in range(1,i+1):
           if nlist[location]>nlist[a]:
               a = location

       temp = nlist[i]
       nlist[i] = nlist[a]
       nlist[a] = temp

nlist = [14,46,43,27,57,41,45,21,70]
elementSort(nlist)
print(nlist)













