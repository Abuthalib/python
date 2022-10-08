# Accept an input from the user and display its multiplication table

x = int(input('enter the number : '))

for i in range(1,11):
    print(i, '*', x,'=', i * x)
