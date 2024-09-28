import turtle
import time
import random

delay=0.1

wn=turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor('green')
wn.setup(width=600,height=600)
wn.tracer(0)  #turns off the screen updates

#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
#head.direction = 'stop' initially stop then change to up when providing func
head.direction = 'stop'

#Snake food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

#snake body segment just empty list
segments=[]
#Variables
Score=0
High_Score=0

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:0 High Score:0",align="center",font=("Courier",24,"normal"))
#Functions
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

def move():
    if head.direction =="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction =="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction =="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction =="right":
        x=head.xcor()
        head.setx(x+20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_right, 'Right')
wn.onkeypress(go_left, 'Left')

#main game loop
while True:
    wn.update()

    #check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000 )

        #clear the segments list
        segments.clear()

        # Reset the score
        Score = 0
        High_Score = 0
        pen.clear()
        pen.write("Score:{} High Score:{}".format(Score, High_Score), align="center", font=("Courier", 24, "normal"))

        # reset delay
        delay = 0.01

    #check for a collision with the food
    if head.distance(food) < 20:
        #move the food to random place
        x=random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #Add a segment in body
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

        #Shorten delay everytime it touches food
        delay-=0.001

        # Increase the score
        Score += 10
        if Score > High_Score:
            High_Score = Score
        pen.clear()
        pen.write("Score:{} High Score:{}".format(Score, High_Score), align="center", font=("Courier", 24, "normal"))
    #move the end segment first
    for index in range(len(segments)-1,0,-1):#9-8-7-6...0
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    # check for a collision with the border
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments list
            segments.clear()

            # Reset the score
            Score = 0
            High_Score = 0
            pen.clear()
            pen.write("Score:{} High Score:{}".format(Score, High_Score), align="center",
                      font=("Courier", 24, "normal"))

            #reset delay
            delay=0.01

    time.sleep(delay)

wn.mainloop()
