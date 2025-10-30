#setup
import turtle as trtl
import random as rand

wn = trtl.Screen()

#Setting difficulty for how much turtles spawn 





#Random spawning turtle on the screen 
def random_turtle():
    x = rand.randint(-300,300)
    y = rand.randint(-300,300)
    objects = trtl.Turtle()
    objects.penup()
    objects.goto(x,y)






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
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(200,200)


def score_count():
    score_writer.clear()
    global score
    score +=1
    print(score)
    score_writer.clear()
    score_writer.write(score, move=False, align='left', font=("Arial", 24, "normal"))

while 1 == 1:
    random_turtle()
#Turtle hits turtle ends game



#End game screen with scoreboard




#
wn = trtl.Screen()
wn.setup(width=600, height=600)
wn.cv._rootwindow.resizable(False, False)
wn.mainloop()