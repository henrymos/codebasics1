#- * - coding: utf - 8 -*-
"""
Created on Tue Apr 14 11:37:08 2020

@author: HenryMos
"""

import turtle

wn = turtle.Screen()
wn.title("Pong by Thabo")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.penup()
paddle_a.goto(0, -290)

# Bricks
bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(0, 290)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(-70, 290)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(-140, 290)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(-210, 290)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(-280, 290)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(70, 290)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(140, 290)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(210, 290)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(280, 290)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(0, 260)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(-70, 260)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(-140, 260)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(-210, 260)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(-280, 260)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(70, 260)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(140, 260)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(210, 260)

bricks = turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("black")
bricks.shapesize(stretch_wid=1, stretch_len=3)
bricks.penup()
bricks.goto(280, 260)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, -290)
ball.dx = 0.5
ball.dy = 0.5


# Game functions
def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)


def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)


wn.listen()
wn.onkeypress(paddle_a_left, "a")
wn.onkeypress(paddle_a_right, "d")

# Main functions
while True:
    wn.update()
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < - 390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() < - 290:
        ball.goto(0, -270)
        ball.dy *= -1

        # paddle and ball collision
    if (ball.ycor() < -290) and (ball.xcor() < paddle_a.xcor() + 40 and ball.xcor() > paddle_a.xcor() - 40):
        ball.sety(-290)
        ball.dy *= -1
