
# Name : Bubble Sort Animation
# Author : Soroush Javed Sulehri
# Liscence : MIT Liscence 
# Sorting Series Part 2(b)
# Email : soroushjaved@gmail.com

import turtle
import random
import time


# Inital Screen Setup
screen = turtle.Screen()
# Defining Screen Size
screen.setup(2000,2000)
# Complicated Argument mostly means that the turtle should not show every step of animation
screen.tracer(10,10)
screen.title('Bubble Sort')
turtle.speed(0)
turtle.hideturtle()

# Taking number of bars as input
#n = int(input("Enter the number of bars to randomly distribute (10-100) : "))
n = int(input("Enter the number of elements you want in the array : "))
l = [0] * n
# Random Generation of list 
for i in range(n):
    l[i] = random.randint(50,600)

# Bar Drawing Function
def draw_bar(x,y,w,h):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()

# Multiple bars drawing and Updating Function 
def draw_bars(l, n):
    w = 500/n
    x = -400
    for i in range(len(l)):
        if i == c : turtle.fillcolor("red")
        elif i == c2: turtle.fillcolor("turquoise")
        else:turtle.fillcolor('Gray')
        draw_bar(x,-350,w,l[i])
        x = x + w
    screen.update()

# Main Function and Sorting 
def bubble_sort(l):
     global c
     global c2
     for i in range(n -1):
        for j in range(0, n-i-1):
             c = j
             c2 = j + 1
             if l[j] > l[j+1]: 
                 l[j], l[j+1] = l[j+1], l[j]
        screen.update()
        turtle.clear()
        draw_bars(l,n)
        screen.update()
        time.sleep(0.5) #time dealy added for sake for animation 


# Function Call 
bubble_sort(l)

    


   


    
            



