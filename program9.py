# Write a program to print the following pattern (hint: use nested loop)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
limit = int(input("enter the limit : "))
for i in range(1, limit + 1):
    print(" ")
    for j in range(1, i + 1):
        print(j, end=" ")
