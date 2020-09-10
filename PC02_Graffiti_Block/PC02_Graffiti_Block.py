#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Caden
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

# for hood
Turtle()
up()
right(90)
forward(25)
left(135)
down()
width(6)
forward(75)
left(25)
forward(30)
left(25)
forward(90)
left(45)
forward(60)
left(20)
forward(20)
left(55)
forward(50)
left(45)
forward(90)
left(30)
forward(60)
left(25)
forward(65)
right(160)
width(10)
forward(30)
width(20)
right(15)
forward(30)
width(30)
right(15)
forward(30)
right(10)
width(40)
forward(40)
right(30)
width(66) # for order 66
forward(100)
right(30)
forward(30)
right(25)
forward(45)
width(40)
right(60)
forward(90)
right(55)
width(15)
forward(115)
right(40)
forward(80)
right(15)
forward(30)

# for eye 1
up()
goto(35,130)
color("DarkOrange1")
width(5)
down()
circle(10)

# for eye 1 iris
up()
color("gold1")
goto(37,127)
down()
circle(5)

# for eye 2
up()
goto(-25,120)
color("DarkOrange1")
down()
circle(10)

# for eye 2 iris
up()
color("gold1")
goto(-23,117)
down()
circle(5)

# for lightsaber
up()
goto(270,-250)
color("red")
left(210)
down()
width(20)
forward(300)
width(10)
color("ivory")
backward(300)

# for force lightning
up()
goto(109, -89)
color("turquoise1")
right(65)
width(7)
down()
forward(30)
right(45)
forward(25)
left(105)
forward(50)
right(70)
forward(30)
right(30)
forward(40)
left(25)
forward(50)
right(25)
forward(40)
left(45)
forward(50)

done()