#project : in built functions calculator
#author : Ajayi 

import math
print("This is an in-built function calculator.....")
Menu=int(input("(1)Square roots\t                             (2)Square's\n(3)Cylinder suface area and volume           (4) Area of a triangle \n"))
if Menu==1:
    sqrt=int(input("Enter your desired number: "))
    solu=math.sqrt(sqrt)
    print(" Your square root is",solu)
elif Menu==2:
     sq=int(input("Enter your desired number: "))
     answer=sq**2
     print(" Your square root is",answer)
elif Menu==3:
    pi=22/7
    Height=float(input("Height of the cylinder: "))
    Radius=float(input("Radius of the cylinder: "))
    Volume = pi*Radius*Radius*Height
    sur_area=((2*pi*Radius)*Height) + ((pi*Radius**2)*2)
    print("volume is",Volume)
    print("Suface Area is",sur_area)             
elif Menu==4:
    x=int(input("enter the tiangle height: "))
    y=int(input("enter the triangle base: "))
    area=(x*y)/2
    print("The area =", area )

else:
    print("NOT FOUND!")

