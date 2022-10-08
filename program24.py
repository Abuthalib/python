# Write a menu driven program to calculate the area of a given object.
class Area:
    def a_circle(self): {}

    def a_rectangle(self): {}

    def a_square(self): {}

    def a_triangle(self): {}


class MyClass(Area):
    def a_circle(self):
        radius = (float(input("enter the radius : ")))
        area = 3.14 * radius * radius
        print('area of circle : ', area)

    def a_rectangle(self):
        height = (float(input("enter the height : ")))
        width = (float(input("enter the width : ")))
        area = height * width
        print("area of rectangle", area)

    def a_square(self):
        side = (float(input("enter the side : ")))
        area = side * side
        print("the area of square : ", area)

    def a_triangle(self):
        base = (float(input("enter the base :")))
        height = (float(input("enter the height :")))
        area = 1 / 2 * base * height


are1 = MyClass()
print("1 - circle ")
print("2 - rectangle")
print("3 - square")
print("4 - triangle")

ch = (int(input("enter the choice: ")))
if ch == 1:
    are1.a_circle()
elif ch==2 :
    are1.a_triangle()
elif ch==3:
    are1.a_square()
elif ch==4:
    are1.a_triangle()
else:
    print("invalid selection")
