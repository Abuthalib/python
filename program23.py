# Write an object oriented program to store and display the values of a 2D array
class Matrix:
    def __init__(self,size,m1):
        self.size=size
        self.m1 =m1
    def GetArr(self):
        print("enter the elemnts of metrix : ")

        for i in range(self.size):
            r = []
            for j in range(self.size):
                r.append(int(input()))
            self.m1.append(r)

    def DisplayArr(self):
        print("the entred matrix is ", self.m1)

size = int(input("enter the size : "))

m1 = []


met1 = Matrix(size,m1)
met1.GetArr()
met1.DisplayArr()

