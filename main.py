# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 17:09:13 2023

@author: Mansoor
"""

import turtle as t
import random as r

screen = t.Screen()

israceon = False
screen.setup(width=600,height=400)
user_input = screen.textinput('Bet on Turtle','Which turtle will win the race ')

color = ['red','green','orange','blue','yellow']
y_position = [-60,-30,0,30,60]

allTurtle = []

for i in range(0,5):
    newturtle = t.Turtle(shape='turtle')
    newturtle.color(color[i])
    newturtle.penup()
    newturtle.goto(x=-280,y=y_position[i])
    allTurtle.append(newturtle)
    
if user_input:
    israceon = True

while israceon:
    for turtle in allTurtle:
        if turtle.xcor() > 275:
            winning = turtle.pencolor()
            if winning == user_input:
                print(f'Congradulations ,{winning} won the race')
            else:
                print(f'You lose, {winning} won the race')
            israceon = False
            break
        rand_distance = r.randint(0, 12)
        turtle.fd(rand_distance)
        
screen.exitonclick()