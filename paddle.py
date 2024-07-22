from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(1, 5)
        self.goto(x=0, y=-230)
        self.move_speed = 70
        self.current_x = 0

    def move_left(self):
        if self.xcor() > -200:
            self.backward(self.move_speed)

    def move_right(self):
        if self.xcor() < 200:
            self.forward(self.move_speed)
