# Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows.

days = {
    1: 'sunday',
    2: 'monday',
    3: 'tuesday',
    4: 'wednesday',
    5: 'thursady',
    6: 'friday',
    7: 'saturday',

}

choice = int(input("enter your choices : "))
print('',days.get(choice,"invalid entry"))
