# Write a program to check whether a student has passed or failed in a subject after he or she enters their mark (pass mark for a subject is 50 out of 100).

mark = float(input("enter the mark out  of 100 : "))
if mark < 50:
    print("oops!!! you are failed")
    print("better luck next time")

else:
    print("passed")
