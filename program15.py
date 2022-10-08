# Write a program to accept an array and display it on the console using functions
from array import *

arr = []


def getArray():
    # arr = array('i', [])
    n = int(input("enter the length of array"))

    for i in range(n):
        x = int(input('enter the value'))
        arr.append(x)


def displayArray():
    print("The array is :", arr)

getArray()
displayArray()