# Name: Johnson Daniel
# Program: Code Lagos FinalProject
# Project Topic: C.B.T Test Creation
# E-mail: elguajeshawn@gmail.com
# Tel: 08036545548

print("This is codes Lagos C.B.T. Project for college student")
print("Select the letters with the correct option")
Score=0
Question1=input("1. How many sides has a triangle?\n(a)4\n(b)12\n(c)21\n(d)30\n")
if (Question1.lower()=="a"):
    print("Correct")
    Score = Score+1
else:
    print("You are wrong")
    

Question2=input("2. What is the line that run through two edge of a rectangle called ?\n(a)transverse\n(b)bisector\n(c)diagonal\n(d)perpendicular\n")
if (Question2.lower()=="c"):
    print("Correct")
    Score = Score+1
else:
    print("You are wrong")

Question3=input("3. How many sides has a heptagon?\n(a)4\n(b)7\n(c)8\n(d)6\n")
if (Question3.lower()=="b"):
    print("Correct")
    Score = Score+1
else:
    print("You are wrong")

Question4=input("4. The force that returns every objects back to the centre of the earth is?\n(a)gravitational\n(b)centripetal\n(c)centrifugal\n(d)viscous\n")
if (Question4.lower()=="a"):
    print("Correct")
    Score = Score+1
else:
    print("You are wrong")

Question5=input("5. The internal friction between the layers of liquids or gas in motion is?\n(a)drag\n(b)friction\n(c)viscosity\n(d)laminar\n")
if (Question5.lower()=="c"):
    print("Correct")
    Score = Score+1
else:
    print("You are wrong")

Question6=input("6. which of the following is not a form of energy?\n(a)heat\n(b)solar\n(c)electrical\n(d)calories\n")
if (Question6.lower()=="d"):
    print("Correct")
    Score = Score+1
else:
    print("You are wrong")

Question7=input("7. The unit of energy is?\n(a)joules\n(b)watts\n(c)pascal\n(d)newton\n")
if (Question7.lower()=="a"):
    print("Correct")
    Score = Score+1
else:
    print("You are wrong")


Question8=input("8. The unit of pressure is?\n(a)joules\n(b)watts\n(c)pascal\n(d)newton\n")
if (Question8.lower()=="c"):
    print("Correct")
    Score = Score+1
else:
    print("You are wrong")


Question9=input("9. The velocity needed for an astronomical object to go beyond the influence of gravity is?\n(a)jump\n(b)space\n(c)disappearance\n(d)escape\n")
if (Question9.lower()=="d"):
    print("Correct")
    Score = Score+1
else:
    print("You are wrong")


Question10=input("10. What is the force acting normally per unit area?\n(a)force\n(b)pressure\n(c)power\n(d)energy\n")                
if (Question10.lower()=="b"):
    print("You are correct")
    Score = Score+1
else:
    print("You are wrong")
print("Your Score is", Score)

