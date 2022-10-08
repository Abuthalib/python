# Write a program to find the sum of all the odd numbers for a given limit

limit = int(input("enter a limit : "))
od = 0
for i in range(1, limit + 1):
    if i % 2 != 0:
        od = od + i
print("sum of odd number", od)
