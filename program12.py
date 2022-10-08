# Program should accept and array, sort the array values in descending order and display it

from array import *

arr = array('i', [])
n = int(input("enter the length of array"))

for i in range(n):
    x = int(input('enter the value'))
    arr.append(x)
print(arr)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("sorted array in descending order is : ", arr)