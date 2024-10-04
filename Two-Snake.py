import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off the screen updates

# Snake head1
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('red')
head.penup()
head.goto(0, 0)
head.direction = 'stop'


# Snake head2
head1 = turtle.Turtle()
head1.speed(0)
head1.shape('square')
head1.color('white')
head1.penup()
head1.goto(0, 0)
head1.direction = 'stop'

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('green')
food.penup()
food.goto(0, 100)

# Snake body segments (empty list)
segments = []
segments1 = []

# Variables
Score = 0
High_Score = 0  # Only reset this manually, not after every game

# Pen for displaying score
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1 Score: 0 High Score: 0", align="center", font=("Courier", 20, "normal"))

# Pen for displaying score
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.shape('square')
pen1.color('white')
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 225)
pen1.write("Player 2 Score: 0 High Score: 0", align="center", font=("Courier", 20, "normal"))

# Functions
def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

# Functions1
def go_up1():
    if head1.direction != 'down':
        head1.direction = 'up'

def go_down1():
    if head1.direction != 'up':
        head1.direction = 'down'

def go_right1():
    if head1.direction != 'left':
        head1.direction = 'right'

def go_left1():
    if head1.direction != 'right':
        head1.direction = 'left'

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head1.direction == "up":
        y = head1.ycor()
        head1.sety(y + 20)

    if head1.direction == "down":
        y = head1.ycor()
        head1.sety(y - 20)

    if head1.direction == "left":
        x = head1.xcor()
        head1.setx(x - 20)

    if head1.direction == "right":
        x = head1.xcor()
        head1.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_right, 'Right')
wn.onkeypress(go_left, 'Left')

wn.onkeypress(go_up1, 'w')
wn.onkeypress(go_down1, 's')
wn.onkeypress(go_right1, 'd')
wn.onkeypress(go_left1, 'a')

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score but keep the high score
        Score = 0
        pen.clear()
        pen.write(f"player 1 Score: {Score} High Score: {High_Score}", align="center", font=("Courier", 20, "normal"))

        # Reset the delay
        delay = 0.1

    # Check for a collision with the border
    if head1.xcor() > 290 or head1.xcor() < -290 or head1.ycor() > 290 or head1.ycor() < -290:
        time.sleep(1)
        head1.goto(0, 0)
        head1.direction = 'stop'

        # Hide the segments
        for segment in segments1:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments1.clear()

        # Reset the score but keep the high score
        Score = 0
        pen1.clear()
        pen1.write(f"player 2 Score: {Score} High Score: {High_Score}", align="center", font=("Courier", 20, "normal"))

        # Reset the delay
        delay = 0.1

    # Check for a collision with the food
    if head.distance(food) < 20 :
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment to the snake's body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay after eating food
        delay -= 0.001

        # Increase the score
        Score += 10
        if Score > High_Score:
            High_Score = Score  # Update high score if current score is greater
        pen.clear()
        pen.write(f"Player 1 Score: {Score} High Score: {High_Score}", align="center", font=("Courier", 20, "normal"))

         
    
     # Check for a collision with the food
    if head1.distance(food) < 20 :
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment to the snake's body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments1.append(new_segment)

        # Shorten the delay after eating food
        delay -= 0.001

        # Increase the score
        Score += 10
        if Score > High_Score:
            High_Score = Score  # Update high score if current score is greater
        pen1.clear()
        pen1.write(f"player 2 Score: {Score} High Score: {High_Score}", align="center", font=("Courier", 20, "normal"))

    # Move the segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

        # Move the segments
    for index in range(len(segments1) - 1, 0, -1):
        x = segments1[index - 1].xcor()
        y = segments1[index - 1].ycor()
        segments1[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments1) > 0:
        x = head1.xcor()
        y = head1.ycor()
        segments1[0].goto(x, y)

    move()

    # Check for a collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score but not the high score
            Score = 0
            pen.clear()
            pen.write(f"Player 1 Score: {Score} High Score: {High_Score}", align="center", font=("Courier", 20, "normal"))

            # Reset the delay
            delay = 0.1

    # Check for a collision with the body
    for segment in segments1:
        if segment.distance(head1) < 20:
            time.sleep(1)
            head1.goto(0, 0)
            head1.direction = 'stop'

            # Hide the segments
            for segment in segments1:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments1.clear()

            # Reset the score but not the high score
            Score = 0
            pen.clear()
            pen.write(f"Score: {Score} High Score: {High_Score}", align="center", font=("Courier", 20, "normal"))

            # Reset the delay
            delay = 0.1

    time.sleep(delay)

wn.mainloop()
