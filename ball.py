from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(x=0, y=-200)
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(x=0, y=-200)
        self.x_move = 1
        self.y_move = 1
        self.bounce_x()
        self.move()

    def reverse(self):
        self.bounce_x()
        self.bounce_y()

    def increase_level(self):
        if self.x_move != 10 and self.y_move != 10:
            self.x_move += 0.5
            self.y_move += 0.5
