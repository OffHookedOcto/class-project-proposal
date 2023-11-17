from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 150)
    angle = int(random() * 550)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()