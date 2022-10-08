# Write a program to identify whether a string is a palindrome or not

a = input("enter the srting :")
b = a[-1::-1]
if a == b:
    print(a, ': its a palindrome')
else:
    print(a, 'it is not a palindrome')
