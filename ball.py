from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super(). __init__()
        self.speed("slow")
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x=10
        self.y=10

    def move(self):
        new_x=self.xcor()+self.x
        new_y=self.ycor()+self.y
        self.goto(new_x, new_y)

    def bounce(self):
        self.y *= (-1)

    def bounce_padle(self):
        self.x *= (-1)
        if self.x < 0:
            self.x -= 2.5
        else:
            self.x += 2.5

    def reset_ball(self):
        self.x = 10
        self.x *= (-1)
        self.goto(0, 0)