import turtle as trtl
painter = trtl.Turtle()
# ask for colors
color6 = trtl.textinput("What color should the 6 be?","Enter color here")
color7 = trtl.textinput("What color should the 7 be?","Enter color here")
 
#ask for size
size6 = trtl.numinput("What size should it be?","Enter size here")
size7 = trtl.numinput("What size should it be?","Enter size here")

#setup custom turtle


# draw the 6
painter.penup()
painter.goto(-50,0)
painter.pendown()
painter.color(color6)
painter.setheading(90)
painter.circle(size6,180)
painter.forward(1.4*size6)
x = painter.xcor()
y = painter.ycor()
painter.penup()
painter.goto(x,y)
painter.pendown()
painter.circle(size6)
painter.penup()
#draw the 7
painter.goto(50,50)
painter.color(color7)
painter.pendown()
painter.setheading(0)
painter.forward(size7*2)
painter.setheading(240)
painter.forward(size7*4)



wn = trtl.Screen()
wn.mainloop()




