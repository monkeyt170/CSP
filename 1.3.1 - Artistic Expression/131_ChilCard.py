#Start screen with email icon 
#Y/n screen after clicking on email icon
#Maps for the game 
#End screen after finishing the game
#Movement in the game using arrow keys

import turtle as trtl
import random as rand
envolope = trtl.Turtle()
mazes = ["maze1.png","maze2.png","maze3.png"]
encimgs = ["q1.png","q2.png","q3.png"]
wn = trtl.Screen()


def envolope_screen(speed, x ,y):
    envolope.speed(speed)
    envolope.goto(x,y)
    envolope.goto(x,-y)
    envolope.goto(-x,-y)
    envolope.goto(-x,y)
    envolope.goto(0,0)
    envolope.goto(-x,y)
    envolope.goto(x,y)
    envolope.goto(0,0)
    envolope.shape("circle")

yn = trtl.Turtle()
no = trtl.Turtle()
def yn_screen(x, y):
    envolope.clear()
    envolope.hideturtle()
    yn.write("Would you like to play a game?", align="center", font=("Arial", 28, "bold"))
    yn.penup()
    yn.goto(-100,-100)
    yn.write("yes", align="center", font=("Arial", 28, "bold"))
    yn.goto(-100, -110)
    yn.color("green")
    yn.shape("circle")
    no.penup()
    no.goto(100,-100)
    no.write("no", align="center", font=("Arial", 28, "bold"))
    no.goto(100, -110)
    no.color("red")
    no.shape("circle")

etrtl = trtl.Turtle()
etrtl.hideturtle()
movertrtl = trtl.Turtle()
movertrtl.hideturtle()
movertrtl.turtlesize(2)
movertrtl.color("black")

def maze(x, y):
    yn.clear()
    no.clear()
    yn.hideturtle()
    no.hideturtle()
    etrtl.penup()
    etrtl.goto(0, 300)
    etrtl.write("Click here when you have completed the maze", align="center", font=("Arial", 28, "bold"))
    etrtl.showturtle()
    etrtl.shape("circle")
    movertrtl.penup()
    movertrtl.goto(0, 250)
    movertrtl.setheading(270)
    movertrtl.showturtle()
    wn.bgpic(rand.choice(mazes))
    
end = 0
def encscreen(x,y):
    global end
    end = end + 1
    wn.clear()
    wn.bgpic(rand.choice(encimgs))
    movement_change_color(1,0,0)

def up():
    movertrtl.setheading(90)
    movertrtl.forward(20)
    movement_change_color(3,0,0)
def down():
    movertrtl.setheading(270)
    movertrtl.forward(20)
    movement_change_color(3,0,0)
def left():
    movertrtl.setheading(180)
    movertrtl.forward(20)
    movement_change_color(3,0,0)
def right():
    movertrtl.setheading(0)
    movertrtl.forward(20)
    movement_change_color(3,0,0)

wn.listen()
wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.onkey(left, "Left")
wn.onkey(right, "Right")


def movement_change_color(tracer, x, y):
    wn.tracer(tracer)
    while end == 0:
        if movertrtl.xcor() > x and movertrtl.ycor() > y:
            movertrtl.color("green")
        elif movertrtl.xcor() < x and movertrtl.ycor() > y:
            movertrtl.color("red")
    while end == 1:
        wn.bgcolor("blue")


etrtl.onclick(encscreen)
envolope.onclick(yn_screen)
yn.onclick(maze)
no.onclick(encscreen)
envolope_screen(0, 150, 100)



wn.mainloop()
