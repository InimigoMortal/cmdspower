import turtle
from random import randint

turtle.setup(900,500)
t = turtle.Turtle()
t.penup()
t.color('yellow')
t.shape('triangle')
t.turtlesize(1)
win = turtle.Screen()
win.bgcolor('black')
cores = ['green','purple','black','white','blue','orange']
formas = ['circle','square','turtle','triangle']
def left():
    t.left(30)
    novaforma = t.shape(formas[randint(0,len(formas)-1)])
    novacor = win.bgcolor(cores[randint(0,len(cores)-1)])
    novotam = t.turtlesize(randint(1, 10))
def r():
    t.right(30)
    novaforma = t.shape(formas[randint(0, len(formas) - 1)])
    novacor = win.bgcolor(cores[randint(0,len(cores)-1)])
    novotam = t.turtlesize(randint(1, 10))
def up():
    t.forward(10)
    novaforma = t.shape(formas[randint(0, len(formas) - 1)])
    novacor = win.bgcolor(cores[randint(0,len(cores)-1)])
    novotam = t.turtlesize(randint(1, 10))
def down():
    t.forward(-10)
    novaforma = t.shape(formas[randint(0, len(formas) - 1)])
    novacor = win.bgcolor(cores[randint(0,len(cores)-1)])
    novotam = t.turtlesize(randint(1, 5))




win.onkey(left,'Left')
win.onkey(r,'Right')
win.onkey(up,'Up')
win.onkey(down,'Down')
win.listen()
win.mainloop()

