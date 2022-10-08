# Write a program to add to two dimensional arrays
from array import *

row = int(input("enter the row  : "))
col = int(input("enter the cols : "))

print("enter the elements for matrix1 : ")
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print("matrix1 is : ")
for i in range(row):
   for j in range(col):
       print(matrix1[i][j], end=" ")
   print()

print("enter the elements for matrix2 : ")
matrix2 = [[int(input()) for i in range(col)] for j in range(row)]
print("matrix2 is : ")
for i in range(row):
   for j in range(col):
       print(matrix2[i][j], end=" ")
   print()
print("the result is :")
result = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
   for j in range(col):
       result[i][j]= matrix1[i][j] + matrix2[i][j]

for i in range(row):
   for j in range(col):
       print(result[i][j], end=" ")
   print()




