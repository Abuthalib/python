# Write a program to find the number of even numbers in an array

from array import *

arr = array('i', [])
n = int(input("enter the length of array"))

for i in range(n):
    x = int(input('enter the value'))
    arr.append(x)
print(arr)
print("even numbers in array are : ")
for j in arr:
    if j % 2 == 0:
        print(j)