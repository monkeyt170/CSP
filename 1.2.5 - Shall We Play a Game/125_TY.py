#setup
import turtle as trtl
import random as rand

wn = trtl.Screen()

#Setting difficulty for how much turtles spawn 





#Random spawning turtle on the screen 





#Turtle moving as an object with arrow keys
mover = trtl.Turtle()
mover.penup()
score = 0

def move_direction(active_turtle,d):
    active_turtle.setheading(d)
    active_turtle.forward(20)
    score_count()

def left_move():
    move_direction(mover,180)

def right_move():
    move_direction(mover,0)

def up_move():
    move_direction(mover,90)

def down_move():
    move_direction(mover,270)

wn.listen()
wn.onkeypress(left_move,"Left")
wn.onkeypress(right_move,"Right")
wn.onkeypress(up_move,"Up")
wn.onkeypress(down_move,"Down")

#Score of moving the object
score = trtl.Turtle()
score.penup()
score.hideturtle()
score.goto(500,550)

def score_count():
    global score
    score +=1
    score.write("Arial", 24, "normal")
    


#Turtle hits turtle ends game



#End game screen with scoreboard



wn = trtl.Screen()
wn.setup(width=600, height=600)
wn.cv._rootwindow.resizable(False, False)
wn.mainloop()