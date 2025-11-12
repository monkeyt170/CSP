#Start screen with email icon 
#Y/n screen after clicking on email icon
#Maps for the game 
#End screen after finishing the game
#Movement in the game using arrow keys

import turtle as trtl
envolope = trtl.Turtle()

maze1img = "maze1.png"
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

def maze1(x, y):
    yn.clear()
    no.clear()
    yn.hideturtle()
    no.hideturtle()
    movertrtl.penup()
    movertrtl.goto(-100, 60)
    movertrtl.setheading(270)
    wn.bgpic(maze1img)

movertrtl = trtl.Turtle()
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

def enourage_screen():
    if movertrtl.pos == (-100,50):
        wn.clear()
        envolope.write("test")
        
    


    

envolope.onclick(yn_screen)
yn.onclick(maze1)





envolope_screen()



wn.mainloop()
