# Write a program to check whether a given number is prime or not
num = int(input("enter the number : "))


def IsPrime():
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


IsPrime()
