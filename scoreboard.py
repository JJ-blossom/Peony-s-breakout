from turtle import Turtle

FONT = ('Helvetica', 35, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.lives_remaining = 2
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(-200, 200)
        self.update_score()

    def update_score(self):
        self.clear()
        lives = ""
        for life in range(0, self.lives_remaining):
            life = "🤍"
            lives += life
        self.write(f'Level: {self.level} {lives} Score: {self.score}', align='left', font=FONT)

    def increase_points(self):
        self.score += 1
        self.update_score()

    def increase_level(self):
        self.level += 1
        self.update_score()

    def decrease_lives(self):
        self.lives_remaining -= 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
        with open('scores.txt', mode='r') as file:
            current_high = file.read()
        if int(current_high) < self.score:
            with open('scores.txt', mode='w') as data:
                data.write(str(self.score))
            self.goto(0, -50)
            self.write(f"NEW HIGH SCORE", align="center", font=FONT)
