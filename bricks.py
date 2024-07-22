from turtle import Turtle
from random import choice

colors = ['#FFBA86', '#F6635C', '#C23373', '#79155B']
x_positions = [-200, -150, -100, -50, 0, 50, 100, 150, 200, ]
y_positions = [-20, 10, 40, 70]

size = [2, 2]


class Brick(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_bricks = []
        self.brick_pallet()

    def brick_pallet(self):
        for i in range(0, 4):
            color = colors[i]
            y_pos = y_positions[i]
            for x_pos in x_positions:
                self.create_brick(color, y_pos, x_pos)

    def create_brick(self, color, y_pos, x_pos):
        new_food = Turtle('square')
        new_food.shapesize(1, choice(size))
        new_food.penup()
        new_food.color(color)
        new_food.goto(x_pos, y_pos)
        self.all_bricks.append(new_food)

    def increase_level(self):
        for item in range(0, len(y_positions)):
            y_positions[item] = y_positions[item] - 10
        self.brick_pallet()
