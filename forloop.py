Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
for i in range(1,6):
    print(i)

    
1
2
3
4
5

for i in range(3):
    print("hello")

    
hello
hello
hello

for i in range(1,11):
    print(i)

    
1
2
3
4
5
6
7
8
9
10

for i in range(1,21):
    if i%2==0:
        print(i)

        
2
4
6
8
10
12
14
16
18
20

for i in range(1,16):
    if i%2!=0:
        print(i)

        
1
3
5
7
9
11
13
15

for i in range(1,11):
    print("5x",i,"=",5*i)

    
5x 1 = 5
5x 2 = 10
5x 3 = 15
5x 4 = 20
5x 5 = 25
5x 6 = 30
5x 7 = 35
5x 8 = 40
5x 9 = 45
5x 10 = 50

name="Atmiya"
for letter in name:
    print(letter)

    
A
t
m
i
y
a

>>> total=0
>>> for i in range(1,6):
...     total=total+i
...     print("sum is:"total)
...     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> total=0
... for i in range(1,6):
...     total=total+i
...     
SyntaxError: multiple statements found while compiling a single statement
>>> for i in range(1,6):
...     total=total+i
...     print("sum is:"total)
...     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> numbers=[10,20,30,40]
>>> for n in numbers:
...     print(n)
... 
...     
10
20
30
40
