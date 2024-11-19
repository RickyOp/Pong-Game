import turtle
import winsound
import pygame

# Initialize Pygame mixer and load background music
pygame.mixer.init()
pygame.mixer.music.load("gamingmusic.wav")

# Start playing background music in a loop
pygame.mixer.music.play(-1)

wn = turtle.Screen()
wn.title("Pong")
wn.bgpic("bg.png") 
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Function to handle player input
def get_player_names():
    player_a = wn.textinput("Player A's Name", "Enter Player A's Name:")
    player_b = wn.textinput("Player B's Name", "Enter Player B's Name:")
    return player_a, player_b

# Play button setup
play_button = turtle.Turtle()
play_button.speed(0)
play_button.shape("square")
play_button.color("green")
play_button.shapesize(stretch_wid=2, stretch_len=5)
play_button.penup()
play_button.goto(0, 0)

# Play button text setup
play_text = turtle.Turtle()
play_text.speed(0)
play_text.color("white")
play_text.penup()
play_text.hideturtle()
play_text.goto(0, -20)
play_text.write("Play", align="center", font=("Arial", 24, "normal"))

# Function to handle play button click
def click_play(x, y):
    if -50 < x < 50 and -25 < y < 25:
        start_game()

# Bind play button click event
wn.onclick(click_play)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Scoring system
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Function to start the game
def start_game():
    global score_a, score_b  # Access the global variables

    # Get players' names
    player_a, player_b = get_player_names()

    # Hide play button and text
    play_button.hideturtle()
    play_text.clear()

    # Set players' names on the screen
    pen.clear()
    pen.write(f"{player_a}: {score_a}         {player_b}: {score_b}", align="center", font=("Arial", 24, "normal"))

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(lambda: paddle_a.sety(paddle_a.ycor() + 20), "w")
    wn.onkeypress(lambda: paddle_a.sety(paddle_a.ycor() - 20), "s")
    wn.onkeypress(lambda: paddle_b.sety(paddle_b.ycor() + 20), "Up")
    wn.onkeypress(lambda: paddle_b.sety(paddle_b.ycor() - 20), "Down")

    # Main game loop
    while True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # Ball left and right
        if ball.xcor() > 350:
            score_a += 1
            pen.clear()
            pen.write(f"{player_a}: {score_a}         {player_b}: {score_b}", align="center", font=("Arial", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
        elif ball.xcor() < -350:
            score_b += 1
            pen.clear()
            pen.write(f"{player_a}: {score_a}         {player_b}: {score_b}", align="center", font=("Arial", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1 
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # Paddle border restriction
        if paddle_a.ycor() + 50 > 290:
            paddle_a.sety(240)
        elif paddle_a.ycor() - 50 < -290:
            paddle_a.sety(-240)

        if paddle_b.ycor() + 50 > 290:
            paddle_b.sety(240)
        elif paddle_b.ycor() - 50 < -290:
            paddle_b.sety(-240)


# Main loop
turtle.done()
