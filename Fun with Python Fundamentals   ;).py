#!/usr/bin/env python
# coding: utf-8

# # 1. Python output

# In[1]:


# Python is a case sensitive language
print('Die World')


# In[2]:


print('Data Science')


# In[5]:


print(7)


# In[6]:


print(7.7)


# In[7]:


print(True)


# In[8]:


print("hello",1,4.5,True)


# In[9]:


print("Hello",1,4.5,False,sep='-')


# In[10]:


print('hello')
print('world')


# In[11]:


print('Dead',end='-')
print('World')


# # 2. Data Types

# In[12]:


# Integer 
print(8)
#1*10^308
print(1e310)


# In[13]:


# Decimal / Float
print(8.55)
print(1.7e309)


# In[14]:


# Boolean
print(True)
print(False)


# In[15]:


# Text / String
print('Dead World')


# In[16]:


# Complex
print(5+6j)


# In[17]:


# List -> C -> Array
print([1,2,3,4,5])


# In[18]:


# Tuple
print((1,2,3,4,5))


# In[19]:


# Sets
print({1,2,3,4,5})


# In[20]:


# Dictionary 
print({"Fucking":"Shit","Dip":"Shit","Piece":['of','shit']})


# In[21]:


# Type
type({"Oh":"Shit"})


# # 3. Variables

# In[22]:


# Static vs Dynamic typing
# Static vs Dynamic Binding
# Stylish declaration techniques


# In[23]:


# C/C++
name = "Saad"
print(name)

a = 5
b = 6

print(a+b)


# In[22]:


# Dynamic Typing
a = 5
# Static Typing
#int a = 5


# In[23]:


# Dynamic Binding 
a = 5
print(a)
a = "Saad"
print(a)

# Static Binding
#int a = 5


# In[24]:


a = 1 
b = 2
c = 4
print(a,b,c)


# In[25]:


a,b,c = 1,2,4
print(a,b,c)


# In[28]:


a=b=c=5
print(a,b,c)


# # Commments

# In[29]:


# This a comment 
# HOW YOU DOIN'
a = 4
b = 5 #Study Dude
# This also a comment 
print(a+b)


# # 4. Keywords and Identifiers 

# In[30]:


# Keywords
import keyword

keyword_list = keyword.kwlist
print(keyword_list)


# In[31]:


# Identifiers 
# You can't start with a digit 
name1 = "SAAD"
print(name1)
# YOU can use special character -> _
_     = 'saad'
print(_)
# identifiers can not be keywords


# # Temp Heading 

# # 5. User Input

# In[32]:


# Static vs Dynamic 
input(" Enter whatever you want to enter here ps. email is preferred :)")


# In[4]:


# Take input from users and store them in a variable
first = int(input("give"))
second= int(input("me"))
third = int(input("your"))
fourth= int(input("phone"))
fifth = int(input("number"))
sixth = int(input("and"))
seventh=int(input("have"))
eight = int(input("an ANGEL"))
ninth  = int(input("as your"))
tenth = int(input("contact;)"))
#print(type())
# add the 2 variables
Ten_number_ticket_to_an_angel=first,secd+third+fourth+fifth+sixth+seventh+eight+ninth+tenth
# print the result 
print(Ten_number_ticket_to_an_angel)


# # 6. Type Conversion

# # Implicit vs Explicit
# print(5+5.6)
# print(type(5),type(5.6))
# 
# print(4+"4")

# In[37]:


# Explicit
# str -> int
# int(4+5j)

# int to str
print(str(1))

# float
float(453)


# # 7. Literals

# In[7]:


binary_literal = 0b1010
decimal_literal = 42
octal_literal = 0o52
hexadecimal_literal = 0x2A

print(binary_literal)        # Output: 10
print(decimal_literal)       # Output: 42
print(octal_literal)         # Output: 42
print(hexadecimal_literal)   # Output: 42


# In[13]:


# FLoat Literal
float_1 = 10.5
float_2 = 1.5e4 # 1.5*10^4
float_3 = 1.5e-2# 1.5*10^-2

print(float_1,
      float_2,
      float_3)


# In[15]:


# complex Literal 
x = 3.14j
print(x,x.imag,x.real)


# In[16]:


# Binary
x = 3.14j
print(x.imag)


# In[32]:


relative_string = "Beta free rehte ho studies par dhyaan do or successful insan bano"
me_string       = "Seh lo ge aap"
character       =   "U"
multiline_string= """Playing tricks is evilness. Understanding tricks is cleverness but not doing both is innocence."""
unicode         = (["Hello, 你好,வணக்கம்"],["\U0001f600\U0001F606\U0001F923"])
raw_string      = r"raw \n string" #while raw strings treat backslashes as literal characters, they still obey 
                                    #escape sequences for quotes (' and ") and triple quotes (''' and """).
print(relative_string)
print(me_string)
print(character)
print(multiline_string)
print(unicode)
print(raw_string)


# In[26]:


a = True + 4 #True = 1
b = False+10 #False=0

print("a:",a)
print("b:",b)


# In[27]:


p = None
a = 4
b=  5
print('Program exe')


# # 8. Operators

# In[28]:


# arithmetic
# relational
# logical
# bitwise
# assignment
# membership


# In[2]:


# Arithmetic Operators
print(5 + 6)   # Addition: 5 + 6 = 11
print(5 - 6)   # Subtraction: 5 - 6 = -1
print(5 * 6)   # Multiplication: 5 * 6 = 30
print(5 / 2)   # Division: 5 / 2 = 2.5
print(5 // 2)  # Floor Division: 5 // 2 = 2 (integer division, discards the fractional part)
print(5 % 2)   # Modulus: 5 % 2 = 1 (remainder of the division)
print(5 ** 2)  # Exponentiation: 5 ** 2 = 25 (5 raised to the power of 2)


# In[4]:


# Relational Operators
print(4 > 5)   # False (4 is not greater than 5)
print(4 < 5)   # True (4 is less than 5)
print(4 >= 4)  # True (4 is greater than or equal to 4)
print(4 <= 4)  # True (4 is less than or equal to 4)
print(4 == 4)  # True (4 is equal to 4)
print(4 != 4)  # False (4 is not not equal to 4, which means it is equal)


# In[6]:


# Logical operators
print(1 and 0)
print(1 or 0)
print(not 0)
print(not 1)


# In[8]:


# Bitwise Operators :

# Bitwise and 
print(2 & 3)

# Bitwise or
print(2|3)

#Bitwise xor
# Bitwise XOR
print(2 ^ 3)   # Output: 1 (Binary: 0010 XOR 0011 = 0001)

# Bitwise NOT
print(~3)      # Output: -4 (Binary: NOT(0011) = 1100, the result is a two's complement binary representation, so -4 in decimal)

# Bitwise Right Shift
print(4 >> 2)  # Output: 1 (Binary: 0100 >> 2 = 0001)

# Bitwise Left Shift
print(5 << 2)  # Output: 20 (Binary: 0101 << 2 = 10100)


# In[9]:


# Assignment Operators

a  = 2 # Assigns the value 2 to variable a 

a %= 2 # Modifies a to be equal to its value modulo 2 (which  is 0)

# increament a by 1 using +=
a += 1 # Equivalent to a = a+1

print(a)  # Output will be 1


# In[13]:


# Membership Operators 
# in/not in

print('peace' not in "Peace is not in my Life.")

print('dark' in "World is dark, atleast for me.")

print(1 in [3,4,2,4,2,4,5,6,7])


# In[21]:


# Program - Find the sum of the last 3 digit number entered by the user

# Prompting the user to enter a 3 digit number
number = int(input('Enter any number it will ony calculate the addition of last 3 digit : '))

# Extracting individual digits using modulo and integer division
a = number % 10
number = number // 10

b = number % 10
number = number // 10

c = number % 10

# Computing and printing the sum of the digits
print("Sum of the digits:", a + b + c)


# # if - else in python

# In[6]:


#                     [  Ultimate Jaadu   ]
#Program - Find the sum of the 3 digit number entered by the user

def add_three_digits():
   num1 = int(input("pehle ek no. daal:"))
   num2 = int(input("ab dusra daalde:"))
   num3 = int(input("teesra bhi daal hi de:"))
   # Check if all numbers are three digits
   if 0<=num1<=9 and 0<=num2<=9 and 0<=num3<=9:
       jaadu = num1+num2+num3
       return jaadu
   else:
       return "never-Try Again"
   
# Example usage:
print("Teen number daal aur jaadu dekh:")
print("aaila jaadu:", add_three_digits())


# In[4]:


#                                               [Gaand faadu code]
# login program and indentation
# email --> datadudesaadkhan@gmail.com
# password --> Baigan

email = input("apna email bataiye :")
password = input("kuch huwa tow hamari responsibility nahi hai:")

if email == "datadudesaadkhan@gmail.com" and password =="Baigan":
    print("Welcome user")
elif email == "datadudesaadkhan@gmail.com" and password !="Baigan":
    # tell the user
    print("Dimak ke andhe password galat dala hai tunne")
    password=input("Abki baar dhang se daal")
    if password =="Baigan":
        print("Subha ka bhula , shaam ko wapas agaya")
    else:
        print("Tum se na ho paega")
else:
    print("Gian he aap ==> [p.s. Doremon waala]")


# In[ ]:


# menu driven calculater
menu = input("""
Aur bhai calculate karne ke liye paisa bhi tow hona chaiye :( 
1. Pin change karega tow 1 daba
2.Paisa kitna hai pata karne ka hai tow 2 daba
3.Paisa nikal na hai tow 3 daba ps. agar hoga tabhi niklega
4.Wapas jaana hai tow 4 daba
""")

if menu =='1':
    print('pin change')
elif menu=='2':
    print('le balance dekh')
else:
    print('Wapas bhejo isko')


# # Modules in Python
# math
# 
# keywords
# 
# random
# 
# datetime

# In[57]:


# math
import math
math.sqrt(225)


# In[58]:


# Keyword
import keyword
print(keyword.kwlist)


# In[69]:


# random
import random
# Generate a random integer between a specified range (inclusive)
random_number = random.randint(1, 100)
print(random_number)
# Generate a random floating-point number between 0 and 1
random_float = random.random()
print(random_float)
# Generate a random floating-point number between a specified range
random_float_range = random.uniform(10.5,31.5)
print(random_float_range)


# In[72]:


# Datetime
import datetime
# Get the current date and time
current_datetime = datetime.datetime.now()
print(current_datetime)
# Format a datetime object
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)
# Parse a string into a datetime object
parsed_datetime = datetime.datetime.strptime("2024-03-07 12:30:45", "%Y-%m-%d %H:%M:%S")
print(parsed_datetime)


# In[21]:


help('modules')


# # Loops in Python
# 
# Need for Loops
# 
# While Loop
# 
# For Loop

# In[74]:


# While loop example -> program to print the table
# Program -> Sum of all digits of a given number
# Program -> keep accepting numbers from users till he/she enters a 0 and then find the avg


# In[78]:


number = int(input('enter the number'))

i = 1

while i<11:
  print(number,'*',i,'=',number * i)
  i += 1


# In[4]:


# while loop with else 
x = 1
while x<12:
 print(x)
 x += 1
        
else:
 print('Bohot ho gaya')


# In[5]:


# kon bane ga crorepati 
 # generate a random integer between 1 to 100
import random
jaadu = random.randint(1,100)
guess = int(input("bolo bacha"))
counter = 1
while guess != jaadu:
    if guess < jaadu:
      print('galat jawab! high ho jao')
    else:
      print('galat jawab! low jao')
            
    guess = int(input('bolo bacha'))
    counter+=1
else:
    print('sahi jawab')
    print('your_chanches',counter)


# In[7]:


# For loop demo
  
for i in {1,2,3,4,5}:
    print(i)


# In[8]:


# For loop examples


# Program - The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years.

# In[9]:


curr_pop = 10000

for i in range(10,0,-1):
    print(i,curr_pop)
    curr_pop = curr_pop-0.1*curr_pop


# # Sequence sum

# In[12]:


import math


# In[13]:


math.factorial(5)


# In[19]:


sequence = [(1/math.factorial(1))+(2/math.factorial(2))+(3/math.factorial(3))]
total = sum(sequence)
print("Sum of the sequence:", total)


# In[15]:


for i in range(5):
    print(math.factorial(i))


# In[20]:


sequence = [1, 2, 3, 4, 5]
total = sum(sequence)
print("Sum of the sequence:", total)


# In[4]:


n = int(input('enter n'))
 
result = 0
fact = 1

for i in range (1,n+1):
    fact = fact*i
    result = result+i/fact
    
print(result)


# # Nested Loops

# In[5]:


# Examples --> unique pairs

for i in range(1,5):
    for j in range(1,5):
        print(i,j)


# # Pattern 1

# *
# 
# **
# 
# ***

# In[13]:


# Code here
rows = int(input('enter the number of rows'))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print('*',end='')
    print()


# pattern 2
# 
# 1
# 
# 121
# 
# 12321
# 
# 1234321

# In[17]:


# Code here
rows = int(input('enter number of rows'))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
        
    print()


# # Loop Control Statement
# 
# Break
# 
# Continue
# 
# Pass

# In[18]:


for i in range(1,10):
    if i == 5:
        break
    print(i)


# In[21]:


lower = int(input('Enter lower range: '))
upper = int(input('Enter upper range: '))

for i in range(lower, upper + 1):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)


# In[26]:


# Continue 
for i in range (1,10):
    if i==5:
        continue
    print(i)
#when i is equal to 5, the print(i) statement is skipped due to the continue statement, and the loop continues with the next value of i.


# In[31]:


for i in range (1,10):
    pass
print(i)
#This behavior is because i retains its value after the loop ends due to its scope in Python'

Strings are sequence of characters

In python specifically , strings are a sequence of unicode characters
Creating Strings
Accessing Strings
Adding Chars to String
Editing Strings
Deleting Strings
Operations on Strings
String Functions

# # Creating Strings

# In[33]:


s = "hello"
s = 'hello'
#Multiline strings
s = '''hello'''
s = """hello"""
s = str('hello')
print(s)


# In[38]:


'Skin to Skin is not enough , I want to take a nap inside your ribcage.'


# # Accessing Substrings from a String

# In[39]:


# Positive Indexing 
s = 'Dead World'
print(s[2])


# In[40]:


# Negative Indexing
s = 'Dead World'
print(s[-3])


# In[41]:


# Slicing
s = 'Dead World'
print(s[6:0:-2])


# In[44]:


s= 'devil neve reven lived'
print(s[::-1])


# In[46]:


s = 'World is Vivid'
print(s[-1:-6:-1])


# # Editing and Deleting in Strings

# In[96]:


s = ['hello world',32,43] #Strings are immutable
del s[0]
print(s)


# In[99]:


s = ['Dead World','Suuiii','timro pratiksha',0,32,4,54,4]
del s[-1:-5:2]
print(s)


# # Operations on strings

# Arithmetic Operations
# 
# Relational Operations
# 
# Logical Operations
# 
# Loops on Strings
# 
# Membership Operations

# In[102]:


print('Nagpur'+' '+"Bhusawal")


# In[106]:


print('Gian hai aap - '*5)


# In[107]:


print("*"*50)


# In[112]:


"Pandas" != "Pandas" and "Pandas" == "Pandas" 


# In[114]:


"pune">"PUNE"
#When comparing strings, lowercase letters are considered to be greater than uppercase letters.


# In[116]:


"mumbai" > "pune" #lexicographic (dictionary) order. i.e m comes before p. so P is high and M is less.


# In[117]:


'Dead' and "World" # It converts the string into bytes and the highest is printed


# In[120]:


'Shitty' or 'world' # It converts the string into bytes and the lowest is printed.


# In[122]:


'' and "world"


# In[124]:


'' or 'world'


# In[125]:


not 'World'


# In[127]:


for i in'Dead':
    print(i)


# In[128]:


for i in 'A Being':
    print("Survivor")


# In[129]:


"D" in 'delhi'


# # Common Functions
# 
# len
# 
# max
# 
# min
# 
# sorted

# In[131]:


len('Dead World') # length of the object


# In[132]:


max("Dead World") # alphabetically last alphabet


# In[135]:


min("deadworld") # alphabetically first alphabet


# In[136]:


sorted('dead world',reverse=True)


# # Capitalize/Title/Upper/Lower/Swapcase

# In[140]:


s= "may flowers grow in the saddest parts of you"
print(s.capitalize())
print(s)


# In[141]:


s.title()


# In[142]:


s.upper()


# In[143]:


'MAY FLOWERS GROW IN THE SADDEST PARTS OF YOU'.lower()


# In[144]:


'May Flowers Grow In The Saddest Parts Of You'.swapcase()


# # Count/Find/Index

# In[148]:


a = "I am datadude saad khan."


# In[149]:


a.count('a')  # How many times a is used in sentence.


# In[151]:


a.find('x')  # If the substring 'x' is not found in 'a' variable the -1. 


# In[153]:


a.find('m') # Index postion of 'm' in variable.


# In[155]:


a.index('k') #Index postion of 'k' in variable but throws error if substring not found.


# # endswith / startswith

# In[157]:


e = 'Baby I dont need no dollar bills to have fun tonight , I love cheap thrills.'


# In[159]:


e.endswith('rills.')


# In[161]:


e.startswith('Bab')


# # Format

# In[163]:


feeling  = 'solitude'
heart    = 'shattered'
"A sprout of darkness is {0} and it {1} me from inside.".format(feeling,heart)


# # isalnum/ isalpha/ isdigit/ isidentifier

# In[164]:


'Self-Destroyer69'.isalnum()


# In[166]:


"FredrickNeitschze".isalpha()


# In[167]:


'77afn'.isdigit()


# In[168]:


name1 = "variable_name"
print(name1.isidentifier())  # Output will be True


# # Split/Join

# In[170]:


'hi my name is Saad'.split()


# In[171]:


" ".join([" ".join(['hi', 'my', 'name', 'is', 'Saad'])])


# # Replace

# In[173]:


'hi', 'my', 'name', 'is', 'Saad'.replace('Saad','datadude')


# # Strip

# In[174]:


'Besabriyaan           '.strip()


# # Example Programs

# In[175]:


## Find the length of a given string without using the len() function

s = input('enter the string')

counter = 0

for i in s:
    counter += 1
    
print('length of the string',counter)
    


# In[176]:


# Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh

s = input('Apna email dalia.')

pos = s.index('@')
print(s[0:pos])



# In[182]:


# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

s = input('apna email dalia.')
term = input('kiski frequency janna chahenge aap.')

counter = 0
for i in s:
  if i == term:
    counter += 1

print('frequency',counter)


# In[1]:


# Write a program which can remove a particular character from a string.
s = input('enter the string')
term = input('what would you like to remove')

result = ''

for i in s:
  if i != term:
    result = result + i

print(result)


# In[188]:


# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

s = input('enter the string')
flag = True
for i in range(0,len(s)//2):
  if s[i] != s[len(s) - i -1]:
    flag = False
    print('Haule, galat daala hai tuh.')
    break

if flag:
  print('Palindrome')



# In[192]:


# Write a program to count the number of words in a string without split()

s = input('enter the string')
L = []
temp = ''
for i in s:

  if i != ' ':
    temp = temp + i
  else:
    L.append(temp)
    temp = ''

L.append(temp)
print(L)


# In[190]:


# Write a python program to convert a string to title case without using the title()
s = input('enter the string')

L = []
for i in s.split():
  L.append(i[0].upper() + i[1:].lower())

print(" ".join(L))


# In[191]:


# Write a program that can convert an integer to string.

number = int(input('enter the number'))

digits = '0123456789'
result = ''
while number != 0:
  result = digits[number % 10] + result
  number = number//10

print(result)
print(type(result))

