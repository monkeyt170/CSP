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


def envolope_screen():
    envolope.goto(100,100)
    envolope.goto(100,-100)
    envolope.goto(-100,-100)
    envolope.goto(-100,100)
    envolope.goto(0,0)
    envolope.goto(-100,100)
    envolope.goto(100,100)
    envolope.goto(0,0)

yn = trtl.Turtle()
no = trtl.Turtle()
def yn_screen(x, y):
    envolope.clear()
    envolope.hideturtle()
    yn.write("Would you like to play a game?", align="center", font=("Arial", 28, "bold"))
    yn.penup()
    yn.goto(-100,-100)
    yn.write("yes", align="center", font=("Arial", 28, "bold"))
    no.penup()
    no.goto(100,-100)
    no.write("no", align="center", font=("Arial", 28, "bold"))

etrtl = trtl.Turtle()
etrtl.hideturtle()
def maze(x, y):
    yn.clear()
    no.clear()
    yn.hideturtle()
    no.hideturtle()
    etrtl.penup()
    etrtl.goto(100, 100)
    etrtl.write("Click here when you have completed the maze", align="center", font=("Arial", 28, "bold"))
    etrtl.showturtle()
    etrtl.shape("circle")
    movertrtl.penup()
    movertrtl.goto(-100, 60)
    movertrtl.setheading(270)
    movertrtl.showturtle()
    wn.bgpic(rand.choice(mazes))

def encscreen(x,y):
    wn.clear()
    wn.bgpic(rand.choice(encimgs))

movertrtl = trtl.Turtle()
movertrtl.hideturtle()
def up():
    movertrtl.setheading(90)
    movertrtl.forward(10)
def down():
    movertrtl.setheading(270)
    movertrtl.forward(10)
def left():
    movertrtl.setheading(180)
    movertrtl.forward(10)
def right():
    movertrtl.setheading(0)
    movertrtl.forward(10)
wn.listen()
wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.onkey(left, "Left")
wn.onkey(right, "Right")

etrtl.onclick(encscreen)

    


    

envolope.onclick(yn_screen)
yn.onclick(maze)





envolope_screen()



wn.mainloop()
