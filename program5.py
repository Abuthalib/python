# Write a program to show the grade obtained by a student after he/she enters their total mark percentage.

grade = float(input("enter the grade "))
if 90 <= grade <= 100:
    print("you have got A grade")
elif 80 <= grade <= 89:
    print("you have got B grade")
elif 70 <= grade <= 79:
    print("you have got C grade")
elif 60 <= grade <= 69:
    print("you have got D grade")
elif 50 <= grade <= 59:
    print("you have got E grade")
else:
    print("!!!!failed!!!!!")
