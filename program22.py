# Write a program to add the values of two 2D arrays

def GetArr(size, m1, m2):
    print("enter the elemnts of metrix1 : ")

    for i in range(size):
        r = []
        for j in range(size):
            r.append(int(input()))
        m1.append(r)
    print("enter the elemnts of metrix2 : ")
    for i in range(size):
        r = []
        for j in range(size):
            r.append(int(input()))
        m2.append(r)


def AddArray(result, m1, m2):
    print("the result is: ")
    result = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = m1[i][j] + m2[i][j]

    for i in range(size):
        for j in range(size):
            print(result[i][j], end=" ")
        print()

size = int(input("enter the size : "))

m1 = []
m2 = []
result = []
GetArr(size, m1, m2)
AddArray(result, m1, m2)
