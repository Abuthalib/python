class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return  self.num1 - self.num2
    def mul(self):
        return  self.num1 * self.num2
    def div(self):
        return  self.num1 / self.num2

    def decision(self,user):
        if user == '+':
            return self.add()
        elif user =='-':
            return self.sub()
        elif user == '*':
            return self.mul()
        elif user == '/':
            return self.div()






n1=int(input("enter the 1 number"))
n2 = int(input("enter the 2nd number"))
calc = Calculator(n1,n2)
print("+ for addition")
print("- for subtract")
print("* for multiplication")
print("/ for division")
d = input("enter your choice :")
result = calc.decision(d)
print(result)