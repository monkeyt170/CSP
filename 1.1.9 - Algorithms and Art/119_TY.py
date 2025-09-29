import turtle as trtl
painter = trtl.Turtle()
# ask for colors
color6 = trtl.textinput("What color should the 6 be?","Enter color here")
color7 = trtl.textinput("What color should the 7 be?","Enter color here")
 
#ask for size
size6 = trtl.textinput("What size should it be?","Enter size here")
size7 = trtl.textinput("What size should it be?","Enter size here")

#setup custom turtle
# draw the 6
painter.penup()
painter.goto(50,0)
painter.pendown()
painter.color(color6)
painter.setheading(90)
painter.circle(50,180)
painter.forward(60)
painter.penup()
painter.goto(-50,-70)
painter.pendown()
painter.circle(50)
#draw the 7 



wn = trtl.Screen()
wn.mainloop()




