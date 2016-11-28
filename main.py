from classes.myclass import MyClass
import math
import os
import sys


def myFunction():
    print("THIS IS A FUNCTION")


def myFunction2():
    print("THIS IS A FUNCTION22222222222222222222222222222222222222")


def add(x, y):
    return x + y

def print_lines():
    print("oooooo babe babe")
    print("oooooo babe babe")

def printtwice(bruce):
    print(bruce)
    print(bruce)


print(os.open(".",))


print(add(5, 1))
# System.out.print("Hello World")
print("Hello World")

x = 1

# It Statment
if x == 1:
    print("X = 1")
else:
    print("X != 1")

# Int
# int myInt = 7
myInt = 7

# Float
# double = 7.0
myFloat = 7.0
myFloat = float(7)

# Boolean
# boolean myBoolean = true
myBoolean = True

# String
# String myString = "Hello World"
myString = "Hello World"

one = 1
two = 2
three = one + two

print(three)

hello = "Hello"
world = "World"
helloWorld = hello + " " + world

print(helloWorld)

a, b = 3, 4

myList = []
myList.append(1)
myList.append(2)
myList.append(3)

print(myList[0])
print(myList[1])
print(myList[2])

for i in myList:
    print(i)

aString = "A Magic String"

print(aString[3:10])
print(aString[3:10:2])
print(aString[2])
print(aString.upper())
print(aString.lower())

myFunction()
myFunction2()

zzz = MyClass("cake")

zzz.messageMe()


print(type(aString)==type(aString))

print(str(int('11')+one))

print(aString + " " + str(one))

print(str(math.pi * 10))

print(math)
print(type(math))

print_lines()
print(type(print_lines()))

printtwice('17')

exit(0)
