#Start screen with email icon 
#Y/n screen after clicking on email icon
#Maps for the game 
#End screen after finishing the game
#Movement in the game using arrow keys

import turtle as trtl
envolope = trtl.Turtle()

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
yn.hideturtle()
def yn_screen(x, y):
    envolope.clear()
    envolope.hideturtle()
    yn.write("Would you like to play a game?", align="center", font=("Arial", 28, "bold"))
    yn.penup()
    yn.goto(-100,-100)
    yn.write("yes", align="center", font=("Arial", 28, "bold"))


    

envolope.onclick(yn_screen)




envolope_screen()


wn = trtl.Screen()
wn.mainloop()
