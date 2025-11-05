#setup
import turtle as trtl
import random as rand
import time


wn = trtl.Screen()
wn.setup(width=600, height=600)
wn.cv._rootwindow.resizable(False, False)

#Setting difficulty for how much turtles spawn 
difficulty = trtl.textinput("What difficulty do you want?","Easy or Hard")
if difficulty == "easy":
    timer = 1
else:
    difficulty = "hard"
    timer = 0.1


#Random spawning turtle on the screen 
turtles = []
def random_turtle():
    x = rand.randint(-300,300)
    y = rand.randint(-300,300)
    objects = trtl.Turtle()
    objects.hideturtle()
    objects.color("red")
    objects.penup()
    objects.goto(x,y)
    objects.showturtle()
    turtles.append(objects)

#Turtle moving as an object with arrow keys
mover = trtl.Turtle()
mover.color("blue")
mover.penup()
score = 0

def move_direction(active_turtle,d):
    active_turtle.setheading(d)
    active_turtle.forward(20)
    score_count(active_turtle)

def left_move():
    global mover
    if  mover.xcor() > -300 - 20:
        move_direction(mover,180)

def right_move():
    global mover
    if  mover.xcor() < 300 - 20:
        move_direction(mover,0)

def up_move():
    global mover
    if  mover.ycor() < 300 - 20:
        move_direction(mover,90)

def down_move():
    global mover
    if  mover.ycor() > -300 + 20:
        move_direction(mover,270)

wn.listen()
wn.tracer(3)
wn.onkeypress(left_move,"Left")
wn.onkeypress(right_move,"Right")
wn.onkeypress(up_move,"Up")
wn.onkeypress(down_move,"Down")

#Score of moving the object
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(250,250)


def score_count(active_turtle):
    active_turtle.clear()
    global score
    score +=1
    active_turtle.clear()
    active_turtle.write(score, move=False, align='left', font=("Arial", 24, "normal"))


#Turtle hits turtle ends game
collide = False
def detect_collision(turtle1, group):
    global collide
    for turtle2 in group:
        if turtle1 != turtle2 and turtle1.distance(turtle2) < 10:
            collide = True
            turtle2.reset() 
            break

while collide == False:
    random_turtle()
    time.sleep(timer)
    detect_collision(mover, turtles)

if collide == True:
    wn.clear()

#End game screen with score
wn.clear()
score_writer.goto(0,0)
score_writer.write(difficulty.upper() + " Mode: Your score was a " + str(score), move=False, align='center', font=("Arial", 24, "normal"))


#
wn = trtl.Screen()
wn.mainloop()