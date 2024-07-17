import turtle as tt
import random as rd

def left():
    tt.setheading(180)
    tt.forward(10)

def right():
    tt.setheading(0)
    tt.forward(10)

def up():
    tt.setheading(90)
    tt.forward(10)

def down():
    tt.setheading(270)
    tt.forward(10)

def pen_updown():
    if tt.isdown():
        tt.penup()
    else:
        tt.pendown()

def switch_color():
    colors = ['red', 'green', 'blue', 'orange', 'black']
    choice = rd.choice(colors)
    tt.color(choice)

def clear():
    tt.clear()
    tt.color('black')