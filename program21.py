# Write a program to multiply the adjacent values of an array and store it in an another array
n = int(input("enter the length of array"))
arr =[]
new =[]
for i in range(n):
    x = int(input('enter the value'))
    arr.append(x)

for i in range(n-1):
    y =arr[i]*arr[i+1]
    new.append(y)

print('result = ',new)

