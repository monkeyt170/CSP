
import turtle as trtl
import random

number = trtl.Turtle()

# ask for bolding
bold= trtl.textinput("Do you want bold","Enter yes/no")
if bold == "yes":
    number.pensize(6.7)
else:
    number.pensize(1)

# ask for colors
custom_colors = trtl.textinput("Do you want custom colors","Enter yes/no")
colors = ["red","orange","gold","green","blue","purple"]
is_error = False
if (custom_colors == "yes"):
    while not is_error:
        color6 = trtl.textinput("What color should the 6 be?","Enter color here")
        color7 = trtl.textinput("What color should the 7 be?","Enter color here")
        try:
            number.color(color6)
            number.color(color7)
            is_error=True
        except trtl.TurtleGraphicsError:
            is_error=False
else:
    color6 = random.choice(colors)
    color7 = random.choice(colors)
    
#ask for size
custom_size = trtl.textinput("Do you want a custom size","Enter yes/no")
if custom_size == "yes":
    size6 = trtl.numinput("What size should the 6 be?","Enter size here")
    size7 = trtl.numinput("What size should the 7 be?","Enter size here")
else:
    size6 = 67
    size7 = 67
#setup custom turtle
trtl.addshape("6",((10,10),(-10,10),(-10,-10),(10,-10),(10,-2),(4,-2),(4,-8),(-2,-8),(-2,-2),(4,-2),(-5,-2),(-5,7),(10,7)))
trtl.addshape("7",((-10,8),(-10,10),(10,10),(-8,-10),(-10,-10),(-10,-8),(8,8)))

# draw the 6
number.penup()
number.shape("6")
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
number.shape("7")
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




