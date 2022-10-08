# Write a program to print the following pattern using for loop
# 1
# 2	3
# 4	5	6
# 7	8	9	10

limit = int(input("enter the limit : "))
num = int(0)
for i in range(1, limit + 1):
    print(" ")
    for j in range(1, i + 1, ):
        num = num + 1
        print(num, end=" ")
