
import turtle as trtl
import random

number = trtl.Turtle()

# ask for colors
custom_colors = trtl.textinput("Do you want custom colors","Enter yes/no")
colors = ["red","orange","gold","green","blue","purple"]
if (custom_colors == "yes"):
    color6 = trtl.textinput("What color should the 6 be?","Enter color here")
    color7 = trtl.textinput("What color should the 7 be?","Enter color here")
else:
    color6 = random.choice(colors)
    color7 = random.choice(colors)
    
#ask for size
custom_size = trtl.textinput("Do you wanta custom size","Enter yes/no")
if custom_size == "yes":
    size6 = trtl.numinput("What size should it be?","Enter size here")
    size7 = trtl.numinput("What size should it be?","Enter size here")
else:
    size6 = 67
    size7 = 67
#setup custom turtle
 

# draw the 6
number.penup()
number.goto(-50,0)
number.pendown()
number.color(color6)
number.setheading(90)
number.circle(size6,180)
number.forward(1.4*size6)
x = number.xcor()
y = number.ycor()
number.penup()
number.goto(x,y)
number.pendown()
number.circle(size6)
number.penup()

#draw the 7
y = 0 + size7
number.goto(50,y)
number.color(color7)
number.pendown()
number.setheading(0)
number.forward(size7*2)
number.setheading(240)
number.forward(size7*4)



wn = trtl.Screen()
wn.mainloop()




