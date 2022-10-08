# Write a program to interchange the values of two arrays.
from array import *

arr = array('i', [])
n = int(input('enter the length of array'))

for i in range(n):
    x = int(input('enter the values of array'))
    arr.append(x)
arr1 = array('i', [])
n = int(input('enter the length of second array'))

for i in range(n):
    x = int(input('enter the values of second array'))
    arr1.append(x)


for i in range(len(arr)):
    print(arr[i], end=" ")
print("|")
for i in range(len(arr1)):
    print(arr1[i], end=" ")

temp = arr
arr = arr1
arr1 = temp
print("|")
print("after swaping")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("|")
for i in range(len(arr1)):
    print(arr1[i], end=" ")
