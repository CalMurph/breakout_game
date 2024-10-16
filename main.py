
from turtle import Turtle, Screen
from ball import Ball

# Constants
FONT = ("Courier", 50)
LIVES = 5
SCORE = 0


class Block(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.penup()
        self.goto(x, y)


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=2.5, stretch_wid=0.5)
        self.goto(x, y)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = LIVES
        self.score = SCORE
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 255)
        self.write(f"LIVES: {self.lives} | SCORE: {self.score}", align="left", font=FONT)

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=645, height=700)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.blocks = self.create_blocks()
        self.paddles = self.create_paddles()
        self.ball = Ball()
        self.scoreboard = Scoreboard()

        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")

    def create_blocks(self):
        colors = ["red", "orange", "green", "yellow"]
        blocks = []
        x_coord = -288
        y_coord = 200

        for color in colors:
            for i in range(20):
                block = Block(color, x_coord, y_coord)
                blocks.append(block)
                if i % 10 == 9:
                    x_coord = -288
                    y_coord -= 25
                else:
                    x_coord += 63
        return blocks

    def create_paddles(self):
        paddles = []
        paddle_x = -30
        for _ in range(6):
            paddle = Paddle(paddle_x, -200)
            paddle_x += 20
            paddles.append(paddle)
        return paddles

    def move_left(self):
        for paddle in self.paddles:
            paddle.goto(paddle.xcor() - 30, paddle.ycor())
        self.screen.update()

    def move_right(self):
        for paddle in self.paddles:
            paddle.goto(paddle.xcor() + 30, paddle.ycor())
        self.screen.update()

    def check_collisions(self):
        for block in self.blocks:
            if block.distance(self.ball) < 35:
                self.ball.bounce()
                block.hideturtle()
                block.goto(500, 500)
                points = self.get_points(block)
                self.scoreboard.increase_score(points)

        midpoint = len(self.paddles) // 2
        for paddle in self.paddles:
            if paddle.distance(self.ball) < 30 and self.ball.y_move < 0 and self.ball.ycor() < -200:
                if paddle == self.paddles[0]:
                    self.ball.y_move = 1
                    self.ball.x_move = -4
                elif paddle == self.paddles[-1]:
                    self.ball.y_move = 1
                    self.ball.x_move = 4
                else:
                    self.ball.x_move = -3 if self.ball.x_move < 0 else 3
                    self.ball.y_move = 3

        if self.ball.ycor() > 400 or self.ball.ycor() < -400:
            self.ball.refresh()
            self.scoreboard.decrease_lives()

        if self.ball.xcor() > 310 or self.ball.xcor() < -310:
            self.ball.bat()

        if self.ball.ycor() > 340:
            self.ball.bounce()

    def get_points(self, block):
        block_index = self.blocks.index(block)
        if block_index < 20:
            return 7
        elif block_index < 40:
            return 5
        elif block_index < 60:
            return 3
        else:
            return 1

    def play(self):
        game_on = True
        while game_on:
            self.ball.move()
            self.screen.update()
            self.check_collisions()

            if self.scoreboard.score == 308:
                self.display_message("YOU DESTROYED ALL THE BLOCKS, WELL DONE!", "blue")
                game_on = False

            if self.scoreboard.lives == 0:
                self.display_message("GAME OVER", "red")
                game_on = False

        self.screen.exitonclick()

    def display_message(self, message, color):
        self.scoreboard.goto(0, 0)
        self.scoreboard.color(color)
        self.scoreboard.write(message, align="center", font=("Courier", 36 if color == "blue" else 50))


if __name__ == "__main__":
    game = Game()
    game.play()















